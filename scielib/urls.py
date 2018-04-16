from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view


urlpatterns = [
    url(r'^books/', include('scielib.apps.books.urls')),
    url(r'^patrons/', include('scielib.apps.patrons.urls')),
    url(r'^api/schema/$',
        get_schema_view(title='Scielib API'), name='api-schema'),
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
        [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
