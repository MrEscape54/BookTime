from django.urls import path
from django.views.generic import TemplateView
from main import views
from main import models

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='about.html'), name='about',),
    path('', TemplateView.as_view(template_name='index.html'), name='index',),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us',),
    path('products/<slug:tag>/', views.ListView.as_view(model=models.Product), name='products',),
]