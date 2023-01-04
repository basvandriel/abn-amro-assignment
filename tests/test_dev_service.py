from abn_assignment.domain.developer.service import Service
from sqlalchemy.orm import scoped_session


def test_save_from_so(sql_session: scoped_session):
    service = Service(sql_session)
    service.save_from_stackoverflow()
