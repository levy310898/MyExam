from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)


class Exam(models.Model):
    key = models.ForeignKey( User ,on_delete = models.CASCADE)

class Question(models.Model):
    key = models.ForeignKey(Exam, on_delete= models.CASCADE)

class Answer(models.Model):
    key = models.ForeignKey(Exam, on_delete= models.CASCADE)

class Point(models.Model):
    key1 = models.ForeignKey(User, on_delete = models.CASCADE)
    key2 = models.ForeignKey(Exam, on_delete= models.CASCADE)