from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = "menu"


class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"


class Drink(models.Model):
    korean_name  = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    description  = models.CharField(max_length=100)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "drinks"


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = "images"
    

class Allergy(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "allergies"

    
class Allergy_drink(models.Model):
    allergy_drink = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink         = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_drinks"
    

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=2)
    sodium_mg        = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat_g  = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_g         = models.DecimalField(max_digits=5, decimal_places=2)
    protein_g        = models.DecimalField(max_digits=5, decimal_places=2)
    caffeine_mg      = models.DecimalField(max_digits=5, decimal_places=2)
    size_ml          = models.CharField(max_length=50)
    size_fluid_ounce = models.CharField(max_length=50)
    drink            = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = "nutritions" 