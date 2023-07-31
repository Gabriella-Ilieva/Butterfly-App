from profile import Profile

from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.templatetags.static import static
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from butterfly.accounts.forms import RegisterUserForm, LogInForm, EditUserForm

UserModel = get_user_model()


class OnlyAnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(OnlyAnonymousMixin, views.CreateView):
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


# class ProfileDetailsView(views.DetailView):
#     template_name = 'profile/details_profile.html'
#     model = UserModel
#
#     profile_image = static('images/pic_butterfly.png')

    # def get_profile_image(self):
    #     if self.object.profile_picture is not None:
    #         return self.object.profile_picture
    #     return self.profile_image
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['profile_image'] = self.get_profile_image()
    #     # context['pets'] = self.request.user.pet_set.all()
    #
    #     return context


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/edit_profile.html'
    model = UserModel
    form_class = EditUserForm
    success_url = reverse_lazy('index')


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('index')
