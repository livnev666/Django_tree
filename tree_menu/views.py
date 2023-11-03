from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import *

# Create your views here.


class IndexView(TemplateView):

    template_name = "tree_menu/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Tree_Menu.objects.filter(slug='main_menu').first()
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response
