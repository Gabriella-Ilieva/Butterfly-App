from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from butterfly.initiatives.forms import CreateInitiativeForm, EditInitiativeForm
from butterfly.initiatives.models import Initiative, Participation


def all_initiatives(request):
    initiatives_list = Initiative.objects.all().order_by('date_of_publication')
    paginator = Paginator(initiatives_list, per_page=6)
    page_number = request.GET.get("page", 1)
    try:
        initiatives = paginator.page(page_number)
    except PageNotAnInteger:
        initiatives = paginator.page(1)
    except EmptyPage:
        initiatives = paginator.page(paginator.num_pages)

    context = {
        "initiatives": initiatives,
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
    # initiatives_list = Initiative.objects.all()
    #
    # if request.user.is_authenticated:
    #
    #     for current_initiative in initiatives_list:
    #         current_initiative.liked_by_user = current_initiative.participation_set \
    #             .filter(user=request.user) \
    #             .exists()
    initiative.participated = False
    if initiative.user == request.user:
        initiative.participated = True
    context = {
        "initiative": initiative,
    }

    return render(request, 'initiative/details_initiative.html', context=context)


@login_required
def participate(request, pk):
    initiative = Initiative.objects.get(pk=pk)

    kwargs = {
        'to_initiative': initiative,
        'user': request.user
    }

    part_obj = Participation.objects \
        .filter(**kwargs) \
        .first()

    if part_obj:
        part_obj.delete()
    else:
        new_part_obj = Participation(**kwargs)
        new_part_obj.save()

    return redirect(request.META['HTTP_REFERER'] + f"{pk}")