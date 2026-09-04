# AGENTS.md

## 项目概述

Flask Starter 是基于 `flask_frame` 框架的项目模板，用于快速搭建内部服务。

## 技术栈

- Python 3.12+
- Flask + flask_frame（框架库，pip 包）
- PostgreSQL（多 schema，反射模型）
- Gunicorn + Gevent（生产部署）

## 关键命令

```bash
# 开发运行
python run.py

# 测试
pytest

# 生产部署
bash script/run.sh
```

## 架构

```
flask_starter/
├── config.py          # 多环境配置
├── context.py         # 全局 app 引用
├── run.py             # 启动入口
├── module/            # 业务模块
│   ├── __init__.py    # 模块加载器（遍历 ENABLED_MODULE）
│   └── example/       # 示例模块
├── extension/         # 自定义扩展（按需）
├── tests/             # 测试
├── docker/            # Dockerfile
├── script/            # 部署脚本
└── requirements.txt   # 依赖
```

## flask_frame 核心导入

```python
from flask_frame import create_app, Response, FlaskFrameConfig, generate_openapi
from flask_frame.extension.database import db, BaseModel, run_sql, sql_concat
from flask_frame.extension.redis import redis_client
from flask_frame.extension.lock import get_lock
from flask_frame.extension.minio import upload_file_to_minio, download_file_from_minio
from flask_frame.extension.permission import get_current_user
from flask_frame.extension.celery import celery, BaseTask
from flask_frame.extension.marshmallow import ma
from flask_frame.api.request import get_request_param, proxy_request
from flask_frame.api.exception import ResourceError, CallException
from flask_frame.util.py_utils import import_dir
```

## 模块结构约定

每个业务模块位于 `module/<name>/`，包含：

| 文件 | 职责 |
|------|------|
| `__init__.py` | Blueprint 定义 + `init_app(app)`（用 `import_dir` 自动导入） |
| `model.py` | 反射模型，`from flask_frame.extension.database import db, BaseModel` |
| `schema.py` | Marshmallow schema，`from flask_frame.extension.marshmallow import ma` |
| `resource.py` | 路由定义，`@blueprint.route` + docstring |
| `service.py` | 业务逻辑 |

`__init__.py` 标准写法：

```python
import os
from flask import Blueprint
from flask_frame.util.py_utils import import_dir

blueprint = Blueprint("xxx", __name__, url_prefix="/xxx")

def init_app(app, **kwargs):
    import_dir(os.path.dirname(__file__), __name__)
    app.register_blueprint(blueprint)
```

## 反射模型约定

**不写 Column 定义**。flask_frame 在启动时通过 `DB_SCHEMA` 配置自动反射表结构。

```python
from flask_frame.extension.database import db, BaseModel

class Task(BaseModel, db.Model):
    """任务表

    Fields:
        id: 主键
        title: 任务标题
        status: 状态|pending:待处理,done:已完成
    """
    __table_args__ = {"schema": "example", "extend_existing": True}
    __tablename__ = "task"
```

改表流程：手动 DDL 修改数据库 → 更新 model docstring → 重启。**不使用自动迁移**。

## 响应格式

```python
# 成功
return Response(data={...}).make_flask_response()

# 失败
return Response(result=False, message="错误信息", http_status=400).make_flask_response()

# 抛异常
raise ResourceError(message="资源不存在", http_status=404)
```

`get_request_param()` 返回 `(params, _)`，params 是合并后的请求参数字典。

## API Docstring 规范

- 中文标题用 **名词_动词** 格式（如 `任务_创建`、`任务列表_查询`）
- `tags` 用 `/` 分层级（如 `示例/任务管理`）
- 参数名用单数（即使数组）
- 枚举 description 含中文说明：`状态|pending:待处理,done:已完成`
- 可选参数加 `default`
- 废弃接口加 `deprecated: true`（位于 tags 之前）

## flask_frame 扩展

在 `config.py` 的 `ENABLED_EXTENSION` 中按需启用：

| 扩展 | 依赖 | 说明 |
|------|------|------|
| `database` | PostgreSQL | SQLAlchemy + 反射模型 |
| `redis` | Redis | 连接池，支持 Sentinel |
| `lock` | Redis（降级文件锁） | 分布式锁 |
| `celery` | Redis/RabbitMQ | 异步任务 |
| `permission` | database | 鉴权 + API 校验 |
| `api_log` | database + celery | 请求日志 |
| `sentry` | Sentry DSN | 异常上报 |
| `minio` | MinIO 服务 | 文件上传/下载 |
| `consul` | Consul 服务 | 服务注册 |
| `loguru` | lock | 结构化日志 |
| `marshmallow` | — | 序列化 |
| `postgrest` | database | postgrest 代理 |

## 关键配置项

| 配置项 | 说明 |
|--------|------|
| `PRODUCT_KEY` | 服务标识 |
| `SQLALCHEMY_DATABASE_URI` | 数据库连接串 |
| `DB_SCHEMA` | 数据库 schema，逗号分隔多个 |
| `AUTO_UPDATE` | 自动建表/迁移（模板设 False） |
| `ENABLED_EXTENSION` | 启用的扩展列表 |
| `ENABLED_MODULE` | 启用的业务模块列表 |
| `CHECK_API` | API 权限校验开关 |
| `USER_AUTH_URL` | 用户认证服务地址 |
| `SENTRY_DS` | Sentry DSN |
| `REDIS_URL` | Redis 连接串 |
| `MINIO_*` | MinIO 配置 |
| `CONSUL_*` | Consul 配置 |

## 测试

```bash
pip install -r requirements_dev.txt
pytest
```

测试直连框架路由（`/`、`/healthy`），零基础设施依赖。业务模块测试可直连开发数据库。
