from django import template
from django.template.defaultfilters import safe

from utils.money import format_money as money_formatter

register = template.Library()


@register.filter()
def format_money(money):
    return money_formatter(money)


@register.filter()
def format_money_html(money):
    return safe(money_formatter(money, html=True))
