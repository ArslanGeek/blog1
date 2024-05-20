# from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.create_user(username=request.data.get('username'),
                                              password=request.data.get('password'))

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'


class UserLoginAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        # print(request.user)

        if user is not None:
            print(request.user)
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({
                'detail': 'You have successfully logged in.',
                'id': user.id,
                'first_name': user.first_name,
                'refreshToken': str(refresh),
                'accessToken': str(access_token),
                'refreshToken_lifetime_days': refresh.lifetime.days,
                'accessToken_lifetime_days': access_token.lifetime.days
            })
        else:
            return Response({'detail': 'Wrong authentication'},
                            status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutAPIView(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        try:
            access_token = request.data.get('accessToken')
            token = RefreshToken(access_token)
            token.blacklist()

            return Response({'detail': 'You have successfully logged out'},
                            status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'detail': 'Something got wrong'},
                status=status.HTTP_400_BAD_REQUEST
            )

class SendMessageAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(receiver_user_id=CustomUser.objects.get(id=request.data['receiver_user_id']))
            print(f'User: {request.user} sent message to: {request.data['receiver_user_id']}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

