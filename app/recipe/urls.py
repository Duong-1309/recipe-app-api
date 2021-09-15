from rest_framework.routers import DefaultRouter

from recipe.views import TagViewSet

app_name = 'recipe'

urlpatterns = []

tag_router = DefaultRouter()
tag_router.register('tags', TagViewSet)
urlpatterns += tag_router.urls
