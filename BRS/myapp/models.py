from django.db import models

class playerdata(models.Model):
    Name = models.CharField(max_length=50)
    Rating  = models.IntegerField(default=1000)
    G_played= models.IntegerField(default=0)
    G_won= models.IntegerField(default=0)
    G_lost= models.IntegerField(default=0)
    
    
    class Meta:
        ordering = ['-Rating']
    