from abn_assignment.domain.country.fetcher import CountryFetcher


def test_country_fetch():
    result = CountryFetcher().fetch(2021)
    assert len(result) != 0
