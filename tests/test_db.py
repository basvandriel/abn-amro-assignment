from sqlalchemy.orm import scoped_session, Query
from abn_assignment.domain.country import Country, Developer


def test_add_country(sql_session: scoped_session):
    country = Country("Nederland", "NL", 123.2, [])
    developer = Developer(["Python", "Java"], country, "18")
    sql_session.add(developer)
    sql_session.commit()

    query: Query = sql_session.query(Country)
    all_countries: list[Country] = query.all()

    assert len(all_countries) == 1
    assert all_countries[0].name == "Nederland"
    assert all_countries[0].developers != []
