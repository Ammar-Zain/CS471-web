from django.db import models
class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField(default=18)
    address = models.ForeignKey('address', on_delete=models.RESTRICT)

class address(models.Model):
    address = models.CharField(max_length=20)