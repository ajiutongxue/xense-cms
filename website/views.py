from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Category, SinglePage, Post, SimplePost, Gallery, Staff, Focus, Calendar, SiteInfo
import math
from django.conf import settings
from django.core.mail import send_mail
from website.utils import x_get_page_tmpl, x_get_list_tmpl


# Create your views here.

zh_site_info = {}
try:
    zh_site_info = SiteInfo.objects.get(lang='zh')
except SiteInfo.DoesNotExist:
    pass


# en_site_info = SiteInfo.objects.get(lang='en')


def index(request):
    focus_list = Focus.objects.filter(is_published=True, lang='zh').order_by('-rank_num', '-id')
    activities = Post.objects.filter(
        category__full_name='activities-default',
        category__lang='zh',
        is_published=True
    ).order_by('-rank_num', '-id')[:3]
    calendars = Calendar.objects.filter(is_published=True, lang='zh').order_by('-rank_num', '-active_time', '-id')
    research_list = Post.objects.filter(category__full_name='research-platform', category__lang='zh',
                                        is_published=True).order_by('-rank_num', '-id')[:4]
    honor_list = list(range(6))
    _honor_list = Gallery.objects.filter(category__full_name='achievements-honors', category__lang='zh',
                                        is_published=True).order_by('-rank_num', '-id')[:6]
    # 控制实际显示的元素数量，数据不够将会留空
    _h_i = 0    # _honor_index
    for v in _honor_list:
        honor_list[_h_i] = v
        _h_i += 1
    friend_links = SimplePost.objects.filter(category__full_name='friend-links', category__lang='zh',
                                             is_published=True).order_by('-rank_num')
    context = {
        'focus_list': focus_list,
        'activities': activities,
        'calendars': calendars,
        'research_list': research_list,
        'honor_list': honor_list,
        'friend_links': friend_links,
        'zh_site_info': zh_site_info
    }
    return render(request, 'website/index.html', {'context': context})


def about(request, slug='introduction'):
    page = get_object_or_404(SinglePage, slug=slug)
    cate = Category.objects.get(full_name='single-about', lang='zh')
    tmpl = x_get_page_tmpl('default-article', cate, page)
    brother_cate_list = SinglePage.objects.filter(category__full_name='single-about', category__lang='zh').order_by(
        '-rank_num')
    context = {
        'page': page,
        'url_base': 'website:about',
        'brother_cate_list': brother_cate_list,
        'parent_link': 'website:about_index',
        'zh_site_info': zh_site_info
    }
    return render(request, 'website/{}.html'.format(tmpl), {'context': context})


def contact(request):
    page = get_object_or_404(SinglePage, slug='contact')
    cate = Category.objects.get(full_name='single-contact', lang='zh')
    tmpl = x_get_page_tmpl('tmpl-contact', cate, page)
    brother_cate_list = SinglePage.objects.filter(category__full_name='single-contact', category__lang='zh').order_by(
        '-rank_num')
    context = {
        'page': page,
        'url_base': 'website:contact',
        'brother_cate_list': brother_cate_list,
        'zh_site_info': zh_site_info,
        'send_status': 'NO'
    }
    if request.method == 'POST':
        title = request.POST['title']
        cate = '合作交流' if int(request.POST['cate']) == 1 else '意见建议'
        uname = request.POST['uname']
        tel = request.POST['tel']
        content = request.POST['content']
        msg = '主题：{}\n分类：{}\n如何称呼：{}\n联系方式：{}\n正文：{}'.format(title, cate, uname, tel, content)
        # html_message = ''.format(request.POST['content'])
        email_from = settings.EMAIL_FORM
        linkman = ['yang_tao_cn@163.com']
        if zh_site_info.email:
            linkman.append(zh_site_info.email)
        # 发送邮件
        try:
            send_mail(title, msg, email_from, linkman)
            context['send_status'] = 'OK'
        except:
            context['send_status'] = 'ERR'
    return render(request, 'website/{}.html'.format(tmpl), {'context': context})


