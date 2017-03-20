from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
  name= models.CharField(max_length=40)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)



class Description(models.Model):
  desc = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  course=models.OneToOneField(Course, related_name='descriptions')

class Comment(models.Model):
  comment = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  course=models.ForeignKey(Course, related_name='comments')

  #install db browser