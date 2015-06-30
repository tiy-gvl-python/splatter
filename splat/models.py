from django.db import models

# Create your models here.


class PaintingStyle(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Painting(models.Model):
    style = models.ForeignKey(PaintingStyle)
    medium = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.style.description, self.medium)


class Splat(models.Model):
    message = models.CharField(max_length=141)
    painting = models.ForeignKey(Painting, null=True)
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    val3 = models.IntegerField()

    def __str__(self):
        return self.message

    @property
    def average_value(self):
        return (self.val1 + self.val2 + self.val3) / 3

    @property
    def has_painting(self):
        return bool(self.painting)
