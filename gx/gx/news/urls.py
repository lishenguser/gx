from django.conf.urls import url
from news import views

urlpatterns = [
    # 首页的入口
    url(r'^index/$', views.IndexView.as_view()),
    # 点击一级分类的入口
    url(r'^catagory/$', views.NewsView.as_view()),
    # 新闻详情页的入口
    url(r'^detail/$', views.NewsDetail.as_view()),
    # 新闻浏览排行的入口
    url(r'^click/$', views.NewsClick.as_view()),
    # 新闻发布的入口
    url(r'^editor/$', views.NewsEditorView.as_view()),
    url(r'^list/$', views.NewsListView.as_view()),

]
