from flask.testing import FlaskClient
import pytest
from sqlalchemy.orm import scoped_session

from abn_assignment.domain.country import Country
from abn_assignment.domain.developer import Developer


def test_get_gdp_no_data(client: FlaskClient):
    with pytest.raises(ValueError) as e:
        client.get("/youngest_coding_gdp/NL")

    assert str(e.value) == "ISO-code not found"


def test_get_gdp_only_country(
    client: FlaskClient,
    sql_session: scoped_session,
):
    country = Country("Nederland", "NL", None, [])
    sql_session.add(country)
    sql_session.commit()

    with pytest.raises(ValueError) as e:
        client.get("/youngest_coding_gdp/NL")

    assert str(e.value) == "Developer not found"


def test_get_gdp_correct(
    client: FlaskClient,
    sql_session: scoped_session,
):
    country = Country("Nederland", "NL", 1000, [])
    sql_session.add(country)
    sql_session.commit()

    dev1 = Developer(["Python"], country, "10")
    dev2 = Developer(["Python"], country, "20")

    sql_session.add_all([dev1, dev2])
    sql_session.commit()

    response = client.get("/youngest_coding_gdp/NL")
    json = response.json

    assert json["gdp_in_euros"] == 1000
    assert json["youngest_age_range"] == "10"
