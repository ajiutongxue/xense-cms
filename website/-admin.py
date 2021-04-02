from django.contrib import admin
from .models import Category, Article, Post, ActivityPost, Alumni, Staff, SinglePage


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['rank_num', 'cate_name', 'slug', 'parent_cate']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    fields = ('title', 'slug', 'rank_num')
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


class ActivityPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('name',)}


class AlumniAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


# about page
class SinglePageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


# admin.site.register(About, AboutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ActivityPost, ActivityPostAdmin)
admin.site.register(Alumni, AlumniAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(SinglePage, SinglePageAdmin)

admin.site.site_header = 'xcms'
