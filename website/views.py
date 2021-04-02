from django.shortcuts import get_object_or_404, render
from .models import Article, Category, SinglePage


# Create your views here.

def index(request):
    print('index,,,,,,')
    return render(request, 'website/index.html')


def about(request, page_name='introduction'):
    page = get_object_or_404(SinglePage, slug=page_name)
    sub_cate_list = SinglePage.objects.filter(category__slug='about').order_by('-rank_num')
    context_data = {
        'page': page,
        'url_base': 'website:about',
        'sub_cate_list': sub_cate_list,
        'parent_link': 'website:about_index'
    }
    return render(request, 'website/single_page.html', {'context_data': context_data})


def contact(request, page_name='contact'):
    page = get_object_or_404(Article, slug=page_name, is_published=True)
    print('page::::')
    print(page)
    sub_cate_list = Article.objects.filter(category__slug='contact').order_by(
        'rank_num')  # all #objects #.get(slug='about')
    print('cate::::')
    print(sub_cate_list)
    context_data = {
        'page': page,
        'url_base': 'website:contact',
        'sub_cate_list': sub_cate_list,
        # 'parent_link': 'website:contact'
    }
    return render(request, 'website/single_page.html', {'context_data': context_data})


# def news(request):
#     cate = Category.objects.get(slug='news')
#     news_list = Article.objects.all()
#     context = {
#         'news_list': news_list,
#         'cate': cate
#     }
#     return render(request, 'website/list.html', context=context)


def list_page(request, list_name, page_no=1):
    print('here common_list')
    cate = Category.objects.get(slug=list_name)
    print(cate)
    list_tmpl = list_name if cate.is_self_template else 'default'
    articles = Article.objects.filter(category__slug=list_name, is_published=True).order_by('rank_num')
    print(articles)
    print(list_tmpl)
    context = {
        'articles': articles,
        'cate': cate
    }
    return render(request, 'website/{}-list.html'.format(list_tmpl), {'context': context})


# def common_article(request, list_name, pk):
#     article = get_object_or_404(Article, category__slug=list_name, slug=pk, is_published=True)
#     # page = Article.objects.filter(category__slug=list_name).get(slug=pk)
#     article_tmpl = list_name if article.category.is_article_self_template else 'default'
#     print('::::')
#     print(article.category.slug)
#     context = {
#         'article': article
#     }
#     return render(request, 'website/{}-article.html'.format(article_tmpl), {'context': context})


def article(request, list_name, pid, slug):
    a = get_object_or_404(
        Article, category__slug=list_name, id=pid, is_published=True
    )

    if a.slug and a.slug != slug:
        return render(request, 'website/404.html')

    article_tmpl = list_name if a.category.is_article_self_template else 'default'
    context = {
        'article': a
    }
    return render(request, 'website/{}-article.html'.format(article_tmpl), {'context': context})


def research(request):
    return render(request, 'website/research.html')


def achievement(request):
    return render(request, 'website/research.html')


def scholar(request):
    return render(request, 'website/scholar.html')


def schoolfellow(request):
    return render(request, 'website/schoolfellow.html')


# def contact(request):
#     return render(request, 'website/contact.html')


def exchange_list(request, exchange_name):
    """ 可以通过参数和model相关数据来决定用哪个模板
    """
    return render(request, 'website/{0}.html'.format(exchange_name))
    # return render(request, 'website/a.html')
