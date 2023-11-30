from django.db import models

# Create your models here.

class Coffee(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    special_price = models.IntegerField(null=True, blank=True)
    is_premium = models.BooleanField(null=True)
    promotion_end_at = models.DateTimeField(null=True, blank=True)
    description =models.TextField(null=True, blank=True)
    image = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return '{}(id={})'.format(self.title,self.id)
    

