from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete = models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    korean_name  = models.CharField(max_length=20)
    english_name = models.CharField(max_length=50)
    description  = models.CharField(max_length=120)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Image(models.Model):
    image_url = models.CharField(max_length=300)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'allergies'

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergies_drinks'

class Size(models.Model):
    name             = models.CharField(max_length=20)
    size_ml          = models.CharField(max_length=20, null=True)
    size_fluid_ounce = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'sizes'

class Nutrition(models.Model):
    one_serving_kal = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'