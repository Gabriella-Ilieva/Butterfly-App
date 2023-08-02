from profile import Profile

from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.templatetags.static import static
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from butterfly.accounts.forms import RegisterUserForm, LogInForm, EditUserForm
from butterfly.initiatives.models import Initiative, Participation
from butterfly.stories.models import Story

UserModel = get_user_model()


# class OnlyAnonymousMixin:
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponse(self.get_success_url())
#
#         return super().dispatch(request, *args, **kwargs)


class RegisterUserView(views.CreateView):
    template_name = 'profile/register_profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('all initiatives')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['next'] = self.request.GET.get('next', '')
    #
    #     return context

    # def get_success_url(self):
    #
    #     return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    form_class = LogInForm
    template_name = 'profile/login.html'
    success_url = reverse_lazy('index')


def user_stories(request):
    all_stories = Story.objects.filter(user=request.user).order_by('date_of_publication')
    paginator = Paginator(all_stories, per_page=9)
    page_number = request.GET.get("page", 1)
    try:
        stories = paginator.page(page_number)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    context = {
        "stories": stories,
    }
    return render(request, 'profile/user_stories.html', context)


def user_initiatives(request):
    initiatives_list = Initiative.objects.filter(user=request.user).order_by('date_of_publication')
    paginator = Paginator(initiatives_list, per_page=9)
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
    return render(request, 'profile/user_initiatives.html', context)


def user_participations(request):
    participations_list = Participation.objects.filter(user=request.user).order_by('to_initiative__date_of_publication')

    paginator = Paginator(participations_list, per_page=9)
    page_number = request.GET.get("page", 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        "page_obj": page_obj,
    }
    return render(request, 'profile/user_participations.html', context)


class LogoutUserView(auth_views.LogoutView):
    success_url = reverse_lazy('index')


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/edit_profile.html'
    model = UserModel
    form_class = EditUserForm
    success_url = reverse_lazy('index')


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('index')
