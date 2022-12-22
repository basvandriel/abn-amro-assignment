# abn-amro-assignment

In essence, when saving the Gross Domestic Product (GDP) data, we only need 2 columns; the country name and the GDP in euro's itself. There are rows which have multiple countries collected in one row. Those needs to be filtered out.

This starts with saving the from the public API endpoint [endpoint](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/TEC00001?format=JSON&lang=en&unit=CP_EUR_HAB&time=2021) of the GDP data provider, which we can then insert in our database. Since 2022 hasn't ended yet, I'm using data from last year; 2021. The filters are applied on the data provider's website.

Actually, SQL isn't even mandatory unless we want to persist data at a certain timestamp. If you always want to keep up to date, assuming this data get's updated, we can call the endpoint itself and fetch save it into memory.

To keep it simple (KISS principle), we just have a seed script which populates the database. We'll use a Python package called click.

## Part 1

...
