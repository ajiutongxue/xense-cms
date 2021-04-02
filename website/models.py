from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q


# Create your models here.

class CommonPost(models.Model):
    """
    通用图文文章
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='标题', blank=True, null=True)
    subhead = models.CharField(max_length=100, verbose_name='副标题', blank=True, null=True)
    slug = models.CharField(max_length=200, null=False, verbose_name='url 优化', blank=True)
    thumbnail = models.ImageField(upload_to='post_thumbnail', blank=True, verbose_name='缩略图')
    summary = models.CharField(max_length=300, verbose_name='摘要', null=True, blank=True)
    content = models.TextField(null=True, verbose_name='正文')
    writer = models.CharField(default='未来交通', max_length=20, verbose_name='作者')
    pub_date = models.DateField(default=timezone.now, verbose_name='发布时间')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    rank_num = models.IntegerField(default=1, verbose_name='排序')

    class Meta:
        ordering = ['-rank_num']
        abstract = True


class CommonStaff(models.Model):
    """
    通用职员档案
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='姓名', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='职位1', blank=True, null=True)
    title2 = models.CharField(max_length=100, verbose_name='职位2', blank=True, null=True)
    slug = models.CharField(max_length=200, null=False, verbose_name='url 优化', blank=True)
    thumbnail = models.ImageField(upload_to='staff_thumbnail', blank=True, verbose_name='照片')
    introduce = models.CharField(max_length=300, verbose_name='简介', null=True, blank=True)
    rank_num = models.IntegerField(default=1, verbose_name='排序')

    class Meta:
        ordering = ['-rank_num']
        abstract = True


class Category(models.Model):
    """
    栏目的所有分类都应该通过这里创建，
    只有如此，才能对每个分类进行数据上的设置，比如顶上的图、列表用的模板等
    """
    id = models.AutoField(primary_key=True)
    parent_cate = models.ForeignKey('self', verbose_name='上级栏目', on_delete=None, blank=True, null=True)
    # 栏目名称是表示这个单独的页面属于哪个栏目：关于我们、专家学者等等
    cate_name = models.CharField(max_length=100, verbose_name='栏目名称', blank=True, null=True)
    full_name = models.CharField(max_length=100, verbose_name='栏目英文全名', blank=False, null=False)
    # 该字段将描述地址中当前页面的上一级
    # e.g. xense.com/about/us
    # 这里写的就应该是 about
    slug = models.CharField(max_length=100, verbose_name='slug', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='seo 标题', blank=True, null=True)
    keyword = models.CharField(max_length=100, verbose_name='seo 关键字', blank=True, null=True)
    description = models.CharField(max_length=300, verbose_name='seo 描述', blank=True, null=True)
    # poster = models.ImageField(upload_to='cate_poster', null=True, verbose_name='顶部大图')
    page_count = models.IntegerField(default=20, verbose_name='每页文章条数')
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    # 如果为 True，则模版文件夹下应该有一个和 slug-list 同名的模版文件，默认使用 default-list
    is_self_template = models.BooleanField(default=False, verbose_name='使用定制栏目模版')
    # 如果为 True，则模版文件夹下应该有一个 ${slug}-article 的模版文件，默认使用 default-article
    is_article_self_template = models.BooleanField(default=False, verbose_name='文章使用定制模版')
    # todo: 看img 标签是否支持 onerror 之类属性，否则，这里可能需要设置一个上面那样的开关指定页面顶上的大图
    is_published = models.BooleanField(default=True, verbose_name='是否发布')

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '栏目'
        verbose_name_plural = '栏目列表'

    def __str__(self):
        parent_cate = '[顶级] '
        if self.parent_cate is not None:
            parent_cate = '[' + self.parent_cate.slug + '] '
        return '{0}{1} | {2}'.format(parent_cate, self.cate_name, self.slug)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=None, blank=True,
                                 null=True)
    # category = models.ForeignKey(Category, limit_choices_to=Q(slug__startswith='news'), on_delete=None, blank=True,
    #                              null=True)
    title = models.CharField(max_length=200, verbose_name='标题', blank=True, null=True)
    subhead = models.CharField(max_length=100, verbose_name='副标题', blank=True, null=True)
    slug = models.CharField(max_length=200, null=False, verbose_name='url 优化', unique_for_date='pub_date', blank=True)
    # thumbnail = models.ImageField(upload_to='news_thumbnail', null=True, verbose_name='缩略图')
    summary = models.CharField(max_length=300, verbose_name='摘要', null=True, blank=True)
    content = models.TextField(null=True, verbose_name='正文')
    writer = models.CharField(default='未来交通', max_length=20, verbose_name='作者')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    custom_template = models.CharField(max_length=50, verbose_name='该文章使用的模版', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    rank_num = models.IntegerField(default=1, verbose_name='排序')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '文章'
        verbose_name_plural = '文章'

    # 比如共用一个 list 模板的时候，这个就有用了，如果没个list都有自己的模板，这个没有意义
    def get_absolute_url(self):
        return reverse(
            'website:article',
            args=[self.category.slug, self.id, self.slug if self.slug else '0']
        )


# 新闻动态 》 中心动态、行业动态
# 使用相同 model
class Post(CommonPost):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, limit_choices_to=Q(slug__startswith='news'), on_delete=None, blank=True,
                                 null=True)

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻列表'


# 学术活动 》所有子栏目都是用和 post 相同的model
class ActivityPost(CommonPost):
    category = models.ForeignKey(Category, limit_choices_to=Q(slug__startswith='activities'), on_delete=None, blank=True,
                                 null=True)
    custom_template = models.CharField(max_length=50, verbose_name='该文章使用的模版', null=True, blank=True)

    class Meta:
        verbose_name = '学术活动'
        verbose_name_plural = '学术活动'


class Alumni(CommonPost):
    category = models.ForeignKey(Category, limit_choices_to=Q(slug__startswith='alumni'), on_delete=None, blank=False, null=False)

    class Meta:
        verbose_name = '学友风采'
        verbose_name_plural = '学友风采'


class Staff(CommonStaff):
    category = models.ForeignKey(Category, limit_choices_to={'full_name__startswith': 'staff'}, on_delete=None, blank=False, null=False)

    class Meta:
        verbose_name = '师资力量'
        verbose_name_plural = '师资力量'


class SinglePage(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, limit_choices_to={'full_name__startswith': 'about'}, on_delete=None, blank=False, null=False)
    title = models.CharField(max_length=100, verbose_name='标题', blank=False, null=False)
    slug = models.CharField(max_length=50, null=False, verbose_name='url 优化', blank=False)
    content = models.TextField(null=True, verbose_name='正文')
    rank_num = models.IntegerField(default=1, verbose_name='排序')

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '关于中心'
        verbose_name_plural = '关于中心'
