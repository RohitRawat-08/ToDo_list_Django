from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)


class DeleteModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

class CompleteModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)