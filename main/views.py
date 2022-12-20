from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.views.generic.edit import CreateView, UpdateView


class PersonPageView(ListView):
    model = Person
    
class PersonView(DetailView):
    model = Person
    
    
    
class CreatePersonView(CreateView):
    model = Person
    template_name = 'main/person.html'
    fields = ["image", "name", "phone", "mail", "telegram", "slug", "body"]
    success_url = '/'
    
    
class UpdatePersonView(UpdateView):
    model = Person
    template_name = 'main/person.html'
    fields = ["image", "name", "phone", "mail", "telegram", "slug", "body"]
    success_url = '/'