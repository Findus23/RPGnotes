from django_bootstrap5.templatetags import django_bootstrap5
from django_jinja import library


@library.global_function
def bootstrap_form(*args, **kwargs):
    return django_bootstrap5.bootstrap_form(*args, **kwargs)
