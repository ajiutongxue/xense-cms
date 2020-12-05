from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """ 栏目的所有分类都应该通过这里创建，
        只有如此，才能对每个分类进行数据上的设置，比如顶上的图、列表用的模板等
    """
    parent_cate = models.ForeignKey('self', verbose_name='上级栏目', on_delete=None, blank=True, null=True)
    # 栏目名称是表示这个单独的页面属于哪个栏目：关于我们、专家学者等等
    cate_name = models.CharField(max_length=100, verbose_name='栏目名称', blank=True, null=True)
    # 该字段将描述地址中当前页面的上一级
    # e.g. xense.com/about/us
    # 这里写的就应该是 about
    slug = models.CharField(max_length=100, verbose_name='栏目名称简写', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='seo 标题', blank=True, null=True)
    keyword = models.CharField(max_length=100, verbose_name='seo 关键字', blank=True, null=True)
    description = models.CharField(max_length=300, verbose_name='seo 描述', blank=True, null=True)
    # poster = models.ImageField(upload_to='cate_poster', null=True, verbose_name='顶部大图')
    page_count = models.IntegerField(default=20, verbose_name='每页文章条数')
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    # 如果为 True，则模版文件夹下应该有一个和 slug 同名的模版文件
    is_self_template = models.BooleanField(default=False, verbose_name='使用定制栏目模版')
    # 如果为 True，则模版文件夹下应该有一个 ${slug}_detail 的模版文件
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
    category = models.ForeignKey(Category, on_delete=None, blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='标题', blank=True, null=True)
    subhead = models.CharField(max_length=100, verbose_name='副标题', blank=True, null=True)
    slug = models.SlugField(null=True, verbose_name='页面名称简写', blank=True)
    # thumbnail = models.ImageField(upload_to='news_thumbnail', null=True, verbose_name='缩略图')
    summary = models.CharField(max_length=300, verbose_name='摘要', null=True, blank=True)
    content = models.TextField(null=True, verbose_name='正文')
    writer = models.CharField(default='未来交通', max_length=20, verbose_name='作者')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    custom_template = models.CharField(max_length=50, verbose_name='该文章使用的模版', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    rank_num = models.IntegerField(default=1, verbose_name='排序')

    def __str__(self):
        return self.title

    # # 比如共用一个 list 模板的时候，这个就有用了，如果没个list都有自己的模板，这个没有意义
    # def get_absolute_url(self):
    #     return reverse('website:news_detail', args=[self.id])

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '文章'
        verbose_name_plural = '文章'
