from django.db import models

# Create your models here.

class Subscription(models.Model):
    STATUS = [
        ("unapproved","Unapproved"),
        ("approved", "Approved"),
        ("banned", "Banned")
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    status = models.CharField(max_length=15, choices=STATUS, default="unapproved")
    registerd_at = models.DateTimeField(auto_now_add=True)
    coffee_set = models.ManyToManyField("app_cof.Coffee")

    def __str__(self) -> str:
        return '{}(id={})'.format(self.title,self.id)
