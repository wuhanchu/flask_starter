import os


class Config:
    """基础配置类"""

    # 项目配置
    PRODUCT_KEY = "flask_starter"
    RUN_PORT = os.environ.get("RUN_PORT", 5000)

    # 启用的扩展
    ENABLED_EXTENSION = ["loguru", "sentry"]

    # 用户认证
    USER_AUTH_URL = os.environ.get("USER_AUTH_URL", "http://127.0.0.1:5000")

    # Sentry错误跟踪配置
    SENTRY_DS = os.environ.get("SENTRY_DS")

    # 启用的模块
    ENABLED_MODULE = []

    # 数据库配置
    # DB_SCHEMA = "flask_starter"
    SQLALCHEMY_ECHO = True                      # SQL语句输出到控制台
    SQLALCHEMY_RECORD_QUERIES = True            # 记录查询统计信息
    SQLALCHEMY_TRACK_MODIFICATIONS = True       # 追踪对象修改并发送信号
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")  # 数据库连接URI


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True


class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True


class ProductionConfig(Config):
    """生产环境配置"""
    pass


# 环境配置映射
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
