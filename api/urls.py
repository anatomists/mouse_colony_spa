from . import views
from .views import RegisterView, MouseViewSet, CageViewSet, BreedingPairViewSet, LitterViewSet  # Импортируем необходимые представления
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mice', MouseViewSet)
router.register(r'cages', CageViewSet)
router.register(r'breeding_pairs', BreedingPairViewSet)
router.register(r'litters', LitterViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
]
