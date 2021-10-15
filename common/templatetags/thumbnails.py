from django import template
from sorl.thumbnail.templatetags.thumbnail import resolution
from django_jinja import library
from sorl.thumbnail import get_thumbnail

from rpg_notes import settings

register = template.Library()

@library.global_function
def thumbnail(*args, **kwargs):
    return get_thumbnail(*args, **kwargs)


@library.filter
def srcset(filename):
    """ Automatically generate the srcset value based on
    THUMBNAIL_ALTERNATIVE_RESOLUTIONS settings
    """
    lines = [filename]
    for res in settings.THUMBNAIL_ALTERNATIVE_RESOLUTIONS:
        res_string = "{}x".format(res)
        lines.append("{} {}".format(resolution(filename, res_string), res_string))
    return ', '.join(lines)
