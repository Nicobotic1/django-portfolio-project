from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name = 'index'),
    path('students/', views.StudentListView.as_view(), name = 'student-list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
]