from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Address, Profile, User

#
# class UserBriefSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'phone', 'firstname', 'lastname']


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ['password']

    def get_owner(self, obj):
        result = obj.owner.all()
        return AddressSerializers(instance=result, many=True).data

# class AddressBriefSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = ['id', 'owner', 'city']


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


# class ProfileBriefSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['id', 'user', 'phone']


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'




