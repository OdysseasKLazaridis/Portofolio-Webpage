# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

class HomeView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add context to check if there's a challenge for today
        context['message'] = "This is a messsage"  # True if there's a challenge, False if not
        return context