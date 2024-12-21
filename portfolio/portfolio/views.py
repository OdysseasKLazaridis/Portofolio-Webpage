# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

class HomeView(TemplateView):
    template_name = "index/index.html"
    
class Works(TemplateView):
    template_name = "works.html"

class About(TemplateView):
    template_name = "about.html"

class Contact(TemplateView):
    template_name = "contact.html"