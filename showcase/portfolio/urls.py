from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, BlogPostViewSet
from . import views

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'blogposts', BlogPostViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
]

