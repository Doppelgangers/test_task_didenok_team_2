from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchPasswordView.as_view()),
    path('<str:service_name>/', views.PasswordView.as_view()),

]
