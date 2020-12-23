__author__ = '秋轩'

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def qgw(a1,a2):
    return a1 + a2

@register.filter
def Ls(a1,a2):
    return  a1 + a2