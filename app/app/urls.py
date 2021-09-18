from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),
    path('api/core/', include('core.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Recipe APIs",
        default_version='v1',
        description="Django Project Template Docs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vanduongk1309@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser),
    permission_classes=(permissions.AllowAny,),
)

# Docs urls
urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-doc'),
]
