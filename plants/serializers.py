#from rest_framework import serializers
from plants.models import Plant, PlantStage, Stage, Image, StagePlanning
from rest_framework_json_api import serializers

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Image
        fields = ['image']

class StagePlanningSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StagePlanning
        fields = '__all__'


class StageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stage
        fields = ['name','id','planning','started']


class PlantStageSerializer(serializers.HyperlinkedModelSerializer):
    stage = StageSerializer()
    
    stage_name = serializers.SerializerMethodField()
    class Meta:
        model = PlantStage
        fields = ['plant', 'stage', 'started','ended','stage_name']
    
    def get_stage_name(self, obj):
        return obj.stage.name
        
class PlantSerializer(serializers.HyperlinkedModelSerializer):
    #images = ImageSerializer(many=True )
    image_urls = serializers.SerializerMethodField()
    #stages = serializers.SerializerMethodField()
    actual_stage = serializers.SerializerMethodField()
    
    class Meta:
        model = Plant
        #fields = '__all__'
        fields = ['name','planted_date','seed_url','age', 'image_urls','actual_stage']
   

    def get_image_urls(self, obj):
        arr=[]
        for image in obj.images.values('image'):
            arr.append(image['image'])
        return arr

    # def get_actual_stage(self, obj):
    #     arr=""
    #     for plantstage in obj.plantStages.values():
    #         if not plantstage['ended']:
    #             for stage in obj.stages.values():
    #                 if plantstage['stage_id'] == stage['id']:
    #                     arr = stage
    #     return arr

    def get_actual_stage(self, obj):
        actual_stage_data = {}
        for plantstage in obj.plantStages.values():
            if not plantstage['ended']:
                stage_id = plantstage['stage_id']
                stage = obj.stages.filter(id=stage_id).values().first()
                actual_stage_data['id'] = stage_id
                actual_stage_data['name'] = stage['name']
                actual_stage_data['started'] = plantstage['started']
                
                # Include stage planning information
                stage_planning = StagePlanning.objects.filter(stage_id=stage_id).values().first()
                if stage_planning:
                    actual_stage_data['planning'] = {
                        'lights': stage_planning['lights'],
                        'humidity': stage_planning['humidity']
                    }
                break  # Break the loop once the actual stage is found

        return actual_stage_data
