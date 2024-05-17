from django.db import models

# Create your models here.
class PrimesData(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    start=models.IntegerField()
    end=models.IntegerField()
    algorithm=models.CharField(max_length=100)
    count=models.IntegerField()
    time_elapsed=models.FloatField()
    primes = models.TextField()

    def __str__(self):
        return self.timestamp