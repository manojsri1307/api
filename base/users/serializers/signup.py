from rest_framework import serializers
from django.contrib.auth.models import User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    def create(self, validated_data): 
        print('valid ===>>', validated_data)
        user = User.objects.create(
            username=validated_data.get('username'),
            password=validated_data['password']
        )

        return user
    