from flask.testing import FlaskClient


def test_get_bad(client: FlaskClient):
    response = client.get("/youngest_coding_gdp/123")
    assert response.text == "123"
