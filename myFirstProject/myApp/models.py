from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    studentID = models.CharField(max_length=20)  # Unique ID for each student
    age = models.IntegerField()

    def __str__(self):
        return self.name
