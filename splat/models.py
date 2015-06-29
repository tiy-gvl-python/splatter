from django.db import models

# Create your models here.

class Splat(models.Model):
    message = models.CharField(max_length=141)

    def __str__(self):
        return self.message
