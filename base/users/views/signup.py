from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..serializers.signup import SignupSerializer

class SignupView(APIView):
    def post(self, request):
        serializerData = SignupSerializer(data = request.data)

        if serializerData.is_valid():
            serializerData.save()
            return Response({'message': 'user register successfully!'}, status=status.HTTP_201_CREATED)
        
        return Response({'message': serializerData.errors}, status=status.HTTP_400_BAD_REQUEST)
        