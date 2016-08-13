# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.core import views
admin.autodiscover()


urlpatterns = [
    url(r'', include('apps.core.urls', app_name="core", namespace="core")),
    url(r'account/', include('apps.account.urls', app_name="account", namespace="account")),
    #url(r'enquete/', include('apps.enquete.urls', app_name="enquete", namespace="enquete")),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^404$', views.http404, name="http404"),
        url(r'^500$', views.http500, name="http500"),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

handler500 = views.http500
handler404 = views.http404
