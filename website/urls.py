from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [

    path('about/', views.about, name='about_index'),
    path('about/<slug>/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('contact-ok/', views.contact, name='contact_ok'),
    # path('contact/sendmail/', views.sendmail, name='contact_sendmail'),
    path('<parent_cate>/<cate_slug>/', views.list_page, name='list_page_index'),
    path('<parent_cate>/<cate_slug>/<int:page_num>/', views.list_page, name='list_page'),
    path('<parent_cate>/<cate_slug>/<pid>/<slug>/', views.article, name='article'),
    path('', views.index, name='index'),
]
