import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

UserModel = get_user_model()
URL_SIGN_UP = reverse('signup')
URL_USER = reverse('user_details', kwargs={'user_id': 2})


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_view_sign_up(authenticated_client, data_user):

    client = authenticated_client
    request = client.post(URL_SIGN_UP, data_user, format='json')
    print(request.json())

    assert request.status_code == status.HTTP_201_CREATED
    recipients_after_post = UserModel.objects.get(id='2')

    assert recipients_after_post is not None


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_user_delete(authenticated_client, data_user):

    client = authenticated_client
    client.post(URL_SIGN_UP, data_user, format='json')
    request = client.delete(URL_USER, format='json')

    assert request.status_code == status.HTTP_200_OK
    assert UserModel.objects.all().count() == 1
