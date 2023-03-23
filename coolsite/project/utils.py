from project.models import *


class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        categs = Category.objects.all()
        context['cats'] = categs
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context
