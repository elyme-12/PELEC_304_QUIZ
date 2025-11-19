from django.db import models

class Student(models.Model):
    School_name = models.CharField(max_length=100)
    School_address = models.CharField(max_length=100)
    Honors = models.CharField(max_length=50)

    def __str__(self):
        return self.name