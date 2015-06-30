from django.contrib import admin

from splat.models import Splat, Painting, PaintingStyle

# Register your models here.

admin.site.register(Splat)
admin.site.register(Painting)
admin.site.register(PaintingStyle)
