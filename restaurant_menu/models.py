from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
)

STATUS= (
    (0, 'unavailable'),
    (1, 'available'),
)

class Item(models.Model):
    meal = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15,decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.BooleanField(choices=STATUS,default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal