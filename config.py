import os


class Config:
    """todo 通用配置 """
    # project
    PRODUCT_KEY = "flask_starter"
    RUN_PORT = os.environ.get('RUN_PORT', 5000)

    # set enable
    ENABLED_EXTENSION = ["loguru",  "sentry"]

    # todo auth
    USER_AUTH_URL = os.environ.get('USER_AUTH_URL', "http://127.0.0.1:5000")

    # todo sentry
    SENTRY_DS = os.environ.get('SENTRY_DS')

    # todo module
    ENABLED_MODULE = []

    # todo database
    # DB_SCHEMA = "flask_starter"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
