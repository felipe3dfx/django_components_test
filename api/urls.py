from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router: ExtendedSimpleRouter = ExtendedSimpleRouter()
router = routers.DefaultRouter()

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'schema/swagger/',
        SpectacularSwaggerView.as_view(url_name='api:schema'),
        name='swagger',
    ),
    path(
        'schema/redoc/',
        SpectacularRedocView.as_view(url_name='api:schema'),
        name='redoc',
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
