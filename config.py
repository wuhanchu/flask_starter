import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    JSON_AS_ASCII = False

    ITEM_FILE_SAVE_PATH = "./resource/"

    # project
    PRODUCT_KEY = "z_ai_service"
    RUN_PORT = os.environ.get('RUN_PORT', 5000)

    # set enable
    ENABLED_EXTENSION = ["loguru", "database", "postgrest", "marshmallow", "sentry"]

    # auth
    USER_AUTH_URL = os.environ.get('USER_AUTH_URL', "http://127.0.0.1:5000")

    # sentry
    SENTRY_DS = "https://b1dea6df85c44820b4dd0f602a4e88ef@server.aiknown.cn:31027/8"

    # module
    ENABLED_MODULE = [
        "service", "report", "ocr", "voice", "asr", "vpr", "tts"
    ]

    # posrgrest
    PROXY_SERVER_URL = os.environ.get('PROXY_SERVER_URL')

    # database
    DB_SCHEMA = "z_ai_service"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # celery
    CELERY_BROKER = os.environ.get('CELERY_BROKER', "redis://:dataknown1234@server.aiknown.cn:32049")

    # 设置定时任务配置
    JOBS = [
        {
            'id': 'job_docker_refresh',
            'func': 'module.service.service:record_docker_status',  # 执行函数的路径
            'args': '',  # 参数
            'trigger': 'interval',  # interval 循环任务
            'seconds': 30  # 每隔30秒执行一次
        }
    ]

    # 其他配置
    UPLOAD_FOLDER = "items_upload"
    RETURN_FOLDER = "items_return"

    # 接口配置
    APIS = {
        # ocr相关接口配置
        'OCR': {
            # 服务器地址
            'SERVER_ADDRESS': 'http://39.105.193.154:57001',
            # 通用识别接口
            'VERSATILE_API_URI': '/dataknown_ocr',
            # 公章检测识别接口
            'STAMP_API_URI': '/dataknown_stamp'
        }
    }


class DevelopmentConfig(Config):
    DEBUG = True

    # set enable
    ENABLED_EXTENSION = ["loguru", "database", "postgrest", "marshmallow"]
    USER_AUTH_URL = "http://server.aiknown.cn:32024"

    PROXY_SERVER_URL = "http://server.aiknown.cn:32025"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
    #                                          'postgresql://postgres:dataknown1234@server.aiknown.cn:32021/dataknown')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql://postgres:dataknown1234@server.aiknown.cn:31014/dataknown')
    JOBS = []


class PerformanceConfig(Config):
    ENABLED_EXTENSION = ["database"]
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql://postgres:dataknown1234@server.aiknown.cn:32021/dataknown')
    JOBS = []


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'performance': PerformanceConfig,
    'default': DevelopmentConfig
}
