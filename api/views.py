from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import HabitatSerializer, AnimalSerializer
from .models import Habitat, Animal

class HabitatViewSet(ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer

class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def list(self, request):
        queryset = Animal.objects.all()
        filterName = request.GET.get('name', None)
        filterHabitat = request.GET.get('habitat', None)
        order = request.GET.get('order', None)
        if filterName != None:
            queryset = queryset.filter(name=filterName)
        if filterHabitat != None:
            queryset = queryset.filter(habitat=filterHabitat)
        if order != None:
            queryset = queryset.order_by(order)
        # animal = get_object_or_404(queryset, many)
        serializer = AnimalSerializer(queryset, many=True)
        return Response(serializer.data)




        

    # def create(self, request):
    #     print('on create')

    # def get_queryset(self):
    #     name = self.kwargs['name']
    #     return Animal.objects.filter(name=name)

# class AnimalViewSetFilterByName(ModelViewSet):
#     queryset = Animal.objects.filter()
#     serializer_class = AnimalSerializer
