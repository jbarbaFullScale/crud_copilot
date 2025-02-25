import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///crud_copilot.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        False  # Disable modification tracking for performance
    )
    DEBUG = (
        os.getenv("FLASK_DEBUG", "False").lower() == "true"
    )  # Convert env string to bool
    TESTING = False


class DevelopmentConfig(Config):
    """Development environment settings."""

    DEBUG = True
    SQLALCHEMY_ECHO = True  # Log SQL queries for debugging


class TestingConfig(Config):
    """Testing environment settings."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_crud_copilot.db"
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    """Production environment settings."""

    DEBUG = False
    SQLALCHEMY_ECHO = False


# Choose config based on FLASK_ENV
config_dict = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}

# Get the current config based on FLASK_ENV
CurrentConfig = config_dict.get(os.getenv("FLASK_ENV", "development"))
