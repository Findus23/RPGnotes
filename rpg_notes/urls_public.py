import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from common import views
from rpg_notes import settings

urlpatterns = [
    path('', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', views.PublicHomepageView.as_view()),
    path('admin/', admin.site.urls),
    path('', include("campaigns.urls_public"))
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)), )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path("css", views.debug_css, name="css"))
    urlpatterns.append(path("css_sourcemap", views.debug_css_sourcemap, name="css_sourcemap"))

handler500 = "common.views.handler500"
