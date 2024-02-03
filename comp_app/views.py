from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Computer, Order, CustomUser
from . import forms
from .utils import calculate_total_price


class ComputerListView(ListView):
    model = Computer
    context_object_name = 'computer'
    template_name = 'comp_list.html'
    paginate_by = 10

class ComputerDetail(DetailView):
    model = Computer
    context_object_name = 'computer'
    template_name = 'comp_detail.html'

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class ComputerCreate(CreateView):
    model = Computer
    template_name = 'form.html'
    form_class = forms.ComputerForm
    success_url = '/comps/{id}'

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class ComputerUpdate(UpdateView):
    model = Computer
    fields = ['title', 'info', 'price', 'image']
    success_url = '/comps/{id}'
    template_name = 'form.html'

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class ComputerDelete(DeleteView):
    model = Computer
    template_name = 'form.html'
    success_url = '/comps/'

def MainPage(request):
    return render(request, 'main_page.html')



class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order_list.html'
    paginate_by = 10

class OrderDetail(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'order_detail.html'


@method_decorator(login_required, name='dispatch')
class OrderCreate(CreateView):
    model = Order
    template_name = 'form.html'
    form_class = forms.OrderForm
    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            form.instance.total_price = calculate_total_price(form.cleaned_data['products'], form.cleaned_data['quantity'])
            return super().form_valid(form)
        else:
            return HttpResponse("Вы должны войти в систему, чтобы создать заказ.")

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class OrderDelete(DeleteView):
    model = Order
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')



