from flask import Blueprint


blueprint = Blueprint("domain", __name__)


@blueprint.route("/youngest_coding_gdp")
def resolve_youngest_coding_gdp(iso_code: str):
    return 0
