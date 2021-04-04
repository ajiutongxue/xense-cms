from django.contrib import admin
import xadmin
from xadmin import views
from xadmin.views.base import CommAdminView
from .models import Category, SinglePage, Post, News, TCMFTCNews, IndNews, Activity, Alumni, Platform, Projects, \
    Achievement, Articles, Patents, Gallery, StaffExperts, StaffFaculty, StaffPostgraduates, StaffProfessors, \
    StaffStudents, Calendar, Focus, Links, SiteInfo


# Article, Post, ActivityPost, Alumni, Staff,


# Register your models here.

class GlobalSettings(object):
    site_title = '未来交通研究中心后台管理系统'
    site_footer = '未来交通研究中心'
    # 将app下的字段信息收起来
    menu_style = 'accordion'

    def get_site_menu(self):
        return (
            {'title': '网站设置', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '网站基本信息', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(SiteInfo, 'changelist')},
                {'title': '友情链接', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(Links, 'changelist')}
            )},
            {'title': '首页', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '幻灯片', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(Focus, 'changelist')},
                {'title': '活动日历', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(Calendar, 'changelist')}
            )},
            {'title': '独立页面', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(SinglePage, 'changelist')},
            {'title': '新闻动态', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '中心动态', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(TCMFTCNews, 'changelist')},
                {'title': '行业动态', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(IndNews, 'changelist')},
            )},
            {'title': '学术活动', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '学术活动', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Activity, 'changelist')},
            )},
            {'title': '科学研究', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '研究平台', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Platform, 'changelist')},
                {'title': '研究项目', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Projects, 'changelist')},
                {'title': '成果转化', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Achievement, 'changelist')},
            )},
            {'title': '成果奖励', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '科学论文', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Articles, 'changelist')},
                {'title': '发明专利', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Patents, 'changelist')},
                {'title': '荣誉奖励', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Gallery, 'changelist')},
            )},
            {'title': '师资力量', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '教师', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffFaculty, 'changelist')},
                {'title': '研究生', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffPostgraduates, 'changelist')},
                {'title': '访问教授', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffProfessors, 'changelist')},
                {'title': '特聘专家', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffExperts, 'changelist')},
                {'title': '访问学生', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffStudents, 'changelist')},
            )},
            {'title': '学友风采', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Alumni, 'changelist')},
        )


class SiteInfoAdmin(object):
    list_display = ['lang', 'title', 'linkman', 'addr', 'tel', 'email', 'copy']
    list_editable = ['title', 'linkman', 'addr', 'tel', 'email', 'copy']
    fields = ['lang', 'title', 'keywords', 'description', 'linkman', 'addr', 'qr', 'tel', 'email', 'copy']


# class CategoryAdmin(object):
# @admin.site.register
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['rank_num', 'cate_name', 'slug', 'full_name', 'parent_name', 'parent_name_en',
                    'default_self_template']
    # list_editable = ('rank_num', 'parent_name', 'parent_name_en', 'default_self_template')
admin.site.register(Category, CategoryAdmin)


class CategoryAdmin(object):
    list_display = ['rank_num', 'cate_name', 'slug', 'full_name', 'parent_name', 'parent_name_en',
                    'default_self_template']
    list_editable = ('rank_num', 'parent_name', 'parent_name_en', 'default_self_template')


