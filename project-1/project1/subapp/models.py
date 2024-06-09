from django.db import models
from django.utils import timezone


class ShoesVareity(models.Model):
    SHOES_TYPE_CHOICES = [
        ('SM','SMALL'),
        ('MD','MEDIUM'),
        ('LG','LARGE'),
        ('XL','EXTRA_LARGE')
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shoeImages/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=SHOES_TYPE_CHOICES,default='MD')
    description = models.TextField(default='')

    def __str__(self):
        return self.name