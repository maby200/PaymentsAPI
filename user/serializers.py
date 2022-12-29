from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from user.models import User


# class UserModelSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = "__all__"

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length = 8, write_only=True)

    class Meta:
        model = User
        fields = (
                'username',
                'email',
                'password',
                )

    def validate(self, attrs):
        """see if email is already taken before signing up"""
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email is already taken")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

# create GetUserSerializer? why would I need a list of users 
# if I can see it in the admin page?
# according to chat it is needed for leting users see information ..

class GetUserSerializer(serializers.ModelSerializer):
    
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
                    "email",
                    "username",
                    "password",
                ]

    # ya que el modelo no tiene especificaciones en sus campos 
    # como `max_length` o `write_only`, es necesario que ,
    # por más que se haya creado un serializador tipo ModelSerializer
    # se tenga que especificar cómo se va a querer los datos de entrada 
    # en cada uno de los campos que se van a usar de modelos
