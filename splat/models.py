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
    splatee = models.ForeignKey("Splatee")

    def __str__(self):
        return "{} - {}".format(self.message, self.painting)

    @property
    def has_painting(self):
        return bool(self.painting)


class Splatee(models.Model):
    sex = models.CharField(max_length=1)
    occupation = models.IntegerField()
    postal_code = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.age, self.sex)
