from django.urls import path
from todoapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('todo/', views.TodoList.as_view()),
]
