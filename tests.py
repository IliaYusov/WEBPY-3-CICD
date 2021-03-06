import run as tested_app
import pytest


@pytest.fixture
def client():
    tested_app.app.config['TESTING'] = True
    app = tested_app.app.test_client()
    return app


def test_get(client):
    r = client.get('/')
    assert r.data.decode('utf-8') == 'Ok'
