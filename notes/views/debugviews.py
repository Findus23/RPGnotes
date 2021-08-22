from django.http import HttpResponse

from notes.utils.assets import get_css


def debug_css(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(css, content_type="text/css")


def debug_css_sourcemap(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(source_map, content_type="application/json")
