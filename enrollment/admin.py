from django.contrib import admin
from .models import Course, Enrollment, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "meeting_days"]
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
    

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["student", "course", "enrollment_date", "created_at"]
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = Student.objects.all()
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