# def contact_ok(request):
#     page = get_object_or_404(SinglePage, slug='contact')
#     cate = Category.objects.get(full_name='single-contact', lang='zh')
#     tmpl = x_get_page_tmpl('tmpl-contact', cate, page)
#     brother_cate_list = SinglePage.objects.filter(category__full_name='single-contact', category__lang='zh').order_by(
#         '-rank_num')
#
#     context = {
#         'page': page,
#         'url_base': 'website:contact',
#         'brother_cate_list': brother_cate_list,
#         'zh_site_info': zh_site_info,
#         'send_ok': True
#     }
#     return render(request, 'website/{}.html'.format(tmpl), {'context': context})
#
#
# def sendmail(request):
#     title = request.POST['title']
#     cate = '合作交流' if int(request.POST['cate']) == 1 else '意见建议'
#     uname = request.POST['uname']
#     tel = request.POST['tel']
#     content = request.POST['content']
#     msg = '主题：{}\n分类：{}\n如何称呼：{}\n联系方式：{}\n正文：{}'.format(title, cate, uname, tel, content)
#     # html_message = ''.format(request.POST['content'])
#     email_from = settings.EMAIL_FORM
#     linkman = ['yang_tao_cn@163.com']
#     if zh_site_info.email:
#         linkman.append(zh_site_info.email)
#     # 发送邮件
#     send_mail(title, msg, email_from, linkman)
#     # return HttpResponse("ok")
#     page = get_object_or_404(SinglePage, slug='contact')
#     cate = Category.objects.get(full_name='single-contact', lang='zh')
#     tmpl = x_get_page_tmpl('tmpl-contact', cate, page)
#     brother_cate_list = SinglePage.objects.filter(category__full_name='single-contact', category__lang='zh').order_by(
#         '-rank_num')
#
#     context = {
#         'page': page,
#         'url_base': 'website:contact',
#         'brother_cate_list': brother_cate_list,
#         'zh_site_info': zh_site_info,
#         'send_ok': True
#     }
#     return render(request, 'website/{}.html'.format(tmpl), {'context': context})
#     # return HttpResponseRedirect(reverse('website:contact_ok'))


# path('<parent_cate>/<cate_slug>/<int:page_no>/', views.list_page, name='list_page'),
def list_page(request, parent_cate, cate_slug, page_num=1):
    cate = Category.objects.get(slug=cate_slug, lang='zh')
    tmpl = x_get_list_tmpl('tmpl-list', cate)
    brother_cate_list = Category.objects.filter(full_name__startswith=parent_cate, lang='zh').order_by('-rank_num')
    # print(brother_cate_list.first())
    count_per_page = cate.page_count
    if cate.full_name == 'research-projects' or cate.full_name == 'achievements-articles' or cate.full_name == 'achievements-patents':
        _M = SimplePost
    elif cate.full_name == 'achievements-honors':
        _M = Gallery
    elif cate.full_name[0:5] == 'staff':
        _M = Staff
    else:
        _M = Post
    total_count = _M.objects.filter(category__full_name=cate.full_name, category__lang='zh', is_published=True).count()
    page_num = int(page_num)  # 当前页码
    count_all_page = int(math.ceil(total_count / count_per_page))  # 列表页数
    articles = _M.objects.filter(
        category__full_name=cate.full_name,
        category__lang='zh',
        is_published=True
    ).order_by('-rank_num', '-id')[count_per_page * (page_num - 1):count_per_page * page_num]
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
        'zh_site_info': zh_site_info
    }
    return render(request, 'website/{}.html'.format(tmpl), {'context': context})


# path('<parent_cate>/<cate_slug>/p/<pid>-<slug>/', views.article, name='article'),
def article(request, parent_cate, cate_slug, pid, slug):
    _M = Post
    if parent_cate == 'staff':
        _M = Staff
    page = get_object_or_404(_M, id=pid, is_published=True)
    # tmpl = 'tmpl-post'
    if parent_cate == 'staff':
        tmpl = 'tmpl-staff'
    else:
        tmpl = x_get_page_tmpl('tmpl-post', page.category, page)
    relative_list = Post.objects.filter(category__full_name=page.category.full_name, category__lang='zh',
                                        is_published=True).order_by('-rank_num', '-id').exclude(id=pid)[:6]
    context = {
        'article': page,
        # 'brother_cate_list': brother_cate_list,
        'relative_list': relative_list,
        'url_base': "website:list_page_index 'parent_cate':{0} 'cate_slug':{1}".format(parent_cate, cate_slug),
        'zh_site_info': zh_site_info
    }
    return render(request, 'website/{}.html'.format(tmpl), {'context': context})
