from django.db import models
from countries.models import Country, City

# Create your models here.
class TourPackage(models.Model):
    title = models.CharField(max_length=250)
    source_country = models.ForeignKey(Country, related_name='source_country', on_delete=models.CASCADE)
    source_city = models.ForeignKey(City, related_name='source_city', on_delete=models.CASCADE)
    destination_country = models.ForeignKey(Country, related_name='dest_country', on_delete=models.CASCADE)
    destination_city = models.ForeignKey(City, related_name='dest_city', on_delete=models.CASCADE)
    description = models.TextField()
    terms = models.TextField()
    photos = models.ImageField(upload_to='packages/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Schedule(models.Model):
    title = models.CharField(max_length=255)
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='schedules')
    from_date = models.DateField()
    to_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    schedule_photos = models.ImageField(upload_to='schedules/')