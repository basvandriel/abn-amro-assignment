from flask import Blueprint

from abn_assignment.domain.country.sql_repository import SQLCountryRepository
from abn_assignment.domain.developer.sql_repository import (
    SQLDeveloperRepository,
)


from abn_assignment.domain.country.service import CountryService

from abn_assignment.sql_database import database
from dataclasses import asdict
from sqlalchemy.orm import scoped_session

blueprint = Blueprint("domain", __name__)


@blueprint.route("/youngest_coding_gdp/<iso_code>")
def resolve_youngest_coding_gdp(iso_code: str) -> dict[str, str | float]:
    session: scoped_session = database.session  # type: ignore

    service = CountryService(
        SQLCountryRepository(session),
        SQLDeveloperRepository(session),
    )
    return asdict(service.get_youngest_gdp(iso_code))
