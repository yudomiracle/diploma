from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Computer
from . import forms

class ComputerListView(ListView):
    model = Computer
    context_object_name = 'computer'
    template_name = 'comp_list.html'
    paginate_by = 10

class ComputerDetail(DetailView):
    model = Computer
    context_object_name = 'computer'
    template_name = 'comp_detail.html'

class ComputerCreate(CreateView):
    model = Computer
    template_name = 'form.html'
    form_class = forms.ComputerForm
    success_url = '/comps/{id}'

class ComputerUpdate(UpdateView):
    model = Computer
    fields = ['title', 'info', 'price', 'image']
    success_url = '/comps/{id}'
    template_name = 'form.html'

class ComputerDelete(DeleteView):
    model = Computer
    template_name = 'form.html'
    success_url = '/comps/'

def MainPage(request):
    return render(request, 'main_page.html')