from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to="recipe")
