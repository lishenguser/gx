# 自定义DRF框架分页类
from rest_framework.pagination import PageNumberPagination


class NewsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'size'
    max_page_size = 20