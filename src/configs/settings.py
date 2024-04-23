from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(
        default="postgresql+asyncpg://workout:workout@localhost/workwout"
    )


settings = Settings()
