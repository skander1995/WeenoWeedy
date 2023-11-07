from django.contrib import admin

# Register your models here.
from .models import Plant, Stage,PlantStage, Image, StagePlanning

admin.site.register(Plant)
admin.site.register(Stage)
admin.site.register(PlantStage)
admin.site.register(Image)
admin.site.register(StagePlanning)
