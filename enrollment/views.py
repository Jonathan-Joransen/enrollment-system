from django.shortcuts import render
from .models import Course, Enrollment, Student


def index(request):
    """Enrollment system dashboard."""
    courses_count = Course.objects.count()
    students_count = Student.objects.count()
    enrollments_count = Enrollment.objects.count()
    
    context = {
        'courses_count': courses_count,
        'students_count': students_count,
        'enrollments_count': enrollments_count,
    }
    return render(request, 'enrollment/index.html', context)


def courses(request):
    courses = Course.objects.all()
    return render(request, 'enrollment/courses.html', {'courses': courses})


def students(request):
    students = Student.objects.all()
    return render(request, 'enrollment/students.html', {'students': students})


def enrollments(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment/enrollments.html', {'enrollments': enrollments})
