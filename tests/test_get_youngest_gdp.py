from flask.testing import FlaskClient


def test_get_bad(client: FlaskClient):
    response = client.get("/youngest_coding_gdp/123")
    json = response.json

    assert json == {
        "gdp_in_euros": 30.3,
        "youngest_age_range": "nee",
    }
