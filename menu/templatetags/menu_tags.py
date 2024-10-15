from django import template
from menu.models import Menu, MenuItem
from django.urls import reverse
from django.db.models import Prefetch

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    menu = Menu.objects.prefetch_related(
        Prefetch('items', queryset=MenuItem.objects.filter(parent=None))
    ).get(name=menu_name)

    return {
        'menu': menu,
        'current_url': current_url,
    }
