from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [

    # -- 定制路由 --
    path('about/', views.about, name='about_index'),
    path('about/<page_name>/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('research/', views.research, name='research'),   # 项目研究
    path('achievement/', views.achievement, name='achievement'),   # 研究成果
    # path('exchange/', views.exchange, name='exchange'),     # 学术活动
    path('scholar/', views.scholar, name='scholar'),    # 学者
    path('schoolfellow/', views.schoolfellow, name='schoolfellow'),    # 学友风采
    path('exchange/<exchange_name>/', views.exchange_list, name='exchange'),
    # -- end --

    # -- url map ---
    # 新闻动态
    # - news/events   中心动态
    # - news/industry   行业动态

    path('p/<list_name>-<pid>-<slug>/', views.article, name='article'),
    path('<list_name>/', views.list_page, name='list_page_index'),
    path('<list_name>/<int:page_no>/', views.list_page, name='list_page'),
    path('', views.index, name='index'),
]
