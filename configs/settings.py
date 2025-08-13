from pydantic_settings import BaseSetting
from pydantic import Field

class Settings(BaseSetting):
    DB_URL: str = Field(default='postgresql+asyncpg://workout:workout@localhost/workout')

settings = Settings()