from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('about/us', views.about, name='about_index'),
    path('about/<page_name>', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('news/<pk>', views.news, name='news_detail'),
    path('events/', views.events, name='events'),
    path('events/<pk>', views.events, name='events_detail'),
    path('research/', views.research, name='research'),   # 项目研究
    path('achievement/', views.achievement, name='achievement'),   # 研究成果
    # path('exchange/', views.exchange, name='exchange'),     # 学术活动
    path('scholar/', views.scholar, name='scholar'),    # 学者
    path('schoolfellow/', views.schoolfellow, name='schoolfellow'),    # 学友风采
    path('exchange/<exchange_name>/', views.exchange_list, name='exchange'),
    path('<list_name>/p/<int:page_no>', views.common_list, name='common_list_page'),
    path('', views.index, name='index'),
]
