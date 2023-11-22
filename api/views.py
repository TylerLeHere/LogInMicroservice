from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, HistorySerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import User, HealthHistory
import jwt
import datetime

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        print(request.data)

        phn = request.data['phn']
        password = request.data['password']

        user = User.objects.filter(phn=phn).first()

        if user is None:
            raise AuthenticationFailed("User not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        
        # user is authenticated
        payload = {
            'id' : user.phn,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token: str = jwt.encode(payload, "super_secret")

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt' : token, 'phn': user.phn, 'name': user.name}

        print(f'success. this is token {token}')

        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            print("not authenticated")
            raise AuthenticationFailed("Not authenticated")
        
        try:
            payload = jwt.decode(token, "super_secret", algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            print("not authenticated 2")
            raise AuthenticationFailed("Not authenticated")
        
        user = User.objects.filter(phn=payload['id']).first()
        serializer = UserSerializer(user)

        print(f'{serializer.data}')
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, response):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success'
        }

        return response

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    
class HistoryView(generics.ListCreateAPIView):
    serializer_class = HistorySerializer

    def get(self, request,  *args, **kwargs):
        phn = self.request.GET.get('phn', None)
        if phn is not None:
            history = HealthHistory.objects.filter(user=phn)
            serializer = HistorySerializer(history, many=True)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return HealthHistory.objects.all()
    
class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        return HealthHistory.objects.all()


