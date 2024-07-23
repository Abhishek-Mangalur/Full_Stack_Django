from django.urls import path
from .views import find_mode

urlpatterns = [
    path('<str:num_list>/', find_mode, name='find_mode'),
]
