from django.template.defaultfilters import safe
from django_jinja import library

from utils.money import format_money as money_formatter


@library.filter()
def format_money(money):
    return money_formatter(money)


@library.filter()
def format_money_html(money):
    return safe(money_formatter(money, html=True))
