
from plants.models import Plant , Image
from plants.serializers import PlantSerializer, ImageSerializer


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PlantList(APIView):
    """
    List all plants, or create a new plant.
    """
    def get(self, request, format=None):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlantDetail(APIView):
    """
    Retrieve, update or delete a plant instance.
    """
    def get_object(self, pk):
        try:
            return Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        plant = self.get_object(pk)
        serializer = PlantSerializer(plant, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        plant = self.get_object(pk)
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        plant = self.get_object(pk)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class PlantImages(APIView):

    """
    List all plant images, or create a new image.
    """
    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



