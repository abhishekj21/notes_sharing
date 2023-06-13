from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.CharField(max_length=10,null=True)
    def _str_(self):
        return self.user.username

class Questions(models.Model):
    que=models.CharField(max_length=300,null=True)
    topic=models.CharField(max_length=100,null=True)
    ans = models.CharField(max_length=500,null=True)
    user = models.CharField(max_length=50,null=True)
    atopic = models.CharField(max_length=100,null=True)
    h = models.IntegerField(max_length=200,null=True)
    nh = models.IntegerField(max_length=200,null=True)

class Feedback(models.Model):
    feedback_name = models.CharField(max_length=20,null=True)
    feedback_contact = models.CharField(max_length=30, null=True)
    feedback_email = models.CharField(max_length=10,null=True)
    feedback_comment = models.CharField(max_length=15,null=True)


class Helpful(models.Model):
    num = models.IntegerField(max_length=200,null=True)
    num2 = models.IntegerField(max_length=200,null=True)
    numid = models.IntegerField(max_length=200,null=True)

class Blog(models.Model):
    user = models.CharField(max_length=200,null=True)
    topic = models.CharField(max_length=200,null=True)
    blogc = models.CharField(max_length=200,null=True)
