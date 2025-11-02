from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(field, css):
    """Adds a CSS class to a bound field's widget.

    Usage in template: {{ form.field|addclass:"form-control" }}
    """
    try:
        return field.as_widget(attrs={"class": css})
    except Exception:
        # If field is not a bound field, return it unchanged
        return field
