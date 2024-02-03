from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ComputerListView.as_view(), name='CompList'),
    path('<int:pk>/', views.ComputerDetail.as_view(), name='CompDetail'),
    path('create/', views.ComputerCreate.as_view(), name='CompCreate'),
    path('update/<int:pk>', views.ComputerUpdate.as_view(), name='CompUpdate'),
    path('delete/<int:pk>', views.ComputerDelete.as_view(), name='CompDelete'),

    path('orders/', views.OrderList.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreate.as_view(), name='order_create'),
    path('orders/delete/<int:pk>', views.OrderDelete.as_view(), name='order_delete')
]

