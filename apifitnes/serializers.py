from rest_framework.serializers import ModelSerializer
from .models import Tarifs, Training, Personal, Clubs

class PersonalSerializer(ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class TarifsSerializer(ModelSerializer):
    class Meta:
        model = Tarifs
        fields = '__all__'

class ClubsSerializer(ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'

class TrainingSerializer(ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

