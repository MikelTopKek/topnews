import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

UserModel = get_user_model()
URL_POSTS = reverse('posts_details')
URL_POST = reverse('post_details', kwargs={'post_id': 1})


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_post_create(authenticated_client, data_post):

    client = authenticated_client
    request = client.post(URL_POSTS, data_post, format='json')
    assert request.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_post_delete(authenticated_client, data_post):

    client = authenticated_client
    client.post(URL_POSTS, data_post, format='json')
    request = client.delete(URL_POST, format='json')
    assert request.status_code == status.HTTP_200_OK
