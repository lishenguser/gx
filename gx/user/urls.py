from django.conf.urls import url
from user import views

urlpatterns = [
    # 用户注册的入口
    url(r'', views.UserView.as_view()),
    # 用户登入
    url(r'^authorizations/$', views.AuthorizationsView.as_view()),
    url(r'^detail/$', views.UserDetailView.as_view()),


]