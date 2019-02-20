from django.conf import settings
from django.db import models
from django.utils import timezone


class Taste(models.Model):
    taster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    brewery = models.CharField(max_length=200)
    beer_name = models.CharField(max_length=200)
    beer_type = models.CharField(max_length=200)
    abv = models.FloatField()
    purchased_location = models.CharField(max_length=200)
    RATING_CHOICES = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        (6, 'Six'),
    )
    rating = models.IntegerField(default=3, choices=RATING_CHOICES)
    tasting_notes = models.TextField()
    tasted_date = models.DateTimeField(default=timezone.now)
    # img_file = models.FileField(upload_to='media/rateBeer/img', null=True)


    def publish(self):
        self.tested_date = timezone.now()
        self.save()

    def __str__(self):
        return self.brewery + " " + self.beer_name