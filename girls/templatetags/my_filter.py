from django import template

register = template.Library()

@register.filter
def my_filter(value):
    value = value.replace("(", "\(")

    return value.replace(")","\)")