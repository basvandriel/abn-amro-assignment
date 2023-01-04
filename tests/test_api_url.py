from abn_assignment.constants import GDP_API_URL
from urllib.parse import urlparse


def test_url_validity():
    parsed_url = urlparse(GDP_API_URL)
    assert parsed_url
