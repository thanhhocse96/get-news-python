from django.contrib import admin

from .models import News, News_Stance, News_Authors, News_Images, News_Movies
# Register your models here.

admin.site.register(News)
admin.site.register(News_Stance)
admin.site.register(News_Authors)