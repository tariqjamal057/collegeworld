from django import template
from django.urls import resolve
from django.utils.html import strip_tags, format_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def show_field_errors(field):
    # field = template.Variable(field).resolve({})
    if field.errors:
        error_message = ""
        for error in field.errors:
            error_message = strip_tags(error)
        return mark_safe(
            '<span id="reason_error" class="text-danger text-sm">{}</span>'.format(
                error_message
            )
        )
    else:
        return ""
    

@register.filter()
def show_non_field_errors(error):
    if error:
        error_message = strip_tags(error)
        return mark_safe(
            '<div class="alert alert-danger"><p><span class="fe fe-alert-triangle fe-16 mr-2"></span>{}'
            "</p></div>".format(error_message)
        )
    else:
        return ""
    

@register.filter()
def show_label(field):
    if isinstance(field, str):
        # Convert the field parameter to a form field object
        field = template.Variable(field).resolve({})
    if field.field.required:
        required = '<span class="text-danger">*</span>'
    else:
        required = ""
    return mark_safe(
        '<label for="{}" class="mb-3.6 text-sm fs-6 text-dark">{} {}</label>'.format(
            field.label, field.label, required
        )
    )
@register.filter
def add_id(field, prefix=""):
    """
    Adds an ID attribute to a form field.
    """
    field_id = f"{prefix}_{field.name}"
    return format_html("{}", field.as_widget(attrs={"id": field_id}))