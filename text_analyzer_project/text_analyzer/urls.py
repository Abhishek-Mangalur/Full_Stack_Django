from django.urls import path
from .views import analyze_text

urlpatterns = [
    path('<str:input_text>/', analyze_text, name='analyze_text'),
]
