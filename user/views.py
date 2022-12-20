from django.contrib.auth import authenticate
from django.shortcuts import get_list_or_404

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets

from .serializers import SignUpSerializer, GetUserSerializer
from .tokens import create_jwt_pair_for_user
from .models import User


class SignupView(APIView):
    """APIView already comes with CRUD functions"""
    serializer_class = SignUpSerializer
    
    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                        "mes    sage":"El usuario se creó correctamente",
                        "data":serializer.data
                        }

            return Response(
                            data = response,
                            status=status.HTTP_201_CREATED
                            )
        return Response(
                        data = serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                        )

class LoginView(APIView):

    def post(self, request:Request): 
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email = email, password = password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            idUser = User.objects.get(email=email)

            response = {
                        "message": "Successful login!",
                        # "email": email, # tenías que entrar a su atributo email, no listarlo 
                        "id":idUser.email,
                        "tokens":tokens
                        }
            
            return Response(data=response, status=status.HTTP_200_OK)

            # if tokens:
            #     login(self.request, idUser)
        return Response(
                        data = {
                                "message":"Invalid email or incorrect password"
                                }
                        )
    def get(self, request:Request):
        content = {
                    "user":str(request.user),
                    "auth":str(request.auth)
                    }
        
        return Response(
                        data=content,
                        status=status.HTTP_200_OK
                        )

class GetUsersView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer