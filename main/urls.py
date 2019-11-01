from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from main import views
from main import models

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='about.html'), name='about',),
    path('', TemplateView.as_view(template_name='index.html'), name='index',),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us',),
    path('products/<slug:tag>/', views.ProductList.as_view(), name='products',),
    path('product/<slug:slug>/', DetailView.as_view(model=models.Product), name='product'),
]