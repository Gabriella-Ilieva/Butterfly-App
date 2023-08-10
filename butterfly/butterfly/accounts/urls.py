from django.urls import path, include
from butterfly.accounts import views
from butterfly.accounts.views import ProfileEditView, ProfileDeleteView, user_stories, user_initiatives, \
    user_participations

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('change_password_done/', views.ChangePasswordDoneView.as_view(), name='change password done'),
    path('profile/<int:pk>/', include([
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
        path('change_password/', views.ChangePasswordView.as_view(), name='change password'),
    ])),
    path('my-stories/', user_stories, name='user stories'),
    path('my-initiatives/', user_initiatives, name='user initiatives'),
    path('my-participations/', user_participations, name='user participations'),
]
