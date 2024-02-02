from django import template

register = template.Library()

@register.filter(name='capitalize_first')
def capitaliza_first(value):
    return value.capitalize()