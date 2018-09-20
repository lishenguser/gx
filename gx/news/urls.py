from django.conf.urls import url
from news import views
from rest_framework.routers import DefaultRouter
urlpatterns = [
    # 首页的入口
    url(r'^index/$', views.IndexView.as_view()),
    # 点击一级分类的入口
    url(r'^category/$', views.NewsView.as_view()),
    # 新闻详情页的入口
    url(r'^detail/$', views.NewsDetail.as_view()),
    # 新闻浏览排行的入口
    url(r'^click/$', views.NewsClick.as_view()),
    # 新闻发布的入口
    url(r'^editor/$', views.NewsEditorView.as_view()),
    # 新闻分类列表
    url(r'^list/$', views.NewsListView.as_view()),
    # 分类修改
    url(r'^category_set/$', views.CategoryUpdate.as_view())

]
router = DefaultRouter()
router.register('search', views.NewsInfoSearchViewSet, base_name='news_search')
urlpatterns += router.urls