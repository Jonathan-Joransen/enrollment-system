# A Django-based school enrollment system that ensures enrollments are only valid on specific days the course meets

## Feature

- Enrollments are only valid on the specific days the course meets.
- Validation ensures that enrollment dates fall on course meeting days.

## Models

### Course
- `name`: Name of the course
- `meeting_days`: List of days the course meets (e.g., ["Monday", "Wednesday", "Friday"])

### Student
- `first_name`: Student's first name
- `last_name`: Student's last name
- `email`: Student's email address (unique)

### Enrollment
- `student`: The student who is enrolling
- `course`: The course being enrolled in
- `enrollment_date`: The specific date of enrollment

## Validation

The Enrollment model includes validation that checks if the enrollment date falls on a meeting day for the course. If not, a validation error is raised.

## Tests

Comprehensive tests covering valid and invalid enrollment dates, multiple enrollments, etc.
