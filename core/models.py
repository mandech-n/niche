from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField

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


CATEGORY_CHOICES = (
    ('SS', 'Special Situations'),
    ('ED', 'Education'),
    ('PH', 'Public Health'),
    ('ST', 'Sanitary'),
    ('SP', 'Sports')
)

LABEL_CHOICES = (
    ('NW', 'new'),
    ('OG', 'sale'),
)

class Item_Detail_View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    item = models.ForeignKey(
        'Item', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default = 0)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    donation_amount = models.FloatField()
    #view_count = models.IntegerField(default = 0)
    thumbnail = models.ImageField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2, blank=True, null=True)
    featured = models.BooleanField(blank=True, null=True)
    content = RichTextUploadingField(blank=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:item_detail', kwargs={'id': self.id})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return Item_Detail_View.objects.filter(item=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(item=self).count()

    def get_update_url(self):
        return reverse('item_detail_update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('item_detail_delete', kwargs={
            'id': self.id
        })









