from django import template
from datetime import date

register = template.Library()

@register.filter(name='is_urgent')
def is_urgent(deadline):
    if not deadline:
        return False
    days_left = (deadline - date.today()).days
    return 0 <= days_left <= 7