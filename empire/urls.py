from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'empire.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('json_list.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    