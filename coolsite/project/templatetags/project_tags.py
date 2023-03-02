from django import template
from project.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return  Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('project/list_categories.html')
def show_categories(sort=None,category_selected=0):
    if not sort:
        categs = Category.objects.all()
    else:
        categs = Category.objects.order_by(sort)

    return {"categs":categs, "category_selected":category_selected}