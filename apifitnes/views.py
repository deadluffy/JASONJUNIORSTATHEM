from rest_framework.viewsets import ModelViewSet
from .serializers import ClubsSerializer, TarifsSerializer, PersonalSerializer, TrainingSerializer
from .models import Clubs, Tarifs, Training, Personal
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

class PersonalViewSet(ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class TarifsViewSet(ModelViewSet):
    queryset = Tarifs.objects.all()
    serializer_class = TarifsSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delTarif(self,request, pk=None):
        tarif=self.queryset.get(id=pk)
        tarif.delete()
        return Response('Удалено')

class ClubsViewSet(ModelViewSet):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer


class TrainingViewSet(ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class GetPersonalView(ListAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'age']


class GetClubsView(ListAPIView):
    queryset = Clubs.objects.filter( Q(amount__gt=230) )
    serializer_class = ClubsSerializer
