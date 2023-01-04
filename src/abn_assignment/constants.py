from os import getenv
from pathlib import Path


DATABASE_USER: str = getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD: str = getenv("DATABASE_PASSWORD", "")
DATABASE_HOST: str = getenv("DATABASE_HOST", "localhost")
DATABASE_PORT: int = getenv("DATABASE_PORT", 5432)
DATABASE_NAME: str = getenv("DATABASE_NAME", "abnamro")

USING_YEAR_DATA: int = 2021

ROOT_DIR = Path(__file__).parent.parent.parent
DATA_DIR = ROOT_DIR / "data"
