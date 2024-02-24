from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('cheap/', views.CheapComputerListView.as_view(), name='CheapComp'),
    path('avg/', views.AverageComputerListView.as_view(), name='AvgComp'),
    path('exp/', views.ExpensiveComputerListView.as_view(), name='ExpComp'),
    path('<int:pk>/', views.ComputerDetail.as_view(), name='CompDetail'),
    path('create/', views.ComputerCreate.as_view(), name='CompCreate'),
    path('update/<int:pk>', views.ComputerUpdate.as_view(), name='CompUpdate'),
    path('delete/<int:pk>', views.ComputerDelete.as_view(), name='CompDelete'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]

