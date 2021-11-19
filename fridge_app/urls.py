from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.FridgeList.as_view(), name='fridge_list'),
    path('fridges/', views.FridgeList.as_view(), name='fridge_list'),
    path('fridges/<int:pk>', views.FridgeDetail.as_view(), name='fridge_detail'),
]