from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from website.models import Category, SinglePage_en, Post_en, SimplePost_en, Gallery_en, Staff_en, Focus, Calendar, SiteInfo
import math
from django.conf import settings
from django.core.mail import send_mail


def _get_page_tmpl(default_tmpl, category, page):
    tmpl = default_tmpl
    if category.default_article_self_template != 'DONT-USE':
        tmpl = category.default_article_self_template
    if category.article_self_template and category.article_self_template.strip():
        tmpl = category.article_self_template
    if page.custom_tmpl and page.custom_tmpl.strip():
        tmpl = page.custom_tmpl
    return tmpl


# Create your views here.

# en_site_info = SiteInfo.objects.get(lang='en')
en_site_info = SiteInfo.objects.get(lang='en')


def index(request):
    focus_list = Focus.objects.filter(is_published=True, lang='en').order_by('-rank_num')
    activities = Post_en.objects.filter(
        category__full_name='activities-default',
        category__lang='en',
        is_published=True
    ).order_by('-rank_num')[:3]
    calendars = Calendar.objects.filter(is_published=True, lang='en').order_by('-rank_num', '-active_time')
    research_list = Post_en.objects.filter(category__full_name='research-platform',category__lang='en', is_published=True).order_by('-rank_num', '-pub_date')[:4]
    honor_list = Gallery_en.objects.filter(category__full_name='achievements-honors',category__lang='en', is_published=True).order_by('-rank_num')[:4]
    friend_links = SimplePost_en.objects.filter(category__full_name='friend-links',category__lang='en', is_published=True).order_by('-rank_num')

    print('sssssssssss')
    print(en_site_info)

    context = {
        'focus_list': focus_list,
        'activities': activities,
        'calendars': calendars,
        'research_list': research_list,
        'honor_list': honor_list,
        'friend_links': friend_links,
        'en_site_info': en_site_info
    }
    return render(request, 'website_en/index.html', {'context': context})


def about(request, slug='introduction'):
    page = get_object_or_404(SinglePage_en, slug=slug)
    cate = Category.objects.get(full_name='single-about', lang='en')
    tmpl = _get_page_tmpl('default-article', cate, page)
    brother_cate_list = SinglePage_en.objects.filter(category__full_name='single-about', category__lang='en').order_by('-rank_num')
    context = {
        'page': page,
        'url_base': 'website_en:about',
        'brother_cate_list': brother_cate_list,
        'parent_link': 'website_en:about_index',
        'en_site_info': en_site_info
    }
    return render(request, 'website_en/{}.html'.format(tmpl), {'context': context})


def contact(request):
    page = get_object_or_404(SinglePage_en, slug='contact')
    cate = Category.objects.get(full_name='single-contact', lang='en')
    tmpl = _get_page_tmpl('tmpl-contact', cate, page)
    brother_cate_list = SinglePage_en.objects.filter(category__full_name='single-contact', category__lang='en').order_by('-rank_num')

    context = {
        'page': page,
        'url_base': 'website_en:contact',
        'brother_cate_list': brother_cate_list,
        'en_site_info': en_site_info,
    }
    return render(request, 'website_en/{}.html'.format(tmpl), {'context': context})


def contact_ok(request):
    page = get_object_or_404(SinglePage_en, slug='contact')
    cate = Category.objects.get(full_name='single-contact', lang='en')
    tmpl = _get_page_tmpl('tmpl-contact', cate, page)
    brother_cate_list = SinglePage_en.objects.filter(category__full_name='single-contact', category__lang='en').order_by('-rank_num')

    context = {
        'page': page,
        'url_base': 'website_en:contact',
        'brother_cate_list': brother_cate_list,
        'en_site_info': en_site_info,
        'send_ok': True
    }
    return render(request, 'website_en/{}.html'.format(tmpl), {'context': context})


