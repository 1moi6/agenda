from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer, AdmTokenPairSerializer
from rest_framework.decorators import  permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioRegistroView(generics.CreateAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário registrado com sucesso."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AdmTokenPairView(TokenObtainPairView):
    serializer_class = AdmTokenPairSerializer