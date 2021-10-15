from django_bootstrap5.templatetags import django_bootstrap5
from django_jinja import library


@library.global_function
def bootstrap_form(*args, **kwargs):
    return django_bootstrap5.bootstrap_form(*args, **kwargs)


@library.global_function
def bootstrap_alert(*args, **kwargs):
    return django_bootstrap5.bootstrap_alert(*args, **kwargs)


@library.filter
def bootstrap_message_alert_type(*args, **kwargs):
    return django_bootstrap5.bootstrap_message_alert_type(*args, **kwargs)
