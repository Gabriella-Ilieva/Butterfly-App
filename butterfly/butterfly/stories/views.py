from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, FormView, ListView, UpdateView, DeleteView

from butterfly.main.forms import SearchForm
from butterfly.stories.forms import StoryForm, EditStoryForm
from butterfly.stories.models import Story


def show_all_stories(request):
    all_stories = Story.objects.all().order_by('date_of_publication')
    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_stories = all_stories.filter(title__icontains=search_form.cleaned_data['title_filed'])

    paginator = Paginator(all_stories, per_page=6)
    page_number = request.GET.get("page", 1)
    try:
        stories = paginator.page(page_number)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    context = {
        "all_stories": all_stories,
        "search_form": search_form,
        "stories": stories,
    }

    return render(request, template_name='story/all_stories.html', context=context)


class CreateStoryView(LoginRequiredMixin, CreateView):
    template_name = 'story/add_story.html'
    form_class = StoryForm
    success_url = reverse_lazy('all stories')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class DeleteStoryView(LoginRequiredMixin, DeleteView):
    model = Story
    template_name = 'story/delete_story.html'
    success_url = reverse_lazy('all stories')


@login_required
def edit_story(request, pk):
    story = Story.objects.get(pk=pk)
    form = EditStoryForm(instance=story)

    if request.method == "POST":
        form = EditStoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('details story', pk=pk)

    context = {
        "story": story,
        "form": form,
    }

    return render(request, 'story/edit_story.html', context)


def story_details(request, pk):
    story = Story.objects.get(pk=pk)

    context = {
        "story": story,
    }

    return render(request, 'story/details_story.html', context=context)
