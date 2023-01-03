from sqlalchemy.orm import scoped_session

from abn_assignment.country import Country


def test_add_country(sql_session: scoped_session):
    country = Country("Nederland", "NL", 123.2, [])
    sql_session.add(country)
    sql_session.commit()
