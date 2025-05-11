from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    game_id = models.CharField(max_length=255, default='TEMP')
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, default='BRL')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
