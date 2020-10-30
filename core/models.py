from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

class Interest(models.Model):
    category  = models.TextField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    school = models.TextField()
    form  = models.TextField()
    interests = models.ManyToManyField(Interest, related_name='interested_students')

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    school = models.TextField()
    form  = models.TextField()
    role = models.TextField()
    interests = models.ManyToManyField(Interest, related_name='interested_teachers')

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    organization = models.TextField()
    interests = models.ManyToManyField(Interest, related_name='interested_donors')

class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    organization = models.TextField()
    interests = models.ManyToManyField(Interest, related_name='interested_partners')

class Public(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
