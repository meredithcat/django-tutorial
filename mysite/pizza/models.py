from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "Making a change"

class Pizza(models.Model):
    name = models.CharField(max_length=20)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return "I am a pizza"

# making some more changes
