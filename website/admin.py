from django.contrib import admin
# from .models import About, SinglePage
from .models import SinglePage, Category, Article


# Register your models here.

# class AboutAdmin(admin.ModelAdmin):
#     list_display = ['name', 'rank_num', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_name']


class SinglePageAdmin(admin.ModelAdmin):
    list_display = ['page_title', 'category', 'rank_num', 'slug', ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'rank_num', ]


# admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SinglePage, SinglePageAdmin)
admin.site.register(Article, ArticleAdmin)

admin.site.site_header = 'xcms'
