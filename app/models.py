from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    DUTSE = 'dutse'
    BIRNINKUDU = 'bkd'
    HADEJIA = 'hadejia'
    RINGIM = 'ringim'
    GUMEL = 'gumel'
    KAZAURE = 'kazaure'
    
    LGA = [
       (DUTSE, ('DUTSE')),
       (BIRNINKUDU, ('BIRNINKUDU')),
       (HADEJIA, ('HADEJIA')),
       (RINGIM, ('RINGIM')),
       (GUMEL, ('GUMEL')),
       (KAZAURE, ('KAZAURE')),
   ]
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    crime_title = models.CharField(max_length=100, blank=True, null=True)
    crime_description = models.TextField(max_length=300, blank=True, null=True)
    crime_location = models.CharField(max_length=100, default='Jigawa', blank=True, null=True)
    lga = models.CharField(
       max_length=32,
       choices=LGA,
       default=DUTSE, blank=True, null=True
   )
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True, null=True)
    street_address = models.CharField(max_length = 255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    treated = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.crime_title

    class Meta:
        ordering = ['-id']
    