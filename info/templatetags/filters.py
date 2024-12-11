from django import template

register = template.Library()

@register.filter(name='filter_by_department')
def filter_by_department(value, args):
      return value.filter(department=int(args)).order_by('lastname')

@register.filter(name='filter_by_group')
def filter_by_group(value, args):
      return value.filter(group=int(args)).order_by('lastname')

@register.filter(name='is_used_group')
def is_used_group(value, args):
      count = value.filter(group=int(args)).count()
      return count > 0