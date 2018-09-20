from rest_framework.views import APIView
from user.serializer import CreateUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from user.serializer import UserSerializer


class UserView(APIView):
    """
    注册用户
    """
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # 返回应答，注册成功
        serializer = CreateUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthorizationsView(APIView):
    """
    用户登入
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': '用户不存在'}, status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
                return Response({'message': '密码错误'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UserDetailView(APIView):
    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)