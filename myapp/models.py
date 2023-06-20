from django.db import models
import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
# Import vestavěného modulu os, který obsahuje různé utility pro práci s daným OS
import os



class Difficulty(models.Model):
    name = models.CharField(max_length=50, unique=True,verbose_name='Difficulty',help_text='Difficulty')

    class Meta:
        verbose_name = 'difficulty'
        verbose_name_plural = 'difficulty'
        ordering = ['name']
    def __str__(self):
        return self.name

class Body_part(models.Model):
    body_part = models.CharField(max_length=50, unique=True,verbose_name='body part',help_text='body part',default='Full body')
    class Meta:
        verbose_name = 'body_part'
        verbose_name_plural = 'body_parts'
        ordering = ['body_part']

    def __str__(self):
        return self.body_part

class Equipment(models.Model):
    equipment = models.CharField(max_length=50, unique=True,verbose_name='body part',help_text='body part')
    class Meta:
        verbose_name = 'equipment'
        verbose_name_plural = 'equipments'
        ordering = ['equipment']

    def __str__(self):
        return self.equipment

class Exercise(models.Model):
    name = models.CharField(max_length=50, unique=True,verbose_name='Exercise',help_text='Exercise')
    poster = models.ImageField(
        upload_to='posters',
        blank=True,
        null=True,
        verbose_name='Plakát ',
        help_text='grafický soubor')
    difficulties = models.ManyToManyField(
        Difficulty,
        verbose_name='difficulties')
    equipments = models.ManyToManyField(Equipment)
    obsah = models.TextField(blank=True, verbose_name='obsah', help_text='obsah')
    body_parts = models.ManyToManyField(Body_part)
    class Meta:
        verbose_name = 'exercise'
        verbose_name_plural = 'exercises'
        ordering = ['name']
    def __str__(self):
        return self.name

# Create your models here.
