from django.contrib import admin
from django.urls import path, include
from pages.views import (
    HomeView, AboutView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('payment/', include('payment.urls')),

    # provide the links for basic pages
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),

]
