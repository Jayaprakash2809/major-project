from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mblenum=models.BigIntegerField()
    email=models.EmailField(max_length=400)
    gender=models.CharField(max_length=200)
class SendmailModel(models.Model):
    sendermail=models.EmailField(max_length=50)
    to=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    chat=models.CharField(max_length=200)
    spam=models.CharField(max_length=200)
    category=models.CharField(max_length=100)

class FeedbackModel(models.Model):
    username = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=300)