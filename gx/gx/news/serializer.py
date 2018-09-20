from rest_framework import serializers
from .models import NewsInfo


class NewsInfoSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(label='新闻',format='%Y-%m-%d %H:%M')

    class Meta:
        model = NewsInfo
        fields = ('id', 'title', 'create_time', 'content', 'source', 'click_count', 'user')


