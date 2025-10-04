from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"
    resend_api_key: str = ""
    allowed_origins: str = "http://localhost:5173"
    rate_limit: str = "10/minute"
    model_config = {"env_file": ".env"}

settings = Settings()