class SinglePageAdmin(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    model_icon = 'fa fa-times'
    fields = ('category', 'title', 'slug', 'rank_num', 'custom_tmpl', 'content')

    # 这个可以根据条件在表单中显示不同的字段，还要查写资料 看里面具体怎么写
    # https://blog.csdn.net/qq_15028721/article/details/112475439?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-12&spm=1001.2101.3001.4242
    # def get_model_form(self, *args, **kwargs):
    #     self.form_obj.fields = ['title', 'content', 'rank_num', 'category']
    #     print('####')
    #     print(self)
    #     if self.category.full_name == 'single_about':
    #         self.form_obj.fields = ['title', 'content', 'rank_num']
    #     return super(SinglePageAdmin, self).get_model_form(*args, **kwargs)

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='single')
        return super(SinglePageAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(SinglePageAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='single')
        return qs


class NewsAdmin(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    model_icon = 'fa fa-times'
    fields = ('category', 'title', 'slug', 'thumbnail', 'summary', 'rank_num', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='news')
        return super(NewsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(NewsAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='news')
        return qs


class TCMFTCNewsAdmin(NewsAdmin):

    def queryset(self):
        qs = super(TCMFTCNewsAdmin, self).queryset()
        qs = qs.filter(category__full_name='news-events')
        return qs


class IndNewsAdmin(NewsAdmin):

    def queryset(self):
        qs = super(IndNewsAdmin, self).queryset()
        qs = qs.filter(category__full_name='news-industry')
        return qs


class ActivityAdmin(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num', ]
    fields = ('category', 'title', 'slug', 'thumbnail', 'summary', 'rank_num', 'custom_tmpl', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='activities')
        return super(ActivityAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ActivityAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='activities')
        return qs


class PlatformAdmin(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num', ]
    fields = ('category', 'title', 'slug', 'thumbnail', 'rank_num', 'custom_tmpl', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-platform')
        return super(PlatformAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(PlatformAdmin, self).queryset()
        qs = qs.filter(category__full_name='research-platform')
        return qs


class ProjectsAdmin(object):
    list_display = ['id', 'title', 'category', 'rank_num', 'msg1', 'msg2']
    fields = ('category', 'title', 'rank_num', 'msg1', 'msg2')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-projects')
        return super(ProjectsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ProjectsAdmin, self).queryset()
        qs = qs.filter(category__full_name='research-projects')
        return qs


class AchievementAdmin(object):
    """
    成果转化
    """
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    fields = ('category', 'title', 'slug', 'rank_num', 'summary', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-industry')
        return super(AchievementAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(AchievementAdmin, self).queryset()
        qs = qs.filter(category__full_name='research-industry')
        return qs


class ArticlesAdmin(object):
    """
    科学论文
    """
    list_display = ['id', 'title', 'category', 'rank_num', 'url', 'is_published']
    fields = ('category', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('category', 'title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-articles')
        return super(ArticlesAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ArticlesAdmin, self).queryset()
        qs = qs.filter(category__full_name='achievements-articles')
        return qs


class PatentsAdmin(object):
    """
    发明专利
    """
    list_display = ['id', 'title', 'category', 'msg1', 'msg2', 'rank_num', 'is_published']
    fields = ('category', 'title', 'msg1', 'msg2', 'rank_num', 'is_published')
    list_editable = ('category', 'title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-patents')
        return super(PatentsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(PatentsAdmin, self).queryset()
        qs = qs.filter(category__full_name='achievements-patents')
        return qs


class GalleryAdmin(object):
    """
    发明专利
    """
    list_display = ['id', 'title', 'category', 'rank_num', 'is_published']
    fields = ('category', 'title', 'thumbnail', 'rank_num', 'is_published')
    list_editable = ('title', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-honors')
        return super(GalleryAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(GalleryAdmin, self).queryset()
        qs = qs.filter(category__full_name='achievements-honors')
        return qs


class StaffFacultyAdmin(object):
    """
    教师
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff')
        return super(StaffFacultyAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffFacultyAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-faculty')
        return qs


class StaffPostgraduatesAdmin(object):
    """
    研究生
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff')
        return super(StaffPostgraduatesAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffPostgraduatesAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-postgraduates')
        return qs


class StaffProfessorsAdmin(object):
    """
    访问教授
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff')
        return super(StaffProfessorsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffProfessorsAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-professors')
        return qs


class StaffExpertsAdmin(object):
    """
    特聘专家
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff')
        return super(StaffExpertsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffExpertsAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-experts')
        return qs


class StaffStudentsAdmin(object):
    """
    访问学生
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff')
        return super(StaffStudentsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffStudentsAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-students')
        return qs


class AlumniAdmin(object):
    """
    学友风采
    """
    list_display = ['id', 'title', 'slug', 'rank_num']
    fields = ('category', 'title', 'slug', 'thumbnail', 'rank_num', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='alumni')
        return super(AlumniAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(AlumniAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='alumni')
        return qs


class CalendarAdmin(object):
    list_display = ('id', 'title', 'active_time', 'month', 'day', 'addr', 'rank_num')
    list_editable = ('title', 'active_time', 'month', 'day', 'addr', 'rank_num')


class FocusAdmin(object):
    list_display = ('id', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('title', 'url', 'rank_num', 'is_published')


class LinksAdmin(object):
    list_display = ('id', 'title', 'url', 'rank_num', 'is_published')
    fields = ('category', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='friend-links')
        return super(LinksAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(LinksAdmin, self).queryset()
        qs = qs.filter(category__full_name='friend-links')
        return qs


class PostAdmin(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


xadmin.site.register(SiteInfo, SiteInfoAdmin)

xadmin.site.register(Category, CategoryAdmin)

xadmin.site.register(Calendar, CalendarAdmin)
xadmin.site.register(Focus, FocusAdmin)
xadmin.site.register(Links, LinksAdmin)

xadmin.site.register(SinglePage, SinglePageAdmin)

xadmin.site.register(News, NewsAdmin)
xadmin.site.register(TCMFTCNews, TCMFTCNewsAdmin)
xadmin.site.register(IndNews, IndNewsAdmin)

xadmin.site.register(Activity, ActivityAdmin)

xadmin.site.register(Platform, PlatformAdmin)
xadmin.site.register(Projects, ProjectsAdmin)
xadmin.site.register(Achievement, AchievementAdmin)

xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(Patents, PatentsAdmin)
xadmin.site.register(Gallery, GalleryAdmin)

xadmin.site.register(StaffFaculty, StaffFacultyAdmin)
xadmin.site.register(StaffPostgraduates, StaffPostgraduatesAdmin)
xadmin.site.register(StaffProfessors, StaffProfessorsAdmin)
xadmin.site.register(StaffExperts, StaffExpertsAdmin)
xadmin.site.register(StaffStudents, StaffStudentsAdmin)

xadmin.site.register(Alumni, AlumniAdmin)

xadmin.site.register(Post, PostAdmin)

xadmin.site.register(views.CommAdminView, GlobalSettings)
# admin.site.site_header = 'xcms'
