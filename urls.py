from django.urls import path
from concrete import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('predict/', views.PredictView, name='predict'),
    #path('result/', views.ResultView, name='result'),
]
