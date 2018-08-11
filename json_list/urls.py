from django.conf.urls import include, url
from .views import JsonListView, JsonFileUploadView

urlpatterns = [
    # Examples:
    # url(r'^$', 'empire.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', JsonListView.as_view(), name='home'),
    url(r'^create/$', JsonFileUploadView.as_view(), name='create'),
]
