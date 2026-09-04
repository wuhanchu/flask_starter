import pytest
from flask_frame.app import create_app


@pytest.fixture
def app():
    """零基础设施冒烟测试 fixture：不依赖数据库/Redis/Celery"""
    test_config = {
        "default": type("TestConfig", (), {
            "PRODUCT_KEY": "flask_starter_test",
            "RUN_PORT": 5000,
            "ENABLED_EXTENSION": ["loguru"],
            "ENABLED_MODULE": [],
            "TESTING": True,
        }),
    }
    app = create_app(test_config)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
