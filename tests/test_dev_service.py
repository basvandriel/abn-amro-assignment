from abn_assignment.constants import USING_YEAR_DATA
from abn_assignment.domain.country.service import CountryService
from abn_assignment.domain.developer.service import Service
from sqlalchemy.orm import scoped_session


def test_save_from_so(sql_session: scoped_session):
    CountryService(sql_session).fetch_gdp_data(USING_YEAR_DATA)

    service = Service(sql_session)
    service.save_from_stackoverflow()
