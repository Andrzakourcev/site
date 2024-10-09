from django import template
import cars.views as views
from cars.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('cars/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('cars/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}