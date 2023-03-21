from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.ListCreateTodoView.as_view(), name='todo_list'),
    path('todos/<int:pk>/', views.RetrieveUpdateDestroyTodoView.as_view(), name='todo_detail'),
]
