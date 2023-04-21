from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
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

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")
    category = models.ForeignKey('Category',on_delete=models.PROTECT)
    user = models.ForeignKey(User,verbose_name='Пользователь',on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


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

def str(self):
        return self.title
def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


