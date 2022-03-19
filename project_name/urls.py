from django.urls import include,re_path, path
from django.contrib import admin
admin.autodiscover()

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView,  SpectacularSwaggerSplitView

urlpatterns = [
    #Api doc
    re_path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    re_path('api/schema/swagger-ui',  SpectacularSwaggerSplitView.as_view(url_name='schema'), name='swagger-ui'),
    re_path('api/schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Admin
    re_path(r'^adm/', admin.site.urls),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),

    re_path(r'^api/', include('api.urls')),
]
