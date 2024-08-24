from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def loop_control(context, limit):
    context['loop_limit'] = limit
    return ''