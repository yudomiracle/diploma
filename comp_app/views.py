from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Computer, CustomUser, Cart
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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        if request.user.is_staff:
            cart_item = Cart(user=None, product_id=product_id)
        else:
            cart_item = Cart(user=request.user, product_id=product_id)
        cart_item.save()
        return redirect('cart')

@login_required
def cart(request):
    if request.user.is_staff:
        cart_items = Cart.objects.all()
    else:
        cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')



