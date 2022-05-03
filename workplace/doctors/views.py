from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .models import Doctors


class DoctorsView(ListView):
    model = Doctors
    template_name = "doctors.html"
    context_object_name = 'doctors'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'menu'
        context['test'] = 'test'
        return context


class HomeView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, object_list=None, **kwargs):
        lst = [1, 2, 3, 5]
        context = super().get_context_data(**kwargs)
        context['title'] = 'Workplace for doctors'
        context['work'] = 'Workplaces'
        context['list'] = lst
        return context
