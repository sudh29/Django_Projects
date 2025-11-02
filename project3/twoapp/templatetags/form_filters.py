from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(field, css):
    """
    Add a CSS class to a Django form field
    Usage: {{ form.field|addclass:"form-control" }}
    """
    return field.as_widget(attrs={"class": css})
