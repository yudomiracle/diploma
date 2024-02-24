from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Computer, Order, CustomUser
from . import forms
from .utils import calculate_total_price


class CheapComputerListView(ListView):
    model = Computer
    template_name = 'comp_list.html'
    context_object_name = 'computers'
    paginate_by = 20

    def get_queryset(self):
        return Computer.objects.filter(price__lt=500)

class AverageComputerListView(ListView):
    model = Computer
    template_name = 'comp_list.html'
    context_object_name = 'computers'
    paginate_by = 20

    def get_queryset(self):
        return Computer.objects.filter(price__range=[500, 1000])

class ExpensiveComputerListView(ListView):
    model = Computer
    template_name = 'comp_list.html'
    context_object_name = 'computers'
    paginate_by = 20

    def get_queryset(self):
        return Computer.objects.filter(price__gt=1000)



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


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetail(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'order_detail.html'


from django.shortcuts import redirect


class OrderCreate(CreateView):
    model = Order
    template_name = 'form.html'
    form_class = forms.OrderForm

    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            products = form.cleaned_data['products']
            quantity = form.cleaned_data['quantity']
            total_price = calculate_total_price(products, [quantity])
            form.instance.total_price = total_price
            return super().form_valid(form)
        else:
            return redirect('user_login')

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class OrderDelete(DeleteView):
    model = Order
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')



