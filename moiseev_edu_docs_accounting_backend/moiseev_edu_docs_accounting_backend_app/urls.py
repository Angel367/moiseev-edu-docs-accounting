from django.urls import path, include
from .views import *

urlpatterns = [
    path('student/create/', student_create, name='student_create'),
    path('student/list/', student_list, name='student_list'),
    path('student/detail/<int:pk>/', student_detail, name='student_detail'),
    path('student/delete/<int:pk>/', student_delete, name='student_delete'),
    path('teacher/create/', teacher_create, name='teacher_create'),
    path('teacher/list/', teacher_list, name='teacher_list'),
    path('teacher/detail/<int:pk>/', teacher_detail, name='teacher_detail'),
    path('teacher/delete/<int:pk>/', teacher_delete, name='teacher_delete'),
    path('document/create/', document_create, name='document_create'),
    path('document/list/', document_list, name='document_list'),
    path('document/detail/<int:pk>/', document_detail, name='document_detail'),
    path('document/delete/<int:pk>/', document_delete, name='document_delete'),
]
