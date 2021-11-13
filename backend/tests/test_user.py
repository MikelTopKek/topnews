import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

USER_MODEL = get_user_model()
URL_SIGN_UP = reverse('signup')


@pytest.mark.django_db
def test_view_sign_up(authenticated_client, data_user):

    client = authenticated_client
    request = client.post(URL_SIGN_UP, data_user, format='json')
    print(request.json())

    assert request.status_code == status.HTTP_201_CREATED
    recipients_after_post = USER_MODEL.objects.get(id='1')

    assert recipients_after_post is not None
