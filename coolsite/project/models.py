from django.db import models

# Create your models here.
class Training1(models.Model):
    title = models.CharField(max_length=255)
    time = models.TextField()
    place = models.TextField()
    training_manager = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")

class Training2(models.Model):
        title = models.CharField(max_length=255)
        time = models.TextField()
        place = models.TextField()
        training_manager = models.CharField(max_length=255)
        photo = models.ImageField(upload_to="photos/%y/%m/%d/")


class Books_self_development(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")

class Books_psychology(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")


class Training_manager1(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    speciality = models.TextField()
    number = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")


class Training_manager2(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    speciality = models.TextField()
    number = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")


class Motivation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.TextField(blank=True)




