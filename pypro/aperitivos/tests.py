import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1>Video Aperitivo: Motivacao</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe width="1280" height="720" src="https://www.youtube.com/embed/2aYplgJrPDU"'
                          'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;'
                          'clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen> </iframe>')
