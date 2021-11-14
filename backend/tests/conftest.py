# pylint: disable=W0621
import os

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

USER_MODEL = get_user_model()


@pytest.fixture()
def data_valid_sign_up_admin_user():
    return {
        'username': os.getenv('DJANGO_ADMIN_USER'),
        'first_name': 'admin',
        'last_name': 'admin',
        'telephone_number': '+380954527680',
    }


@pytest.fixture()
def data_user():
    return {
        'username': 'test-username',
        'first_name': 'user1',
        'last_name': 'user1',
        'telephone_number': '+380950000001',
        'password': 'password'
    }


@pytest.fixture()
def data_post():
    return {
        'title': 'test-title',
        'text': 'test-text',
        'topic': 'test-topic'
    }


@pytest.fixture()
def data_company():
    return {
        'name': 'name-title',
        'url': 'url-text',
        'address': 'address-topic'
    }


@pytest.fixture()
def user(data_valid_sign_up_admin_user):
    created_user = USER_MODEL.objects.create(**data_valid_sign_up_admin_user)
    return created_user


@pytest.fixture()
def authenticated_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
