from django.db import models
from django.utils import timezone
from django.urls import reverse
from xcms.storage import ImageStorage


# Create your models here.


class AbsPost(models.Model):
    """
    通用图文文章
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='标题', blank=False, null=True)
    subhead = models.CharField(max_length=100, verbose_name='副标题', blank=True, null=True)
    url = models.CharField(max_length=100, verbose_name='链接', blank=True, null=True)
    slug = models.CharField(max_length=100, null=False, verbose_name='url 优化', blank=True)
    thumbnail = models.ImageField(upload_to='post_thumbnail', storage=ImageStorage(), null=True,
                                  help_text='图片尺寸：300x150', blank=True, verbose_name='缩略图')
    summary = models.TextField(max_length=150, verbose_name='摘要', null=True, blank=True, help_text='中文字数 50 个左右较好')
    content = models.TextField(blank=True, null=True, verbose_name='正文')
    writer = models.CharField(default='未来交通研究中心', max_length=20, verbose_name='来源')
    pub_date = models.DateField(default=timezone.now, verbose_name='发布时间')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    custom_tmpl = models.CharField(max_length=50, verbose_name='页面模版', blank=True, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['rank_num', 'id']
        abstract = True


CATE_TMPL_CHOICES = (
    ('DONT-USE', '使用默认'),
    ('tmpl-list-1', '图文列表模版1'),
    ('tmpl-list-2', '图文列表模版2'),
    ('tmpl-list-3-no-thumb', '文字列表模版1'),
    ('tmpl-list-4-simple', '文字列表模版2（无详情页）'),
    ('tmpl-list-5-simple', '文字列表模版3（论文）'),
    ('tmpl-list-6-staff', '人员档案列表1'),
    ('tmpl-list-7-gallery', '图片列表（无详情）'),
)

ARTICLE_TMPL_CHOICES = (
    ('DONT-USE', '使用默认'),
    ('tmpl-post-1', '新闻资讯模版1'),
    ('tmpl-post-2', '新闻资讯模版2'),
    ('tmpl-single', '独立文章模版'),
    ('tmpl-single-1', '独立文章模版1'),
    ('tmpl-contact', '联系方式模版'),
)


class Category(models.Model):
    """
    栏目的所有分类都应该通过这里创建，
    只有如此，才能对每个分类进行数据上的设置，比如顶上的图、列表用的模板等
    """
    id = models.AutoField(primary_key=True)
    # parent_cate = models.ForeignKey('self', verbose_name='上级栏目', on_delete=None, blank=True, null=True)
    parent_name = models.CharField(max_length=100, verbose_name='上级栏目名称', blank=True, null=True)
    parent_name_en = models.CharField(max_length=100, verbose_name='上级栏目名称 en', blank=True, null=True)
    # 栏目名称是表示这个单独的页面属于哪个栏目：关于我们、专家学者等等
    cate_name = models.CharField(max_length=100, verbose_name='栏目名称', blank=True, null=True)
    cate_name_en = models.CharField(max_length=100, verbose_name='栏目名称 en', blank=True, null=True)
    full_name = models.CharField(max_length=100, verbose_name='栏目英文全名', blank=False, null=False)
    # 该字段将描述地址中当前页面的上一级
    # e.g. xense.com/about/us
    # 这里写的就应该是 about
    slug = models.CharField(max_length=100, verbose_name='slug', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='seo 标题', blank=True, null=True)
    keyword = models.CharField(max_length=100, verbose_name='seo 关键字', blank=True, null=True)
    description = models.CharField(max_length=300, verbose_name='seo 描述', blank=True, null=True)
    title_en = models.CharField(max_length=100, verbose_name='seo 标题 en', blank=True, null=True)
    keyword_en = models.CharField(max_length=100, verbose_name='seo 关键字 en', blank=True, null=True)
    description_en = models.CharField(max_length=300, verbose_name='seo 描述 en', blank=True, null=True)
    # poster = models.ImageField(upload_to='cate_poster', null=True, verbose_name='顶部大图')
    page_count = models.IntegerField(default=20, verbose_name='每页文章条数')
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    default_self_template = models.CharField(default='DONT-USE', max_length=30, choices=CATE_TMPL_CHOICES,
                                             verbose_name='默认列表模版', blank=True, null=True)
    # 如果为 True，则模版文件夹下应该有一个和 slug-list 同名的模版文件，默认使用 default-list
    # 并不灵活，因为一个网站中的列表页形式本来就可能有几种，和栏目之间相当于一种多对多的关系，所以模版改为指定模版名
    # is_self_template = models.BooleanField(default=False, verbose_name='使用定制栏目模版')
    self_template = models.CharField(max_length=30, verbose_name='指定列表模版', blank=True, null=True)
    default_article_self_template = models.CharField(default='DONT-USE', max_length=30, choices=ARTICLE_TMPL_CHOICES,
                                                     verbose_name='默认文章模版', blank=True, null=True)
    # 如果为 True，则模版文件夹下应该有一个 ${slug}-article 的模版文件，默认使用 default-article
    # 文章模版和列表模版一样，都通过指定具体的来设置
    # is_article_self_template = models.BooleanField(default=False, verbose_name='文章使用定制模版')
    article_self_template = models.CharField(max_length=30, verbose_name='指定文章模版', blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='是否发布')

    # todo: 看img 标签是否支持 onerror 之类属性，否则，这里可能需要设置一个上面那样的开关指定页面顶上的大图

    def get_absolute_url(self):
        parent_slug = self.full_name.split('-')[0]
        return reverse(
            'website:list_page_index',
            args=[parent_slug, self.slug]
        )

    class Meta:
        ordering = ['-rank_num', 'id']
        verbose_name = '栏目'
        verbose_name_plural = '栏目列表'

    def __str__(self):
        parent_name = ''
        if self.parent_name is not None:
            parent_cate = '[' + self.parent_name + '] '
        return '{0}{1} | {2} | {3}'.format(parent_name, self.cate_name, self.slug, self.full_name)


class SimplePost(models.Model):
    category = models.ForeignKey(Category, verbose_name='栏目', on_delete=None, blank=False, null=False)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='标题', blank=False, null=True)
    url = models.CharField(max_length=100, verbose_name='链接', blank=True, null=True)
    msg1 = models.CharField(max_length=100, verbose_name='信息1', help_text='显示在右侧的信息，需要填入完整显示内容，如："委托方：清华大学" ',
                            blank=True, null=True)
    msg2 = models.CharField(max_length=100, verbose_name='信息2', help_text='显示在右侧的信息，需要填入完整显示内容', blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    rank_num = models.IntegerField(default=1, verbose_name='排序')


class Links(SimplePost):
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
        proxy = True


class Gallery(models.Model):
    category = models.ForeignKey(Category, verbose_name='栏目', on_delete=None, blank=False, null=False)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='标题', blank=True, null=True)
    url = models.CharField(max_length=100, verbose_name='链接', blank=True, null=True)
    msg = models.CharField(max_length=200, verbose_name='信息', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='gallery_thumbnail', storage=ImageStorage(), null=True,
                                  help_text='建议图片尺寸：300x180', blank=True, verbose_name='缩略图')
    big_pic = models.ImageField(upload_to='gallery_thumbnail', storage=ImageStorage(), null=True, blank=True,
                                verbose_name='图片')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    rank_num = models.IntegerField(default=1, verbose_name='排序')

    class Meta:
        verbose_name = '荣誉奖励'
        verbose_name_plural = '荣誉奖励'


class Post(AbsPost):
    category = models.ForeignKey(Category, verbose_name='栏目', on_delete=None, blank=False, null=False)

    def get_absolute_url(self):
        parent_slug = self.category.full_name.split('-')[0]
        return reverse(
            'website:article',
            args=[parent_slug, self.category.slug, self.id, self.slug if self.slug else '0']
        )

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class SinglePage(Post):
    """
    关于我们、联系方式
    """

    class Meta:
        verbose_name = '单独页面'
        verbose_name_plural = '单独页面'
        proxy = True


class Staff(models.Model):
    """
    职员档案
    """
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, verbose_name='栏目', on_delete=None, blank=False, null=False)
    name = models.CharField(max_length=60, verbose_name='姓名', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='职位', blank=True, null=True)
    title1 = models.CharField(max_length=100, verbose_name='职位1', blank=True, null=True)
    title2 = models.CharField(max_length=100, verbose_name='职位2', blank=True, null=True)
    slug = models.CharField(max_length=200, null=False, verbose_name='url 优化', blank=True)
    thumbnail = models.ImageField(upload_to='staff_thumbnail', blank=True, verbose_name='照片', help_text='图片：320 x 400')
    introduce = models.TextField(max_length=300, verbose_name='简介', null=True, blank=True)
    content = models.TextField(blank=True, null=True, verbose_name='正文')
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')

    class Meta:
        ordering = ['-rank_num']
        verbose_name = '师资力量'
        verbose_name_plural = '师资力量'


class SiteInfo(models.Model):
    lang = models.CharField(max_length=100, primary_key=True, verbose_name='语言版本', choices=(
        ('en', '英语 English'),
        ('zh', '中文 Chinese')
    ))
    title = models.CharField(max_length=100, verbose_name='网站名称', blank=True, null=True)
    keywords = models.TextField(max_length=200, verbose_name='关键字', blank=True, null=True, help_text='使用","分隔')
    description = models.TextField(max_length=200, verbose_name='网站描述', blank=True, null=True)
    logo = models.ImageField(upload_to='site_img', blank=True, verbose_name='logo',
                             help_text='通常自适应设计网站，logo根据需要也会有形式的变化')
    logo1 = models.ImageField(upload_to='site_img', blank=True, verbose_name='logo1',
                              help_text='通常自适应设计网站，logo根据需要也会有形式的变化')
    sign_code = models.CharField(max_length=30, verbose_name='备案号', blank=True, null=True)
    linkman = models.CharField(max_length=100, verbose_name='联系人', blank=True, null=True)
    copy = models.CharField(max_length=100, verbose_name='版权信息', blank=True, null=True)
    addr = models.CharField(max_length=100, verbose_name='地址', blank=True, null=True)
    qr = models.ImageField(upload_to='site_img', blank=True, verbose_name='微信二维码')
    tel = models.CharField(max_length=100, verbose_name='电话', blank=True, null=True)
    tel1 = models.CharField(max_length=100, verbose_name='电话1', blank=True, null=True)
    email = models.CharField(max_length=100, verbose_name='邮箱', blank=True, null=True)
    is_used = models.BooleanField(default=True, verbose_name='是否生效')

    class Meta:
        verbose_name = '网站基本信息'
        verbose_name_plural = '网站基本信息'

    def __str__(self):
        return '{} 版本设置'.format(self.lang)


class Calendar(models.Model):
    """
    活动日历
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='标题', blank=True, null=True)
    active_time = models.DateTimeField(verbose_name='活动时间', blank=True, null=True)
    month = models.CharField(max_length=10, verbose_name='月简写', blank=False, help_text='如：Jnm.')
    addr = models.CharField(max_length=100, verbose_name='活动地点', blank=False)
    day = models.IntegerField(verbose_name='日', blank=False)
    url = models.CharField(max_length=100, verbose_name='链接到', blank=True, null=True)
    introduce = models.TextField(max_length=300, verbose_name='简介', null=True, blank=True)
    rank_num = models.IntegerField(default=1, verbose_name='排序')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')

    class Meta:
        ordering = ['-rank_num', '-active_time']
        verbose_name = '活动日历'
        verbose_name_plural = '活动日历'


