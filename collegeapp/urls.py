from django.urls import path
from .views import register_college, sign_in, register_user
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='sign_in/', permanent=False), name='home'),  # Redirect root URL to sign-in
    path('register/', register_college, name='register_college'),  # URL for college registration
    path('sign_in/', sign_in, name='sign_in'),                      # URL for signing in
    path('register_user/', register_user, name='register_user'),    # URL for user registration
]
