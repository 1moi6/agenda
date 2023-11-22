from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class UsuarioSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True,required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = get_user_model()  # Use get_user_model() para obter o modelo de usuário configurado
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'password_confirmation', 'clinica', 'cnpj')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'clinica': {'required': True},
            'cnpj': {'required': True},
        }

    def validate(self, data):
        # Garantir que a senha e a confirmação de senha correspondam
        if data.get('password') != data.get('password_confirmation'):
            raise serializers.ValidationError("As senhas não correspondem.")
        return data

    def create(self, validated_data):
        # Remover a confirmação de senha antes de criar o usuário
        validated_data.pop('password_confirmation', None)

        user = CustomUser.objects.create_user(**validated_data)
        return user

class AdmTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['nome'] = user.first_name
        token['sobrenome'] = user.last_name
        token['clinica'] = user.clinica
        token['cnpj'] = user.cnpj
        # ...

        return token