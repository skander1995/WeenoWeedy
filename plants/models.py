from django.db import models
from datetime import datetime, timedelta, timezone


# Create your models here.
class Plant(models.Model):
    planted_date = models.DateTimeField("date planted")
    seed_url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    stages = models.ManyToManyField('Stage',through="PlantStage",related_name='stages')

    
    def __str__(self):
        return self.name

    def age(self):
        age = datetime.now(timezone.utc) - self.planted_date
        return age.days
        

    def actual_stage(self):
        return "actual stage"


class Stage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PlantStage(models.Model):
    plant = models.ForeignKey('Plant',related_name='plantStages', on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage',on_delete=models.CASCADE)

    started = models.DateTimeField("started",null=True, blank=True)
    ended = models.DateTimeField("ended",null=True, blank=True)

    def __str__(self):
        return self.plant.name + ' '+self.stage.name

class Image(models.Model):
    plant = models.ForeignKey('Plant', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    created_at = models.DateTimeField('created_at',auto_now_add=True)
    updated_at = models.DateTimeField('updated_at',auto_now=True)
    def __str__(self):
        return self.image.url
    
class StagePlanning(models.Model):
    stage = models.ForeignKey("Stage", related_name='planning', on_delete=models.CASCADE)
    lights= models.FloatField(null=True,blank= True)
    humidity= models.FloatField(null=True,blank= True)

    def __str__(self):
        return self.stage.name + ' Planning'