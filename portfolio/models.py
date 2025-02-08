from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    cgpa = models.CharField(max_length=10)

    def __str__(self):
        return self.degree
    
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Certification(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name