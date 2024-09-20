from django.urls import path
from .views import MyLoginView, ProfileView, MyLogoutView, RegistrationView


urlpatterns = [

    path('login', MyLoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('logout', MyLogoutView.as_view(), name='logout'),
    path('registration', RegistrationView.as_view(), name='register'),

]
