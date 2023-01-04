from flask.testing import FlaskClient


def test_get_bad(client: FlaskClient):
    response = client.get("/youngest_coding_gdp/NL")

    assert response.json == {
        "gdp_in_euros": 893.0,
        "youngest_age_range": "18",
    }
