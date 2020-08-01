from django import template
from ..models import MenuType
register = template.Library()


@register.filter(name="resto_scrub")
def resto_scrub(text):
    if isinstance(text, MenuType):
        text = str(text)
    return text.lower().replace(' ', '_')
