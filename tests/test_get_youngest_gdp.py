from flask.testing import FlaskClient


def test_get_gdp_no_data(client: FlaskClient):
    response = client.get("/youngest_coding_gdp/NL")
    response.status_code == 404
    # assert response.json == {
    #     "gdp_in_euros": 893.0,
    #     "youngest_age_range": "18",
    # }
