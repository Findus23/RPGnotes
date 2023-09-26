from django_jinja import library
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.templatetags.thumbnail import resolution, is_portrait as is_portrait_original

from rpg_notes import settings


@library.global_function
def thumbnail(*args, **kwargs):
    kwargs["upscale"] = False
    size = args[1]
    file = args[0]
    if "x" not in size:
        if is_portrait_original(file):
            size = f"x{size}"
            args = list(args)
            args[1] = size
            args = tuple(args)
    return get_thumbnail(*args, **kwargs)


@library.filter
def is_portrait(file):
    return is_portrait_original(file)


@library.filter
def srcset(filename):
    """ Automatically generate the srcset value based on
    THUMBNAIL_ALTERNATIVE_RESOLUTIONS settings
    """
    lines = [filename]
    for res in settings.THUMBNAIL_ALTERNATIVE_RESOLUTIONS:
        res_string = f"{res}x"
        lines.append(f"{resolution(filename, res_string)} {res_string}")
    return ', '.join(lines)
