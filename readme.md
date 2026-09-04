# Flask Starter

基于 `flask_frame` 的 Flask 项目模板，用于快速搭建内部服务。

## 快速开始

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

访问 `http://127.0.0.1:5000/`。

## 环境要求

- Python 3.12+
- PostgreSQL（启用 database 扩展时）
- Redis（启用 redis/celery/lock 扩展时）

## 目录结构

```
flask_starter/
├── config.py              # 多环境配置（Development/Testing/Production）
├── context.py             # 全局 app 引用
├── run.py                 # 启动入口
├── AGENTS.md              # AI 编码指南
├── module/                # 业务模块
│   ├── __init__.py        # 模块加载器
│   └── example/           # 示例模块（默认不启用）
│       ├── __init__.py    # Blueprint + init_app
│       ├── model.py       # 反射模型
│       ├── schema.py      # Marshmallow schema
│       ├── resource.py    # 路由 + docstring
│       └── service.py     # 业务逻辑
├── extension/             # 自定义扩展（按需）
├── tests/                 # pytest 测试
├── docker/Dockerfile      # 容器构建
├── script/
│   ├── run.sh             # 生产启动（Gunicorn + Gevent）
│   └── run_dev.sh         # 开发启动
├── requirements.txt       # 生产依赖
├── requirements_dev.txt   # 开发依赖（pytest 等）
├── pytest.ini             # pytest 配置
└── license.txt
```

## 配置

`config.py` 定义三套环境，通过 `FLASK_CONFIG` 环境变量切换（默认 `development`）。

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `PRODUCT_KEY` | `flask_starter` | 服务标识 |
| `RUN_PORT` | `5000` | 监听端口 |
| `ENABLED_EXTENSION` | `['loguru', 'sentry']` | 启用的 flask_frame 扩展 |
| `ENABLED_MODULE` | `[]` | 启用的业务模块 |
| `SQLALCHEMY_DATABASE_URI` | 环境变量 | 数据库连接串 |
| `DB_SCHEMA` | `example` | 数据库 schema（逗号分隔多个） |
| `AUTO_UPDATE` | `False` | 禁止自动建表/迁移 |
| `CHECK_API` | `False` | API 权限校验开关 |
| `SENTRY_DS` | 环境变量 | Sentry DSN |

```bash
export FLASK_CONFIG=production
export SQLALCHEMY_DATABASE_URI=postgresql://user:pass@host:5432/db
export SENTRY_DS=https://example.ingest.sentry.io/000000
```

## 模块开发

### 创建新模块

1. 在 `module/` 下创建目录（如 `module/order/`）
2. 实现 `__init__.py`（Blueprint + `init_app`）、`model.py`、`schema.py`、`resource.py`、`service.py`
3. 在 `config.py` 的 `ENABLED_MODULE` 添加模块名

参考 `module/example/` 的完整示例。

### 反射模型

**不写 Column 定义**，flask_frame 启动时自动反射表结构：

```python
from flask_frame.extension.database import db, BaseModel

class Order(BaseModel, db.Model):
    """订单表

    Fields:
        id: 主键
        order_no: 订单号
        status: 状态|pending:待处理,done:已完成
    """
    __table_args__ = {"schema": "example", "extend_existing": True}
    __tablename__ = "order"
```

改表流程：手动 DDL → 更新 model docstring → 重启。不使用自动迁移。

### API 响应

```python
from flask_frame.api.response import Response
from flask_frame.api.request import get_request_param

@blueprint.route("/order", methods=["POST"])
def order_create():
    params, _ = get_request_param()
    return Response(data={...}).make_flask_response()
```

### API Docstring 规范

- 中文标题用 **名词_动词** 格式（如 `订单_创建`）
- `tags` 用 `/` 分层级（如 `订单/管理`）
- 枚举 description 含中文说明：`状态|pending:待处理,done:已完成`
- 可选参数加 `default`

## flask_frame 扩展

在 `ENABLED_EXTENSION` 中按需启用：

| 扩展 | 依赖 | 说明 |
|------|------|------|
| `database` | PostgreSQL | SQLAlchemy + 反射模型 |
| `redis` | Redis | 连接池，支持 Sentinel |
| `lock` | Redis | 分布式锁 |
| `celery` | Redis/RabbitMQ | 异步任务 |
| `permission` | database | 鉴权 + API 校验 |
| `api_log` | database + celery | 请求日志 |
| `sentry` | Sentry DSN | 异常上报 |
| `minio` | MinIO | 文件上传/下载 |
| `consul` | Consul | 服务注册 |
| `loguru` | lock | 结构化日志 |
| `marshmallow` | — | 序列化 |
| `postgrest` | database | postgrest 代理 |

## 测试

```bash
pip install -r requirements_dev.txt
pytest
```

冒烟测试不依赖数据库/Redis，直接测试框架路由（`/`、`/healthy`）。

## Docker 部署

```bash
docker build -t flask-starter:latest -f docker/Dockerfile .
docker run -d --name flask-starter -p 5000:5000 \
  -e FLASK_CONFIG=production \
  -e SQLALCHEMY_DATABASE_URI=postgresql://user:pass@host:5432/db \
  flask-starter:latest
```

`script/run.sh` 使用 Gunicorn + Gevent：

```bash
gunicorn -w $CORE_NUM -t $TIME_OUT --worker-class gevent \
  --worker-connections 2000 -b 0.0.0.0:5000 run:app
```

## 默认路由

| 路由 | 说明 |
|------|------|
| `GET /` | 服务状态 |
| `GET /healthy` | 健康检查（JSON） |
| `GET /flask/log` | 日志文件列表 |
| `GET /flask/log/download` | 日志下载（zip） |
| `GET /debug-sentry` | Sentry 测试 |
| `GET any?profile` | 性能分析（pyinstrument） |

## 许可证

MIT License，详见 `license.txt`。
