from django import template
from ..models import Event

register = template.Library()


@register.simple_tag(name="tag_events")
def get_events():
    return Event.objects.all()
