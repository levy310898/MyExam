from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    day = models.DecimalField(max_digits= 2, decimal_places= 0)
    month = models.DecimalField(max_digits= 2, decimal_places= 0)
    year = models.DecimalField(max_digits= 4, decimal_places= 0)
    phoneNumber = models.CharField(max_length= 10)
    email = models.EmailField()
    sex = models.BooleanField()
    address = models.CharField(max_length= 200)

class Exam(models.Model):
    key = models.ForeignKey( User ,on_delete = models.CASCADE)
    examName = models.CharField(max_length= 200)

class Question(models.Model):
    key = models.ForeignKey(Exam, on_delete= models.CASCADE)
    question = models.TextField()

class Answer(models.Model):
    key = models.ForeignKey(Exam, on_delete= models.CASCADE)
    answer = models.TextField()
    isCorrect = models.BooleanField()

class Point(models.Model):
    key1 = models.ForeignKey(User, on_delete = models.CASCADE)
    key2 = models.ForeignKey(Exam, on_delete= models.CASCADE)
    point = models.DecimalField(max_digits= 2, decimal_places= 0)