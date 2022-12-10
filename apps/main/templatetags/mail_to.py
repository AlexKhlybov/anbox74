from xml.etree import ElementTree as ET

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="mail_to")
def mail_to(np):
    """
    Create link `mailto:`
    """
    phone = ET.Element("a", {"href": f"mailto:{np}", "class": "link-primary"})
    phone.text = f"{np}"
    return mark_safe(ET.tostring(phone, encoding="unicode"))
