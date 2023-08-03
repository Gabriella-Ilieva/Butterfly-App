from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from butterfly.initiatives.forms import CreateInitiativeForm, EditInitiativeForm
from butterfly.initiatives.models import Initiative, Participation
from butterfly.main.forms import CommentForm, SearchForm


def all_initiatives(request):
    initiatives_list = Initiative.objects.all()
    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            initiatives_list = initiatives_list.filter(title__icontains=search_form.cleaned_data['title_filed'])

    paginator = Paginator(initiatives_list, per_page=4)
    page_number = request.GET.get("page", 1)
    try:
        initiatives = paginator.page(page_number)
    except PageNotAnInteger:
        initiatives = paginator.page(1)
    except EmptyPage:
        initiatives = paginator.page(paginator.num_pages)

    context = {
        "initiatives": initiatives,
        "search_form": search_form,
        "initiatives_list": initiatives_list,
    }

    return render(request, template_name='initiative/all_initiatives.html', context=context)


class CreateInitiativeView(LoginRequiredMixin, CreateView):
    template_name = 'initiative/add_initiative.html'
    form_class = CreateInitiativeForm
    success_url = reverse_lazy('all initiatives')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class DeleteInitiativeView(LoginRequiredMixin, DeleteView):
    model = Initiative
    template_name = 'initiative/delete_initiative.html'
    success_url = reverse_lazy('all initiatives')


@login_required
def edit_initiative(request, pk):
    initiative = Initiative.objects.get(pk=pk)
    form = EditInitiativeForm(instance=initiative)

    if request.method == "POST":
        form = EditInitiativeForm(request.POST, instance=initiative)
        if form.is_valid():
            form.save()
            return redirect('details initiative', pk=pk)
        else:
            print(form.errors)

    context = {
        "initiative": initiative,
        "form": form,
    }

    return render(request, 'initiative/edit_initiative.html', context)


def initiative_details(request, pk):
    initiative = Initiative.objects.get(pk=pk)
    comment_form = CommentForm()
    initiative.participated = False
    all_comments = initiative.comment_set.all()
    comments_count = all_comments.count()
    already_participated = Participation.objects.filter(user=request.user, to_initiative=initiative).count()
    if already_participated > 0:
        initiative.participated = True

    context = {
        "initiative": initiative,
        "all_comments": all_comments,
        "comment_form": comment_form,
        "comments_count": comments_count,
    }

    return render(request, 'initiative/details_initiative.html', context=context)


@login_required
def participate(request, pk):
    to_initiative = Initiative.objects.get(pk=pk)
    new_like, created = Participation.objects.get_or_create(user=request.user, to_initiative=to_initiative)
    if not created:
        new_like.delete()
    return redirect(request.META['HTTP_REFERER'])

