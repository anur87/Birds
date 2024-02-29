from django import template
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
register = template.Library()

@register.filter(name='convert_date')

def convert_date(value):
    converted_date = value.strftime("%d.%m.%Y %H:%M")
    return converted_date

@register.filter(name='convert_to_other_date')

def convert_to_other_date(value):
    converted_date = value.strftime("%d %B %Y")
    return converted_date

@register.filter(name='convert_to_month')

def convert_to_month(value):
    converted_date = value.strftime("%B %Y")
    return converted_date