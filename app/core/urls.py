from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views.demo_schemas import ListDemos


router = DefaultRouter()
router.register('tags', ListDemos)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls))
]
