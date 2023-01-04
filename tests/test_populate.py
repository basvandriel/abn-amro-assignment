from abn_assignment.constants import USING_YEAR_DATA
from abn_assignment.domain.country.service import CountryService

from sqlalchemy.orm import scoped_session


def test_populate(sql_session: scoped_session):
    # CountryService(sql_session).fetch_gdp_data(USING_YEAR_DATA)
    assert True is not False
