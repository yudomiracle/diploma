from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'drf_comp'
router = DefaultRouter()
router.register('comps', views.CompViewSet)

urlpatterns = router.urls