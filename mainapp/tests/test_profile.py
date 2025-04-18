import pytest
from rest_framework import status
from baseapp.models import User


@pytest.mark.django_db
class TestProfile:

    def test_anonymous_wants_get_profile_page(self, api_client):
        response = api_client.get('/baseapp/profile/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_users_wants_get_profile_page(self, api_client):
        api_client.force_authenticate(user=User())
        response = api_client.get('/baseapp/profile/')
        assert response.status_code == status.HTTP_200_OK