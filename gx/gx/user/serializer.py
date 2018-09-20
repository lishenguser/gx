from rest_framework import serializers
from django.contrib.auth.models import User
import re


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'mobile')
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 20,
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
            }
        }

    def validate_mobile(self, value):
        """手机号是否合法"""
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号不合法')
        return value

    def create(self, validated_data):
        """保存注册用户的信息"""
        # 创建新用户
        user = super().create(validated_data)
        # 对用户密码进行加密
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile','password')