from os import getenv

DATABASE_USER: str = getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD: str = getenv("DATABASE_PASSWORD", "")
DATABASE_HOST: str = getenv("DATABASE_HOST", "localhost")
DATABASE_PORT: int = getenv("DATABASE_PORT", 5432)
DATABASE_NAME: str = getenv("DATABASE_NAME", "abnamro")

USING_YEAR_DATA: int = 2021

# Neighboring string constants are automatically concatenated
# https://stackoverflow.com/a/1874679/2989034
GDP_API_URL: str = (
    "https://ec.europa.eu/eurostat/api/dissemination/statistics"
    "/1.0/data/TEC00001"
    f"?format=JSON&lang=en&unit=CP_EUR_HAB&time={USING_YEAR_DATA}"
)
