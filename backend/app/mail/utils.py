from django.template.loader import get_template


def render_template(template_name, context):
    return get_template(template_name).render({**context})
