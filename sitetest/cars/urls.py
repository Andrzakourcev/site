from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000
    path(r"about/", views.about,name='about'), #http://127.0.0.1:8000/about
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('additionally', views.additionally, name='additionally'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),

]