from django import template

register = template.Library()

@register.filter
def make_range(value):
    """
    Generate a range of numbers from 0 to value-1.
    Usage in templates: {{ value|make_range }}
    """
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return range(int(5))
