import datetime

from django.db import models


class Person(models.Model):
    category = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()

    def age(self):
        return int((datetime.date.today() - self.birth_date).days / 365.25)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
