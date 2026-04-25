from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path(
        'password/change/',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url='/accounts/profile/',
        ),
        name='password_change',
    ),
]
