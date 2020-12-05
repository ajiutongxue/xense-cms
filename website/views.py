from django.shortcuts import get_object_or_404, render
from .models import SinglePage, Article, Category


# Create your views here.

def index(request):
    print('index,,,,,,')
    return render(request, 'website/index.html')


def about(request, page_name='us'):
    # us - 中心简介
    # alliance - 联盟大学
    # course - 发展历程
    # honor - 中心荣誉
    page = get_object_or_404(SinglePage, slug=page_name, is_published=True)
    # print(request)
    sub_cate_list = SinglePage.objects.filter(category__slug='about').order_by('rank_num')    #all #objects #.get(slug='about')
    print(page.category.slug)
    context_data = {
        'page': page,
        # 'cate': 'about',
        'url_base': 'website:about',
        'sub_cate_list': sub_cate_list,
        'parent_link': 'website:about_index'
    }
    return render(request, 'website/single_page.html', {'context_data': context_data})


def news(request):
    cate = Category.objects.get(slug='news')
    news_list = Article.objects.all()
    context = {
        'news_list': news_list,
        'cate': cate
    }
    return render(request, 'website/news.html', context=context)


def events(request):
    cate = Category.objects.get(slug='events')
    news_list = Article.objects.all()
    context = {
        'news_list': news_list,
        'cate': cate
    }
    return render(request, 'website/news.html', context=context)


def research(request):
    return render(request, 'website/research.html')


def achievement(request):
    return render(request, 'website/research.html')


def scholar(request):
    return render(request, 'website/scholar.html')


def schoolfellow(request):
    return render(request, 'website/schoolfellow.html')


def contact(request):
    return render(request, 'website/contact.html')


def exchange_list(request, exchange_name):
    """ 可以通过参数和model相关数据来决定用哪个模板
    """
    return render(request, 'website/{0}.html'.format(exchange_name))
    # return render(request, 'website/a.html')
