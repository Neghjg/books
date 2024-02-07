from django import template
from books.models import Category


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Category.objects.all().order_by("-id")