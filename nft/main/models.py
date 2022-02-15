from django.db import models


class Cards(models.Model):
    title = models.CharField(max_length=70)
    photo = models.ImageField(upload_to="arts/")
    series = models.CharField(max_length=30)
    attribute = models.CharField(max_length=30)
    spectacular = models.CharField(max_length=30)
    token_frame = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.title
