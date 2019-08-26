from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField(default=18)
    date_birth=models.DateTimeField()

    def __str__(self):
        return self.first_name


class degree(models.Model):
    student_id=models.ForeignKey(student, on_delete=models.CASCADE)
    student_degree=models.IntegerField(default=15)

    def __str__(self):
        return self.student_degree