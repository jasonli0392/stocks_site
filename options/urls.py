from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('options_calculator/', views.options_calculator, name='options_calculator'),
]