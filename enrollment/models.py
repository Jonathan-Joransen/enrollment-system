from django.db import models
from django.core.exceptions import ValidationError


class Course(models.Model):
    """A course that students can enroll in."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    # Meeting days as a JSON field storing a list of day names (e.g., ["Monday", "Wednesday", "Friday"])
    meeting_days = models.JSONField(
        default=list,
        help_text="List of days the course meets (e.g., ['Monday', 'Wednesday', 'Friday'])"
    )
    
    def clean(self):
        """Validate meeting days."""
        if not isinstance(self.meeting_days, list):
            raise ValidationError({"meeting_days": "Meeting days must be a list."})
        if not all(isinstance(day, str) for day in self.meeting_days):
            raise ValidationError({"meeting_days": "All meeting days must be strings."})
    
    def __str__(self):
        return self.name


class Enrollment(models.Model):
    """A student's enrollment in a course on a specific date."""
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'course', 'enrollment_date']
    
    def clean(self):
        """Validate that the enrollment date is on a meeting day for the course."""
        super().clean()
        day_name = self.enrollment_date.strftime("%A")
        if day_name not in self.course.meeting_days:
            raise ValidationError({
                "enrollment_date": f"Course does not meet on {day_name}. Valid days: {', '.join(self.course.meeting_days)}"
            })
    
    def __str__(self):
        return f"{self.student} in {self.course} on {self.enrollment_date}"


class Student(models.Model):
    """A student in the system."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
