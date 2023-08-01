from django.urls import path, include
from butterfly.accounts import views
from butterfly.accounts.views import ProfileEditView, ProfileDeleteView, user_stories, user_initiatives

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
        path('stories/', user_stories, name='user stories'),
        path('initiatives/', user_initiatives, name='user initiatives'),
    ]))
]
