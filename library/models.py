from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.user.first_name} [{self.enrollment}]"

    @property
    def get_name(self):
        return self.user.first_name

    @property
    def get_user_id(self):
        return self.user.id

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    average_rating = models.FloatField(default=0.0)
    isbn = models.PositiveIntegerField(default=0)
    Number_of_Pages = models.PositiveIntegerField(default=0)
    Ratings_Count = models.PositiveIntegerField(default=0)
    Text_Reviews_Count = models.PositiveIntegerField(default=0)
    publisher = models.CharField(max_length=100)
    Publication_Date = models.DateField()  # Changed to DateField for publication date
    Language_Code = models.CharField(max_length=10)
    isbn13 = models.PositiveIntegerField(default=0)
    Book_ID = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

def get_expiry():
    return datetime.today() + timedelta(days=5)

class IssuedBook(models.Model):
    enrollment = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default=get_expiry)  # Use get_expiry directly

    def __str__(self):
        return self.enrollment

