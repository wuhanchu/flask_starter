import os


class Config:
    """基础配置类"""

    # 项目配置
    PRODUCT_KEY = "flask_starter"
    RUN_PORT = os.getenv("RUN_PORT", 5000)

    # 启用的扩展（flask_frame 内置扩展名，按需增减）
    ENABLED_EXTENSION = ["loguru", "sentry"]

    # 启用的业务模块（module/ 下的目录名，如 ['example']）
    ENABLED_MODULE = []

    # 数据库配置（启用 database 扩展时必填）
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    DB_SCHEMA = "example"  # 数据库 schema，逗号分隔多个
    AUTO_UPDATE = False  # 禁止自动建表/迁移，手动管理表结构
    CHECK_API = False  # 禁用 API 权限校验（启用 permission 扩展后可开启）

    # 用户认证
    USER_AUTH_URL = os.getenv("USER_AUTH_URL", "http://127.0.0.1:5000")

    # Sentry 错误跟踪
    SENTRY_DS = os.getenv("SENTRY_DS")


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


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
