from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView
from api.views import RegisterView  # Импортируйте ваше представление RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TemplateView.as_view(template_name="index.html")),  # Обслуживание React
    re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name="index.html")),  # Обслуживание React для всех маршрутов
]
