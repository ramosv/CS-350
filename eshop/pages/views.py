from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='home.html'

class IndexPage(TemplateView):
    template_name='index.html'

class ProfilePage(TemplateView):
    template_name='profile.html'
    
class CheckOutPage(TemplateView):
    template_name='checkout.html'

class SigninPage(TemplateView):
    template_name='signin.html'

class ProductPage(TemplateView):
    template_name='Product.html'
