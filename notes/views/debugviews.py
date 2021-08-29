from django.http import HttpResponse
from django.views.decorators.cache import cache_page

from notes.utils.assets import get_css

@cache_page(60 * 15)
def debug_css(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(css, content_type="text/css")

@cache_page(60 * 15)
def debug_css_sourcemap(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(source_map, content_type="application/json")
