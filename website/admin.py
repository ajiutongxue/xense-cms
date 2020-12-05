from django.contrib import admin
from .models import Category, Article


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['rank_num', 'cate_name', 'slug', 'parent_cate']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'rank_num', ]


# admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.site_header = 'xcms'
