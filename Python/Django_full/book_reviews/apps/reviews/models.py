from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=40)
  alias=models.CharField(max_length=40)
  email=models.CharField(max_length=40)
  password=models.CharField(max_length=400)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

class Book(models.Model):
  name=models.CharField(max_length=40)
  author=models.CharField(max_length=40)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  
class Review(models.Model):
  rating=models.IntegerField()
  book=models.ForeignKey(Book, related_name='book_reviews')
  description=models.CharField(max_length=1000)
  poster=models.ForeignKey(User, related_name='user_reviews')
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)