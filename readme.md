# Flask Starter

> 结合 `flask_frame` 的轻量级 Flask 项目模版，用于快速搭建具备日志、监控与可扩展能力的内部服务。

## 目录

- [项目简介](#项目简介)
- [快速开始](#快速开始)
- [配置与环境变量](#配置与环境变量)
- [目录结构](#目录结构)
- [模块与扩展](#模块与扩展)
- [Docker 与部署](#docker-与部署)
- [常用脚本](#常用脚本)
- [开发与调试建议](#开发与调试建议)
- [许可证](#许可证)

## 项目简介

该脚手架在标准 Flask 应用上整合了 `flask_frame` 提供的组件，具备以下能力：

- 统一的异常拦截与响应格式，默认提供 `/`、`/healthy`、`/flask/log*` 等基础路由。
- 可以按需启用 `loguru`、`sentry`、`database`、`redis`、`celery` 等扩展，快速接入常见基础设施。
- 模块化加载业务代码，`ENABLED_MODULE` 中声明后自动导入并执行 `init_app`。
- 支持通过配置类或环境变量切换开发、测试、生产环境。
- 为容器部署准备了 `docker/Dockerfile` 与 `script/run.sh`，方便进阶部署。

## 快速开始

### 环境要求

- Python 3.12+
- pip 最新版本
- 可选：Docker / Docker Compose

### 本地运行

```bash
git clone https://github.com/wuhanchu/flask_starter.git
cd flask_starter

python -m venv .venv
source .venv/bin/activate          # Windows 用户执行 .venv\Scripts\activate

pip install -r requirements.txt

python run.py
```

启动后访问 `http://127.0.0.1:5000/`。若启用了 `loguru` 扩展，日志默认写入 `log/` 目录。

## 配置与环境变量

项目使用 `config.py` 中的配置类，默认选择 `DevelopmentConfig`。可通过环境变量 `FLASK_CONFIG` 指定其他配置，例如 `production`。

| 配置项                    | 默认值                  | 说明                                                      |
| ------------------------- | ----------------------- | --------------------------------------------------------- |
| `PRODUCT_KEY`             | `flask_starter`         | 服务标识，用于日志等场景                                  |
| `RUN_PORT`                | `5000`                  | `python run.py` 时的监听端口                              |
| `ENABLED_EXTENSION`       | `['loguru', 'sentry']`  | 自动加载的扩展名称，对应 `flask_frame.extension` 下的模块 |
| `ENABLED_MODULE`          | `[]`                    | 业务模块列表，模块需实现 `init_app(app)`                  |
| `USER_AUTH_URL`           | `http://127.0.0.1:5000` | 用户中心或认证服务地址，可在业务中使用                    |
| `SENTRY_DS`               | `None`                  | Sentry DSN，配置后自动初始化监控                          |
| `SQLALCHEMY_DATABASE_URI` | `None`                  | 数据库连接串，启用 `database` 扩展时必填                  |

常用环境变量示例：

```bash
export FLASK_CONFIG=production
export RUN_PORT=8080
export SQLALCHEMY_DATABASE_URI=postgresql://user:pass@host:5432/db
export SENTRY_DS=https://example.ingest.sentry.io/000000
```

## 目录结构

```
flask_starter/
├── config.py            # 多环境配置及启用扩展、模块的入口
├── context.py           # 全局 app 引用，便于模块化场景复用
├── run.py               # 应用启动入口，创建 Flask 实例并加载模块
├── requirements.txt     # Python 依赖（当前仅依赖 flask_frame）
├── docker/
│   └── Dockerfile       # 构建镜像所用的基础 Dockerfile
├── extension/           # 自定义扩展目录，占位示例
├── module/              # 业务模块目录，通过 ENABLED_MODULE 控制加载
├── script/
│   └── run.sh           # 容器内启动脚本（Gunicorn + 可选 Celery）
├── log/                 # 日志输出目录（运行后生成）
└── license.txt
```

## 模块与扩展

### 启用业务模块

1. 在 `module/` 下创建模块（例如 `module/example/__init__.py`）。
2. 实现 `init_app(app)`，在其中注册蓝图、命令或任务。
3. 在 `config.py` 中的 `ENABLED_MODULE` 列表添加模块名：`ENABLED_MODULE = ['example']`。

```python
# module/example/__init__.py
from flask import Blueprint

bp = Blueprint("example", __name__, url_prefix="/api/example")


@bp.route("/ping")
def ping():
    return {"message": "pong"}


def init_app(app):
    app.register_blueprint(bp)
```

### 使用内置扩展

`flask_frame` 已实现常用扩展，可在 `ENABLED_EXTENSION` 中按需开启：

- `loguru`：结构化日志，输出到控制台并持久化到 `log/`。
- `sentry`：上报异常到 Sentry，需设置 `SENTRY_DS`。
- `database`：封装 SQLAlchemy，需配置 `SQLALCHEMY_DATABASE_URI`。
- `redis`：初始化 Redis 连接池，需设置 `REDIS_URL` 环境变量。
- `celery`：集成 Celery，配合 `script/run.sh` 可启动 worker/beat。

扩展模块如果需要额外第三方依赖，请在 `requirements.txt` 中补充。

## Docker 与部署

### 构建镜像

`docker/Dockerfile` 基于官方 Python 3.12 镜像，默认安装 `requirements.txt` 并执行 `script/run.sh`：

```bash
docker build -t flask-starter:latest -f docker/Dockerfile .
```

### 运行容器

```bash
docker run -d \
  --name flask-starter \
  -p 5000:5000 \
  -e FLASK_CONFIG=production \
  -e RUN_PORT=5000 \
  flask-starter:latest
```

若需要挂载日志目录，可加入 `-v $(pwd)/log:/opt/www/log`。

### Gunicorn 部署

`script/run.sh` 默认使用 Gunicorn + Gevent：

```bash
pip install gunicorn gevent
CORE_NUM=4 TIME_OUT=300 PARAM_STR="--access-logfile -" gunicorn -w 4 -t 300 \
  --worker-class gevent --worker-connections 2000 -b 0.0.0.0:5000 run:app
```

## 常用脚本

`script/run.sh` 会：

- 读取 `CORE_NUM`、`TIME_OUT`、`PARAM_STR` 环境变量，启动 Gunicorn。

### celery

默认禁用的 Celery 支持：

- 创建日志目录并滚动清理旧的 Celery PID 文件。
- 如果在代码中实现了 Celery 命令，尝试执行 `python3 run.py --celery` 与 `--celery --beat`（可按需注释或扩展）。
  在未接入 Celery 时，可移除或注释相关行，避免多余进程占用资源。

## 开发与调试建议

- `FLASK_CONFIG=development python run.py`：使用开发配置，开启调试模式。
- `GET /healthy`：健康检查；`GET /flask/log`：查看已生成的日志文件列表。
- 在请求 URL 后追加 `?profile` 可启用 `pyinstrument` 性能分析（按需安装）。
- 建议在 `module/` 中编写 pytest 单元测试，并在项目根目录执行 `pytest`。

## 许可证

项目基于 MIT License 发行，详见 `license.txt`。
