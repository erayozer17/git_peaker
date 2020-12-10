class BaseConfig:
    """Base configuration."""

    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    pass


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
