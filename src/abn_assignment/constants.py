from os import getenv

DATABASE_USER: str = getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD: str = getenv("DATABASE_PASSWORD", "")
DATABASE_HOST: str = getenv("DATABASE_HOST", "localhost")
DATABASE_PORT: int = getenv("DATABASE_PORT", 5432)
DATABASE_NAME: str = getenv("DATABASE_NAME", "abnamro")
