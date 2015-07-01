from django.contrib import admin

from splat.models import Splat, Painting, PaintingStyle, Splatee

# Register your models here.

admin.site.register(Splat)
admin.site.register(Splatee)
admin.site.register(Painting)
admin.site.register(PaintingStyle)
