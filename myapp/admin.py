from django.contrib import admin

from .models import Body_part ,Equipment, Difficulty ,Exercise
# Register your models here.
admin.site.register(Difficulty)
admin.site.register(Body_part)
admin.site.register(Equipment)
admin.site.register(Exercise)