from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """ 栏目的所有分类都应该通过这里创建，
        只有如此，才能对每个分类进行数据上的设置，比如顶上的图、列表用的模板等
    """
    # 栏目名称是表示这个单独的页面属于哪个栏目：关于我们、专家学者等等
    cate_name = models.CharField(max_length=100, verbose_name='栏目名称', null=True)
    # 该字段将描述地址中当前页面的上一级
    # e.g. xense.com/about/us
    # 这里写的就应该是 about
    slug = models.CharField(max_length=100, verbose_name='栏目名称简写', null=True)
    title = models.CharField(max_length=100, verbose_name='seo 标题', null=True)
    keyword = models.CharField(max_length=100, verbose_name='seo 关键字', null=True)
    description = models.CharField(max_length=300, verbose_name='seo 描述', null=True)
    # poster = models.ImageField(upload_to='cate_poster', null=True, verbose_name='顶部大图')
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '栏目'
        verbose_name_plural = '栏目列表'

    def __str__(self):
        return '{0} | {1}'.format(self.cate_name, self.slug)


# class SubCategory(models.Model):
#     cate_name = models.CharField(max_length=100, verbose_name='栏目名称', null=True)
#     slug = models.CharField(max_length=100, verbose_name='栏目名称简写', null=True)
#     rank_num = models.IntegerField(default=1, verbose_name='排序')
#     is_published = models.BooleanField(default=True, verbose_name='是否发布')
#
#     class Meta:
#         ordering = ['-rank_num']
#         verbose_name = '二级栏目'
#         verbose_name_plural = '二级栏目列表'
#
#     def __str__(self):
#         return '{0} | {1}'.format(self.cate_name, self.slug)


class SinglePage(models.Model):
    category = models.ForeignKey(Category, on_delete=None, null=True)
    page_title = models.CharField(max_length=100, verbose_name='页面')
    content = models.TextField(null=True, verbose_name='正文')
    slug = models.SlugField(null=True, verbose_name='页面名称简写')
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '单独页面'
        verbose_name_plural = '单独页面'

    def get_absolute_url(self):
        if self.category.slug == 'news':
            return reverse('website:news_detail', args=(self.id,))
        return reverse('about', kwargs={'slug': self.slug})

    def __str__(self):
        return self.page_title


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=None, null=True)
    title = models.CharField(max_length=200, verbose_name='标题')
    subhead = models.CharField(max_length=100, verbose_name='副标题')
    # thumbnail = models.ImageField(upload_to='news_thumbnail', null=True, verbose_name='缩略图')
    summary = models.CharField(null=True, max_length=300, verbose_name='摘要')
    writer = models.CharField(default='北京米亿礼仪培训', max_length=20, verbose_name='作者')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    rank_num = models.IntegerField(default=1, verbose_name='排序')

    def __str__(self):
        return self.title

    # 比如共用一个 list 模板的时候，这个就有用了，如果没个list都有自己的模板，这个没有意义
    def get_absolute_url(self):
        return reverse('website:news_detail', args=[self.id])

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '文章'
        verbose_name_plural = '文章'
