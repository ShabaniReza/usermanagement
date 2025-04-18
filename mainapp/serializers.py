from rest_framework.serializers import ModelSerializer, CurrentUserDefault, PrimaryKeyRelatedField, ImageField, CharField
from .models import User, Profile


class ProfileSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    avatar = ImageField()
    first_name = CharField(source='user.first_name', read_only=True)
    last_name = CharField(source='user.last_name', read_only=True)


    class Meta:
        model = Profile
        fields = '__all__'