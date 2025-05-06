from django import template
from treemenu.models import MenuItem
from mptt.utils import get_cached_trees
register = template.Library()


@register.inclusion_tag('treemenu/menu_bootstrap.html', takes_context=True)
def show_menu(context):
    menu_items = get_cached_trees(MenuItem.objects.order_by('position'))
    return {
        "menu_items": menu_items,
        "user": context['request'].user
    }