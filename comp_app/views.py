from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
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

@login_required
def order_list(request):
    user_instance = request.user
    custom_user_instance = None

    if isinstance(user_instance, CustomUser):
        custom_user_instance = user_instance
    else:
        try:
            custom_user_instance = CustomUser.objects.get(pk=user_instance.pk)
        except CustomUser.DoesNotExist:
            pass

    if custom_user_instance:
        print(f"User type: {type(custom_user_instance)}")
        user_id = getattr(custom_user_instance, 'id', None)
        print(f"User ID: {user_id}")

        orders = Order.objects.filter(user=custom_user_instance)
        return render(request, 'order_list.html', {'orders': orders})

    error_message = 'Invalid user type'
    print(error_message)
    return render(request, 'error_page.html', {'error_message': error_message}, status=403)

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})


@login_required
def create_order(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)

        if form.is_valid():
            selected_products = form.cleaned_data['products']
            quantity = form.cleaned_data['quantity']

            order = Order.objects.create(
                user=request.user,
                quantity=quantity,
                total_price=0,
            )

            order.products.set(selected_products)

            return redirect('order_detail', pk=order.pk)
    else:
        form = forms.OrderForm()

    return render(request, 'form.html', {'form': form})
