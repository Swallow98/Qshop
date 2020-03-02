from django import template
register = template.Library()
@register.filter(name='add_yang')
def add_x(arg):
    a = float(arg+10)
    return round(a,2)