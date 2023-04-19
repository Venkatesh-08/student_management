from django.db import models

# Create your models here.
from django.db import models

GRADE_CHOICES = (
    ('S', 'S'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
)

class Student(models.Model):
    #roll_number = models.CharField(max_length=50, unique=True)
    roll_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name, self.date_of_birth

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.student} - {self.grade}'


