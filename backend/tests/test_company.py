import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

UserModel = get_user_model()
URL_COMPANIES = reverse('companies_details')
URL_COMPANY = reverse('company_details', kwargs={'company_id': 1})


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_company_create(authenticated_client, data_company):

    client = authenticated_client
    request = client.post(URL_COMPANIES, data_company, format='json')
    assert request.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_company_delete(authenticated_client, data_company):

    client = authenticated_client
    client.post(URL_COMPANIES, data_company, format='json')
    request = client.delete(URL_COMPANY, format='json')
    assert request.status_code == status.HTTP_200_OK
