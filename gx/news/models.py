from django.contrib.auth.models import User
from django.db import models
from gx.models import BaseModel


class NewsCategory(models.Model):
    """
    新闻类别
    """
    name = models.CharField(max_length=10, verbose_name='名称')
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name='父类别')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_news_category'
        verbose_name = '新闻类别'
        verbose_name_plural = verbose_name


class NewsInfo(BaseModel):
    """
    新闻
    """
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    source = models.CharField(max_length=10, verbose_name='来源', default='')
    click_count = models.IntegerField(verbose_name='浏览次数', default=0)
    # 关系外键：分类与新闻为1对多的关系，在新闻中定义外键，在分类中定义属性
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name='新闻类别')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', null=True)

    class Meta:
        db_table = 'tb_news'
        ordering = ['-create_time']
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


