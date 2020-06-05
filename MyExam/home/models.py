from django.db import models


# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length = 200, default= "")
    password = models.CharField(max_length = 200, default= "")
    name = models.CharField(max_length = 200, default= "")
    day = models.DecimalField(max_digits= 2, decimal_places= 0, default= 0)
    month = models.DecimalField(max_digits= 2, decimal_places= 0, default= 0)
    year = models.DecimalField(max_digits= 4, decimal_places= 0, default= 0)
    phoneNumber = models.CharField(max_length= 10, default= "")
    email = models.EmailField(default= "")
    sex = models.BooleanField(default= False)
    address = models.CharField(max_length= 200, default= "")

class Exam(models.Model):
    key = models.ForeignKey( User ,on_delete = models.CASCADE)
    examName = models.CharField(max_length= 200, default= "")

class Question(models.Model):
    key = models.ForeignKey(Exam, on_delete= models.CASCADE)
    question = models.TextField(default= "")

class Answer(models.Model):
    key = models.ForeignKey(Exam, on_delete= models.CASCADE)
    answer = models.TextField(default= "")
    isCorrect = models.BooleanField(default= False)

class Point(models.Model):
    key1 = models.ForeignKey(User, on_delete = models.CASCADE)
    key2 = models.ForeignKey(Exam, on_delete= models.CASCADE)
    point = models.DecimalField(max_digits= 2, decimal_places= 0, default= 0)