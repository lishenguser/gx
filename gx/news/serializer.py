from rest_framework import serializers
from .models import NewsInfo, NewsCategory
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import NewsInfoIndex


class NewsInfoSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(label='新闻',format='%Y-%m-%d %H:%M')

    class Meta:
        model = NewsInfo
        fields = ('id', 'title', 'create_time', 'content', 'source', 'click_count', 'user')


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        field = ('id', 'name', 'parent')


class NewsInfoIndexSerializer(HaystackSerializer):
    """搜索结果序列化器类"""
    object = NewsInfoSerializer(read_only=True)

    class Meta:
        index_classes = [NewsInfoIndex]
        fields = ('text', 'object')