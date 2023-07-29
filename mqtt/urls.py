from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('details/<int:id>', views.details, name="details"),
    path('api/device_list/', views.device_list, name="device_list"),
    path('api/device_detail/<int:id>', views.device_detail, name='device_detail'),
    path('deltaTEMP/', views.deltaTEMP, name='deltaTEMP'),
]