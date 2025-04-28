
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user_record(django_user_model):
    return django_user_model.objects.create_user(
        'user@example.com',
        password='password',
    )

@pytest.fixture
def api_client_drf():
    return APIClient()


@pytest.fixture
def api_client_drf_authenticate(authenticated_user, api_client_drf):
    refresh = RefreshToken.for_user(authenticated_user)
    api_client_drf.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return api_client_drf


@pytest.fixture
def api_client_drf_with_permissions(authenticated_user, api_client_drf):
    refresh = RefreshToken.for_user(authenticated_user)
    api_client_drf.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return api_client_drf, authenticated_user
