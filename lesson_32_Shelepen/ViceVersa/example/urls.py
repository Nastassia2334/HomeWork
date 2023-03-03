from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('reverse/', views.reverse, name='reverse')
]

