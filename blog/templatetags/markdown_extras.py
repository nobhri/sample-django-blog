from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import escape
from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    value     = escape(value)
    value = md.markdown(value, extensions=[
        'markdown.extensions.fenced_code',
        'extra',
        'markdown_checklist.extension'
    ])
    return value