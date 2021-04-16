from django.contrib import admin
import xadmin
from xadmin import views
from xadmin.views.base import CommAdminView
from .models import Category, SinglePage, Post, News, TCMFTCNews, IndNews, Activity, Alumni, Platform, Projects, \
    Achievement, Articles, Patents, Gallery, StaffExperts, StaffFaculty, StaffPostgraduates, StaffProfessors, \
    StaffStudents, Calendar, Focus, Links, SiteInfo
from .models import SinglePage_en, Post_en, News_en, TCMFTCNews_en, IndNews_en, Activity_en, Alumni_en, Platform_en, \
    Projects_en, Achievement_en, Articles_en, Patents_en, Gallery_en, StaffExperts_en, StaffFaculty_en, \
    StaffPostgraduates_en, StaffProfessors_en, StaffStudents_en, Links_en


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
                 'url': self.get_model_url(Links, 'changelist')},
                {'title': '友情链接 en', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(Links_en, 'changelist')},
            )},
            {'title': '首页', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '幻灯片', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(Focus, 'changelist')},
                {'title': '活动日历', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(Calendar, 'changelist')}
            )},
            {'title': '独立页面', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '独立页面内容', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(SinglePage, 'changelist')},
                {'title': '独立页面内容_en', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(SinglePage_en, 'changelist')}
            )},
            {'title': '新闻动态', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '中心动态', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(TCMFTCNews, 'changelist')},
                {'title': '行业动态', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(IndNews, 'changelist')},
                {'title': '中心动态_en', 'icon': 'fa fa-angle-right',
                 'url': self.get_model_url(TCMFTCNews_en, 'changelist')},
                {'title': '行业动态_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(IndNews_en, 'changelist')},
            )},
            {'title': '学术活动', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '学术活动', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Activity, 'changelist')},
                {'title': '学术活动_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Activity_en, 'changelist')},
            )},
            {'title': '科学研究', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '研究平台', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Platform, 'changelist')},
                {'title': '研究项目', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Projects, 'changelist')},
                {'title': '成果转化', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Achievement, 'changelist')},
                {'title': '研究平台_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Platform_en, 'changelist')},
                {'title': '研究项目_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Projects_en, 'changelist')},
                {'title': '成果转化_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Achievement_en, 'changelist')},
            )},
            {'title': '成果奖励', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '科学论文', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Articles, 'changelist')},
                {'title': '发明专利', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Patents, 'changelist')},
                {'title': '荣誉奖励', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Gallery, 'changelist')},
                {'title': '科学论文_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Articles_en, 'changelist')},
                {'title': '发明专利_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Patents_en, 'changelist')},
                {'title': '荣誉奖励_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Gallery_en, 'changelist')},
            )},
            {'title': '师资力量', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '教师', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffFaculty, 'changelist')},
                {'title': '研究生', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffPostgraduates, 'changelist')},
                {'title': '访问教授', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffProfessors, 'changelist')},
                {'title': '特聘专家', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffExperts, 'changelist')},
                {'title': '访问学生', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffStudents, 'changelist')},
                {'title': '教师_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffFaculty_en, 'changelist')},
                {'title': '研究生_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffPostgraduates_en, 'changelist')},
                {'title': '访问教授_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffProfessors_en, 'changelist')},
                {'title': '特聘专家_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffExperts_en, 'changelist')},
                {'title': '访问学生_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(StaffStudents_en, 'changelist')},
            )},
            {'title': '学友风采', 'icon': 'fa fa-angle-down', 'menus': (
                {'title': '学友风采', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Alumni, 'changelist')},
                {'title': '学友风采_en', 'icon': 'fa fa-angle-right', 'url': self.get_model_url(Alumni_en, 'changelist')}
            )},
        )


class SiteInfoAdmin(object):
    list_display = ['lang', 'title', 'linkman', 'addr', 'tel', 'email', 'copy']
    list_editable = ['title', 'linkman', 'addr', 'tel', 'email', 'copy']
    fields = ['lang', 'title', 'keywords', 'description', 'linkman', 'addr', 'qr', 'tel', 'email', 'copy']


@admin.register(Category)
class ACategoryAdmin(admin.ModelAdmin):
    list_display = ['rank_num', 'cate_name', 'slug', 'full_name', 'parent_name', 'lang',
                    'default_self_template']
    # list_editable = ('rank_num', 'parent_name', 'parent_name_en', 'default_self_template')
# admin.site.register(Category, CategoryAdmin)


@admin.register(Focus)
class AFocusAdmin(admin.ModelAdmin):
    list_display = ['id', 'rank_num', 'lang']


class CategoryAdmin(object):
    list_display = ['id', 'rank_num', 'cate_name', 'slug', 'full_name', 'parent_name', 'lang',
                    'default_self_template']
    list_editable = ('rank_num', 'cate_name', 'slug', 'full_name', 'parent_name', 'lang', 'default_self_template')


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
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='single', lang='zh')
        return super(SinglePageAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(SinglePageAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='single', category__lang='zh')
        return qs


class SinglePageAdmin_en(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    model_icon = 'fa fa-times'
    fields = ('category', 'title', 'slug', 'rank_num', 'custom_tmpl', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='single', lang='en')
        return super(SinglePageAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(SinglePageAdmin_en, self).queryset()
        qs = qs.filter(category__full_name__startswith='single', category__lang='en')
        return qs


class NewsAdmin(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    model_icon = 'fa fa-times'
    fields = ('category', 'title', 'slug', 'thumbnail', 'summary', 'rank_num', 'writer', 'pub_date', 'content')
    # fields.title.short_description = '这是大标题'
    view_on_site = True

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='news')
        return super(NewsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(NewsAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='news')
        return qs


class TCMFTCNewsAdmin(NewsAdmin):
    view_on_site = True

    def queryset(self):
        qs = super(TCMFTCNewsAdmin, self).queryset()
        qs = qs.filter(category__full_name='news-events')
        return qs


class IndNewsAdmin(NewsAdmin):

    def queryset(self):
        qs = super(IndNewsAdmin, self).queryset()
        qs = qs.filter(category__full_name='news-industry')
        return qs


class NewsAdmin_en(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    model_icon = 'fa fa-times'
    fields = ('category', 'title', 'slug', 'thumbnail', 'summary', 'rank_num', 'writer', 'pub_date', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='news', lang='en')
        return super(NewsAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(NewsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name__startswith='news')
        return qs


class TCMFTCNewsAdmin_en(NewsAdmin_en):

    def queryset(self):
        qs = super(TCMFTCNewsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='news-events')
        return qs


class IndNewsAdmin_en(NewsAdmin_en):

    def queryset(self):
        qs = super(IndNewsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='news-industry')
        return qs


class ActivityAdmin(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num', ]
    fields = ('category', 'title', 'slug', 'thumbnail', 'summary', 'rank_num', 'pub_date', 'writer', 'custom_tmpl', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='activities', lang='zh')
        return super(ActivityAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ActivityAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='activities', category__lang='zh')
        return qs


class ActivityAdmin_en(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num', ]
    fields = ('category', 'title', 'slug', 'thumbnail', 'summary', 'rank_num', 'pub_date', 'writer', 'custom_tmpl', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='activities', lang='en')
        return super(ActivityAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ActivityAdmin_en, self).queryset()
        qs = qs.filter(category__full_name__startswith='activities', category__lang='en')
        return qs


class PlatformAdmin(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num', ]
    fields = ('category', 'title', 'slug', 'thumbnail', 'rank_num', 'writer', 'custom_tmpl', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-platform', lang='zh')
        return super(PlatformAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(PlatformAdmin, self).queryset()
        qs = qs.filter(category__full_name='research-platform', category__lang='zh')
        return qs


class PlatformAdmin_en(object):
    list_display = ['id', 'title', 'category', 'slug', 'rank_num', ]
    fields = ('category', 'title', 'slug', 'thumbnail', 'rank_num', 'writer', 'custom_tmpl', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-platform', lang='en')
        return super(PlatformAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(PlatformAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='research-platform', category__lang='en')
        return qs


class ProjectsAdmin(object):
    list_display = ['id', 'title', 'category', 'rank_num', 'msg1', 'msg2']
    fields = ('category', 'title', 'rank_num', 'msg1', 'msg2')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-projects', lang='zh')
        return super(ProjectsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ProjectsAdmin, self).queryset()
        qs = qs.filter(category__full_name='research-projects', category__lang='zh')
        return qs


class ProjectsAdmin_en(object):
    list_display = ['id', 'title', 'category', 'rank_num', 'msg1', 'msg2']
    fields = ('category', 'title', 'rank_num', 'msg1', 'msg2')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-projects', lang='en')
        return super(ProjectsAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ProjectsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='research-projects', category__lang='en')
        return qs


class AchievementAdmin(object):
    """
    成果转化
    """
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    fields = ('category', 'title', 'slug', 'rank_num', 'writer', 'summary', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-industry', lang='zh')
        return super(AchievementAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(AchievementAdmin, self).queryset()
        qs = qs.filter(category__full_name='research-industry',category__lang='zh')
        return qs


class AchievementAdmin_en(object):
    """
    成果转化 en
    """
    list_display = ['id', 'title', 'category', 'slug', 'rank_num']
    fields = ('category', 'title', 'slug', 'rank_num', 'writer', 'summary', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='research-industry', lang='en')
        return super(AchievementAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(AchievementAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='research-industry', category__lang='en')
        return qs


class ArticlesAdmin(object):
    """
    科学论文
    """
    list_display = ['id', 'title', 'category', 'rank_num', 'url', 'is_published']
    fields = ('category', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('category', 'title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-articles', lang='zh')
        return super(ArticlesAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ArticlesAdmin, self).queryset()
        qs = qs.filter(category__full_name='achievements-articles', category__lang='zh')
        return qs


class ArticlesAdmin_en(object):
    """
    科学论文
    """
    list_display = ['id', 'title', 'category', 'rank_num', 'url', 'is_published']
    fields = ('category', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('category', 'title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-articles', lang='en')
        return super(ArticlesAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(ArticlesAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='achievements-articles', category__lang='en')
        return qs


class PatentsAdmin(object):
    """
    发明专利
    """
    list_display = ['id', 'title', 'category', 'msg1', 'msg2', 'rank_num', 'is_published']
    fields = ('category', 'title', 'msg1', 'msg2', 'rank_num', 'is_published')
    list_editable = ('category', 'title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-patents', lang='zh')
        return super(PatentsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(PatentsAdmin, self).queryset()
        qs = qs.filter(category__full_name='achievements-patents', category__lang='zh')
        return qs


class PatentsAdmin_en(object):
    """
    发明专利
    """
    list_display = ['id', 'title', 'category', 'msg1', 'msg2', 'rank_num', 'is_published']
    fields = ('category', 'title', 'msg1', 'msg2', 'rank_num', 'is_published')
    list_editable = ('category', 'title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-patents', lang='en')
        return super(PatentsAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(PatentsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='achievements-patents', category__lang='en')
        return qs


class GalleryAdmin(object):
    list_display = ['id', 'title', 'category', 'rank_num', 'is_published']
    fields = ('category', 'title', 'thumbnail', 'rank_num', 'is_published')
    list_editable = ('title', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-honors', lang='zh')
        return super(GalleryAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(GalleryAdmin, self).queryset()
        qs = qs.filter(category__full_name='achievements-honors', category__lang='zh')
        return qs


class GalleryAdmin_en(object):
    list_display = ['id', 'title', 'category', 'rank_num', 'is_published']
    fields = ('category', 'title', 'thumbnail', 'rank_num', 'is_published')
    list_editable = ('title', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='achievements-honors', lang='en')
        return super(GalleryAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(GalleryAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='achievements-honors', category__lang='en')
        return qs


class StaffFacultyAdmin(object):
    """
    教师
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    # formfield_overrides = {
    #     models.TextField: {'style': 'width:'}
    # }

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='zh')
        return super(StaffFacultyAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffFacultyAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-faculty', category__lang='zh')
        return qs


class StaffFacultyAdmin_en(object):
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='en')
        return super(StaffFacultyAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffFacultyAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='staff-faculty', category__lang='en')
        return qs


class StaffPostgraduatesAdmin(object):
    """
    研究生
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='zh')
        return super(StaffPostgraduatesAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffPostgraduatesAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-postgraduates', category__lang='zh')
        return qs


class StaffPostgraduatesAdmin_en(object):
    """
    研究生
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='en')
        return super(StaffPostgraduatesAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffPostgraduatesAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='staff-postgraduates', category__lang='en')
        return qs


class StaffProfessorsAdmin(object):
    """
    访问教授
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='zh')
        return super(StaffProfessorsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffProfessorsAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-professors', category__lang='zh')
        return qs


class StaffProfessorsAdmin_en(object):
    """
    访问教授
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='en')
        return super(StaffProfessorsAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffProfessorsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='staff-professors', category__lang='en')
        return qs


class StaffExpertsAdmin(object):
    """
    特聘专家
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='zh')
        return super(StaffExpertsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffExpertsAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-experts', category__lang='zh')
        return qs


class StaffExpertsAdmin_en(object):
    """
    特聘专家
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='en')
        return super(StaffExpertsAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffExpertsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='staff-experts', category__lang='en')
        return qs


class StaffStudentsAdmin(object):
    """
    访问学生
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='zh')
        return super(StaffStudentsAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffStudentsAdmin, self).queryset()
        qs = qs.filter(category__full_name='staff-students', category__lang='zh')
        return qs


class StaffStudentsAdmin_en(object):
    """
    访问学生
    """
    list_display = ['id', 'name', 'title', 'title1', 'category', 'rank_num', 'is_published']
    fields = ('category', 'name', 'title', 'title1', 'thumbnail', 'introduce', 'rank_num', 'is_published', 'content')
    list_editable = ('title', 'title1', 'rank_num', 'is_published', 'category')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='staff', lang='en')
        return super(StaffStudentsAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(StaffStudentsAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='staff-students', category__lang='en')
        return qs


class AlumniAdmin(object):
    """
    学友风采
    """
    list_display = ['id', 'title', 'slug', 'rank_num']
    fields = ('category', 'title', 'slug', 'thumbnail', 'rank_num', 'writer', 'pub_date', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='alumni', lang='zh')
        return super(AlumniAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(AlumniAdmin, self).queryset()
        qs = qs.filter(category__full_name__startswith='alumni', category__lang='zh')
        return qs


class AlumniAdmin_en(object):
    """
    学友风采
    """
    list_display = ['id', 'title', 'slug', 'rank_num']
    fields = ('category', 'title', 'slug', 'thumbnail', 'rank_num', 'writer', 'pub_date', 'content')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name__startswith='alumni', lang='en')
        return super(AlumniAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(AlumniAdmin_en, self).queryset()
        qs = qs.filter(category__full_name__startswith='alumni', category__lang='en')
        return qs


class CalendarAdmin(object):
    list_display = ('id', 'lang', 'title', 'active_time', 'month', 'day', 'addr', 'rank_num')
    fields = ('lang', 'title', 'month', 'day', 'active_time', 'addr', 'url', 'rank_num', 'introduce', 'is_published')
    list_editable = ('title', 'active_time', 'month', 'day', 'addr', 'rank_num')


class FocusAdmin(object):
    list_display = ('id', 'lang', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('title', 'url', 'rank_num', 'is_published')


class LinksAdmin(object):
    list_display = ('id', 'title', 'url', 'rank_num', 'is_published')
    fields = ('category', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='friend-links', lang='zh')
        return super(LinksAdmin, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(LinksAdmin, self).queryset()
        qs = qs.filter(category__full_name='friend-links', category__lang='zh')
        return qs


class LinksAdmin_en(object):
    list_display = ('id', 'title', 'url', 'rank_num', 'is_published')
    fields = ('category', 'title', 'url', 'rank_num', 'is_published')
    list_editable = ('title', 'url', 'rank_num', 'is_published')

    def get_form_helper(self, *args, **kwargs):
        self.form_obj.fields['category'].queryset = Category.objects.filter(full_name='friend-links', lang='en')
        return super(LinksAdmin_en, self).get_form_helper(*args, **kwargs)

    def queryset(self):
        qs = super(LinksAdmin_en, self).queryset()
        qs = qs.filter(category__full_name='friend-links', category__lang='en')
        return qs


class PostAdmin(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin_en(object):
    list_display = ['id', 'title', 'slug', 'category', 'rank_num', ]
    prepopulated_fields = {'slug': ('title',)}


xadmin.site.register(SiteInfo, SiteInfoAdmin)

xadmin.site.register(Category, CategoryAdmin)

xadmin.site.register(Calendar, CalendarAdmin)
xadmin.site.register(Focus, FocusAdmin)

xadmin.site.register(Links, LinksAdmin)
xadmin.site.register(Links_en, LinksAdmin_en)

xadmin.site.register(SinglePage, SinglePageAdmin)
xadmin.site.register(SinglePage_en, SinglePageAdmin_en)

xadmin.site.register(News, NewsAdmin)
xadmin.site.register(TCMFTCNews, TCMFTCNewsAdmin)
xadmin.site.register(IndNews, IndNewsAdmin)
xadmin.site.register(News_en, NewsAdmin_en)
xadmin.site.register(TCMFTCNews_en, TCMFTCNewsAdmin_en)
xadmin.site.register(IndNews_en, IndNewsAdmin_en)

xadmin.site.register(Activity, ActivityAdmin)
xadmin.site.register(Activity_en, ActivityAdmin_en)

xadmin.site.register(Platform, PlatformAdmin)
xadmin.site.register(Projects, ProjectsAdmin)
xadmin.site.register(Achievement, AchievementAdmin)
xadmin.site.register(Platform_en, PlatformAdmin_en)
xadmin.site.register(Projects_en, ProjectsAdmin_en)
xadmin.site.register(Achievement_en, AchievementAdmin_en)

xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(Patents, PatentsAdmin)
xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(Articles_en, ArticlesAdmin_en)
xadmin.site.register(Patents_en, PatentsAdmin_en)
xadmin.site.register(Gallery_en, GalleryAdmin_en)

xadmin.site.register(StaffFaculty, StaffFacultyAdmin)
xadmin.site.register(StaffPostgraduates, StaffPostgraduatesAdmin)
xadmin.site.register(StaffProfessors, StaffProfessorsAdmin)
xadmin.site.register(StaffExperts, StaffExpertsAdmin)
xadmin.site.register(StaffStudents, StaffStudentsAdmin)
xadmin.site.register(StaffFaculty_en, StaffFacultyAdmin_en)
xadmin.site.register(StaffPostgraduates_en, StaffPostgraduatesAdmin_en)
xadmin.site.register(StaffProfessors_en, StaffProfessorsAdmin_en)
xadmin.site.register(StaffExperts_en, StaffExpertsAdmin_en)
xadmin.site.register(StaffStudents_en, StaffStudentsAdmin_en)

xadmin.site.register(Alumni, AlumniAdmin)
xadmin.site.register(Alumni_en, AlumniAdmin_en)

xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Post_en, PostAdmin_en)

xadmin.site.register(views.CommAdminView, GlobalSettings)
# admin.site.site_header = 'xcms'
