# from django.contrib import admin
import xadmin
from website.models import Category, Article, Post, ActivityPost, Alumni, Staff, SinglePage


# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(object):
    list_display = ['rank_num', 'cate_name', 'slug', 'parent_cate']


# class ArticleAdmin(admin.ModelAdmin):
class ArticleAdmin(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    fields = ('title', 'slug', 'rank_num')
    prepopulated_fields = {'slug': ('title',)}


# class PostAdmin(admin.ModelAdmin):
class PostAdmin(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


# class ActivityPostAdmin(admin.ModelAdmin):
class ActivityPostAdmin(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


# class StaffAdmin(admin.ModelAdmin):
class StaffAdmin(object):
    list_display = ['id', 'name', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('name',)}


# class AlumniAdmin(admin.ModelAdmin):
class AlumniAdmin(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


# about page
# class SinglePageAdmin(admin.ModelAdmin):
class SinglePageAdmin(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(ActivityPost, ActivityPostAdmin)
xadmin.site.register(Alumni, AlumniAdmin)
xadmin.site.register(Staff, StaffAdmin)
xadmin.site.register(SinglePage, SinglePageAdmin)

# admin.site.site_header = 'xcms'
