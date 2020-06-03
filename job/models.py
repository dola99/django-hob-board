from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full time'),
    ('Part Time','Part Time'),
)

class Job(models.Model):
    
    title = models.CharField(max_length = 100)
    job_type = models.CharField(max_length = 15, choices=JOB_TYPE) 
    descrption = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacany = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    exprience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category (models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name