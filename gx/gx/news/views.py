from rest_framework.views import APIView
from news.utils import CORSResponse
from .serializer import NewsInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from news.models import NewsCategory, NewsInfo
from news.pagination import NewsPagination


# 127.0.0.1:8000/news/list/?category_id=1
class NewsView(APIView):
    """
    展示父级分类页面的新闻
    """
    def get(self, request):
        """
        :param request:category_id是父级新闻分类的id
        :return:返回被点击的父级分类下面所有的新闻
        """
        category_id = request.query_params.get('category_id')
        try:
            category = NewsCategory.objects.get(id=category_id)
        except NewsCategory.DoesNotExist:
            return Response({'message': '分类不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            news = NewsInfo.objects.filter(category__parent__id=category.id)
            serializer = NewsInfoSerializer(news, many=True)
            return CORSResponse(serializer.data)


# 127.0.0.1:8000/news/index/?category_id=2
class IndexView(APIView):
    """
    展示首页
    """
    def get(self, request):
        """
        :param request:category_id是子级分类的id
        :return: 返回首页需要展示的子级分类的新闻
        """
        category_id = request.query_params.get('category_id')
        try:
            news_category = NewsCategory.objects.get(id=category_id)
        except NewsCategory.DoesNotExist:
            return CORSResponse({'message': '分类不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 通过外键找出新闻
            news = news_category.newsinfo_set.all()
            serializer = NewsInfoSerializer(news, many=True)
            return CORSResponse(serializer.data)


# 127.0.0.1:8000/news/detail/?news_id=2
class NewsDetail(APIView):
    """
    新闻内容的展示
    """
    def get(self, request):
        """
        :param request:news_id是新闻的id
        :return: 返回具体新闻的内容
        """
        news_id = request.query_params.get('news_id')
        news = NewsInfo.objects.get(id=news_id)
        news.click_count += 1
        news.save()
        serializer = NewsInfoSerializer(news)
        return CORSResponse(serializer.data)


# http://127.0.0.1:8000/news/click/?show_count=5
class NewsClick(APIView):
    """
    新闻浏览量排行展示
    """
    def get(self, request):
        """
        :param request:show_count是展示是新闻条数
        :return: 返回按照浏览量排序的新闻
        """
        show_count = request.query_params.get('show_count', 6)
        news_click_list = NewsInfo.objects.all().order_by('-click_count')[0:show_count]
        serializer = NewsInfoSerializer(news_click_list, many=True)
        return CORSResponse(serializer.data)


# 192.168.1.4:8000/news/editor/
class NewsEditorView(APIView):
    """
    新闻发布
    """

    def get(self, request):
        """
        :param request:不需要传参数
        :return: 返回新闻的分类
        """
        categorys = NewsCategory.objects.filter(parent__isnull=True)
        data = []
        for category in categorys:
            category_dict = {'value': category.id, 'label': category.name}
            dict_list = []
            for category_second in NewsCategory.objects.filter(parent=category.id):
                dict_list.append({
                    'value': category_second.id,
                    'label': category_second.name
                })
            # dict_list 没有数据时 就可以不显示
            if dict_list:
                category_dict['children'] = dict_list
            data.append(category_dict)
        return CORSResponse(data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:上传新闻的字段
        :return: 返回作者发布的新闻
        """
        title = request.data.get('title')
        source = request.data.get('source', '')
        user = request.data.get('user_id', 1)
        content = request.data.get('content')
        category = request.data.get('category_id')
        if not all([title,  user, content, category]):
            return CORSResponse({'message': '不能有空值'})
        news = NewsInfo.objects.create(title=title, source=source, content=content,
                                       user_id=user, category_id=category)
        serializer = NewsInfoSerializer(news)
        return CORSResponse(serializer.data)


class NewsListView(APIView):
    """
    分页展示新闻
    """

    def get(self, request):
        news = NewsInfo.objects.all()
        pg = NewsPagination()
        page_news = pg.paginate_queryset(queryset=news, request=request, view=self)
        serializer = NewsInfoSerializer(page_news, many=True)
        return CORSResponse({'list': serializer.data, 'total': news.count()})
