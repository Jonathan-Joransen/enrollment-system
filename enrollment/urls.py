from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='enrollment_index'),
    path('courses/', views.courses, name='enrollment_courses'),
    path('students/', views.students, name='enrollment_students'),
    path('enrollments/', views.enrollments, name='enrollment_enrollments'),
]
