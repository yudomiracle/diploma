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

    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/create/', views.create_order, name='create_order'),
]

