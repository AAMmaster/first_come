from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import RecipeForm
from .models import Resipe


class RecipeListView(ListView):
    model = Resipe
    template_name = 'home.html'
    context_object_name = 'resipes'


class RecipeCreateView(CreateView):
    model = Resipe
    form_class = RecipeForm
    template_name = 'createresipe.html'
    success_url = reverse_lazy('home')


class RecipeUpdateView(UpdateView):
    model = Resipe
    form_class = RecipeForm
    template_name = 'edit.html'
    context_object_name = 'resipes'
    success_url = reverse_lazy('home')


class RecipeDeleteView(DeleteView):
    model = Resipe
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return redirect('home')
