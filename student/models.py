from django.db import models

# Create your models here.


class stud(models.Model):
    studentName = models.CharField(max_length=20)
    Grade = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.studentName