def sendmail(request):
    title = request.POST['title']
    cate = '合作交流' if int(request.POST['cate']) == 1 else '意见建议'
    uname = request.POST['uname']
    tel = request.POST['tel']
    content = request.POST['content']
    msg = '主题：{}\n分类：{}\n如何称呼：{}\n联系方式：{}\n正文：{}'.format(title, cate, uname, tel, content)
    # html_message = ''.format(request.POST['content'])
    email_from = settings.EMAIL_FORM
    linkman = ['yang_tao_cn@163.com', '85103350@qq.com']
    # 发送邮件
    send_mail(title, msg, email_from, linkman)
    # return HttpResponse("ok")
    page = get_object_or_404(SinglePage_en, slug='contact')
    cate = Category.objects.get(full_name='single-contact', lang='en')
    tmpl = _get_page_tmpl('tmpl-contact', cate, page)
    brother_cate_list = SinglePage_en.objects.filter(category__full_name='single-contact', category__lang='en').order_by('-rank_num')

    context = {
        'page': page,
        'url_base': 'website_en:contact',
        'brother_cate_list': brother_cate_list,
        'en_site_info': en_site_info,
        'send_ok': True
    }
    return render(request, 'website_en/{}.html'.format(tmpl), {'context': context})
    # return HttpResponseRedirect(reverse('website_en:contact_ok'))


# path('<parent_cate>/<cate_slug>/<int:page_no>/', views.list_page, name='list_page'),
def list_page(request, parent_cate, cate_slug, page_num=1):
    cate = Category.objects.get(slug=cate_slug, lang='en')
    tmpl = 'tmpl-list'
    if cate.default_self_template != 'DONT-USE':
        tmpl = cate.default_self_template
    if cate.self_template and cate.self_template.strip():
        tmpl = cate.self_template
    brother_cate_list = Category.objects.filter(full_name__startswith=parent_cate, lang='en').order_by('-rank_num')
    # print(brother_cate_list.first())
    count_per_page = cate.page_count
    if cate.full_name == 'research-projects' or cate.full_name == 'achievements-articles' or cate.full_name == 'achievements-patents':
        _M = SimplePost_en
    elif cate.full_name == 'achievements-honors':
        _M = Gallery_en
    elif cate.full_name[0:5] == 'staff':
        _M = Staff_en
    else:
        _M = Post_en
    total_count = _M.objects.filter(category__full_name=cate.full_name, is_published=True).count()
    page_num = int(page_num)  # 当前页码
    count_all_page = int(math.ceil(total_count / count_per_page))  # 列表页数
    articles = _M.objects.filter(
        category__full_name=cate.full_name,
        category__lang='en',
        is_published=True
    ).order_by('-rank_num')[count_per_page * (page_num - 1):count_per_page * page_num]
    prev_num = page_num - 1 if page_num >= 1 else 0
    next_num = page_num + 1 if page_num < count_all_page else 0
    num_list = range(1, count_all_page + 1)  # 所有页码的序号
    context = {
        'brother_cate_list': brother_cate_list,
        'articles': articles,
        'parent_cate': parent_cate,
        'cate': cate,
        'page_num': page_num,
        'count_all_page': count_all_page,
        'num_list': num_list,
        'prev_num': prev_num,
        'next_num': next_num,
        'en_site_info': en_site_info
    }
    return render(request, 'website_en/{}.html'.format(tmpl), {'context': context})


# path('<parent_cate>/<cate_slug>/p/<pid>-<slug>/', views.article, name='article'),
def article(request, parent_cate, cate_slug, pid, slug):
    page = get_object_or_404(Post_en, id=pid, is_published=True)
    tmpl = _get_page_tmpl('tmpl-post', page.category, page)
    relative_list = Post_en.objects.filter(category__full_name=page.category.full_name, category__lang='en', is_published=True).exclude(id=pid)[
                    :6]
    context = {
        'article': page,
        # 'brother_cate_list': brother_cate_list,
        'relative_list': relative_list,
        'url_base': "website_en:list_page_index 'parent_cate':{0} 'cate_slug':{1}".format(parent_cate, cate_slug),
        'en_site_info': en_site_info,
        'parent_cate': parent_cate
    }
    return render(request, 'website_en/{}.html'.format(tmpl), {'context': context})

