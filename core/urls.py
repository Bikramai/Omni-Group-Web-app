from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.views.static import serve

from core.settings import MEDIA_ROOT, STATIC_ROOT, ENVIRONMENT


def handler404(request, *args, **kwargs):
    return render(request, "404.html")


def handler500(request, *args, **kwargs):
    return render(request, "500.html")


# EXTERNAL APPS URLS
urlpatterns = [

    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
]

# your apps urls
urlpatterns += [
    path('', include('src.website.urls', namespace='website')),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

# if ENVIRONMENT != 'server':
#     urlpatterns += [
#         path("__reload__/", include("django_browser_reload.urls"))
#     ]