class Focus(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(null=True, verbose_name='摘要')
    rank_num = models.IntegerField(default=1, verbose_name='排序', help_text='数字大的在前面')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    url = models.CharField(max_length=128, default='', verbose_name='链接到')
    focus_img = models.ImageField(upload_to='focus', storage=ImageStorage(), default='', verbose_name='图片',
                                  help_text='尺寸：1600 x 560')

    class Meta:
        ordering = ['-is_published', '-rank_num']
        verbose_name = '焦点图'
        verbose_name_plural = '焦点图列表'


class News(Post):
    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'
        proxy = True


class TCMFTCNews(Post):
    class Meta:
        verbose_name = '中心动态'
        verbose_name_plural = '中心动态'
        proxy = True


class IndNews(Post):
    class Meta:
        verbose_name = '行业动态'
        verbose_name_plural = '行业动态'
        proxy = True


class Activity(Post):
    class Meta:
        verbose_name = '学术活动'
        verbose_name_plural = '学术活动'
        proxy = True


class Platform(Post):
    class Meta:
        verbose_name = '研究平台'
        verbose_name_plural = '研究平台'
        proxy = True


class Projects(SimplePost):
    class Meta:
        verbose_name = '研究项目'
        verbose_name_plural = '研究项目'
        proxy = True


class Achievement(Post):
    class Meta:
        verbose_name = '成果转化'
        verbose_name_plural = '成果转化'
        proxy = True


class Articles(SimplePost):
    class Meta:
        verbose_name = '科学论文'
        verbose_name_plural = '科学论文'
        proxy = True


class Patents(SimplePost):
    class Meta:
        verbose_name = '发明专利'
        verbose_name_plural = '发明专利'
        proxy = True


class StaffFaculty(Staff):
    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师'
        proxy = True


class StaffPostgraduates(Staff):
    class Meta:
        verbose_name = '研究生'
        verbose_name_plural = '研究生'
        proxy = True


class StaffProfessors(Staff):
    class Meta:
        verbose_name = '访问教授'
        verbose_name_plural = '访问教授'
        proxy = True


class StaffExperts(Staff):
    class Meta:
        verbose_name = '特聘专家'
        verbose_name_plural = '特聘专家'
        proxy = True


class StaffStudents(Staff):
    class Meta:
        verbose_name = '访问学生'
        verbose_name_plural = '访问学生'
        proxy = True


class Alumni(Post):
    class Meta:
        verbose_name = '学友风采'
        verbose_name_plural = '学友风采'
        proxy = True
