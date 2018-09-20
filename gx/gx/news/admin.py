from django.contrib import admin

# Register your models here.
from news.models import *

admin.site.register(NewsCategory)
admin.site.register(NewsInfo)
