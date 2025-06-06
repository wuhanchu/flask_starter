# 🚀 Flask Starter

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)

**企业级 Flask 后端开发脚手架**

*基于 Flask 的模块化后端框架，集成企业级开发组件，助力快速构建高质量 Web 服务*

</div>

## 📋 目录

- [🚀 Flask Starter](#-flask-starter)
  - [📋 目录](#-目录)
  - [✨ 项目特点](#-项目特点)
  - [🏁 快速开始](#-快速开始)
    - [📋 环境要求](#-环境要求)
    - [⚡ 快速安装](#-快速安装)
    - [🐳 Docker 快速启动](#-docker-快速启动)
  - [📁 项目结构](#-项目结构)
  - [🏗️ 架构设计](#️-架构设计)
  - [⚙️ 配置说明](#️-配置说明)
  - [🚀 部署指南](#-部署指南)
  - [🔧 开发指南](#-开发指南)
  - [📦 技术栈](#-技术栈)
  - [🤝 贡献指南](#-贡献指南)
  - [📄 许可证](#-许可证)

## ✨ 项目特点

🎯 **现代化架构**
- 基于 Flask 的模块化架构设计
- 遵循 RESTful API 设计规范
- 支持微服务架构拆分

🔧 **开箱即用**
- 集成用户认证和权限管理
- 内置 Sentry 错误监控
- 支持 Loguru 日志管理
- 统一的异常处理机制

🐳 **容器化支持**
- Docker 容器化部署
- 多环境配置管理
- 健康检查和监控

⚡ **高性能**
- 异步任务处理支持
- 数据库连接池优化
- 缓存策略集成

🛡️ **企业级特性**
- 完善的权限控制系统
- 多租户架构支持
- 审计日志记录

## 🏁 快速开始

### 📋 环境要求

- **Python**: 3.12 或更高版本
- **pip**: 最新版本
- **Docker & Docker Compose**: 可选，用于容器化部署
- **Git**: 用于版本控制

### ⚡ 快速安装

1. **克隆项目**
   ```bash
   git clone https://github.com/wuhanchu/flask_starter.git
   cd flask_starter
   ```

2. **创建虚拟环境**（推荐）
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # 或 venv\Scripts\activate  # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置环境变量**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件，配置必要的环境变量
   ```

5. **启动开发服务器**
   ```bash
   python run.py
   ```

   访问 http://localhost:5000 查看应用

### 🐳 Docker 快速启动

1. **使用 Docker Compose 一键启动**
   ```bash
   docker-compose up -d
   ```

2. **或者构建自定义镜像**
   ```bash
   docker build -t flask-starter .
   docker run -p 5000:5000 flask-starter
   ```

## 📁 项目结构

```
flask_starter/
├── 📄 README.md              # 项目说明文档
├── 🚀 run.py                 # 程序入口文件
├── ⚙️ config.py              # 全局配置文件
├── 📦 requirements.txt       # 项目依赖包清单
├── 🐳 Dockerfile             # Docker 镜像构建文件
├── 📝 license.txt            # 许可证文件
│
├── 🔌 extension/             # 通用扩展组件
│   └── __init__.py
├── 🧩 module/                # 业务模块目录
│   ├── __init__.py
│   └── ...                   # 其他业务模块
├── 📋 context.py             # 应用上下文管理
├── 📊 log/                   # 日志文件目录
└── 🛠️ script/                # 脚本工具目录
```

### 核心组件说明

- **`run.py`**: 应用程序启动入口，负责初始化 Flask 应用和模块
- **`config.py`**: 配置管理，支持多环境配置（开发/测试/生产）
- **`extension/`**: 扩展组件目录，包含自定义的 Flask 扩展
- **`module/`**: 业务模块目录，采用模块化架构设计
- **`context.py`**: 全局应用上下文管理

## 🏗️ 架构设计

基于 Flask 的模块化架构，遵循 RESTful API 设计规范，采用依赖注入和插件化的设计模式。

### 🏛️ 系统架构

```
Flask Application
├── 🔧 Flask-Frame (核心框架)
│   ├── 🔐 权限管理 - 用户认证与授权
│   ├── ⚠️ 错误处理 - 统一异常处理机制
│   └── 📝 日志管理 - 请求追踪与审计
│
├── 🔌 Extensions (扩展组件)
│   ├── 📊 Loguru - 结构化日志记录
│   ├── 🔍 Sentry - 错误监控与性能追踪
│   └── ⚙️ 自定义扩展 - 业务特定功能
│
└── 📦 Business Modules (业务模块)
    ├── 👤 用户模块 - 用户信息管理
    ├── 💼 业务模块 - 核心业务逻辑
    └── 🔧 其他模块 - 扩展业务功能
```

### 🔄 架构特点

- **🧩 模块化设计**: 每个功能模块独立开发和部署
- **🔌 插件化扩展**: 支持动态加载和配置扩展组件
- **📊 统一监控**: 集成日志、错误追踪和性能监控
- **🔐 安全可靠**: 内置权限管理和数据安全机制

## ⚙️ 配置说明

### 环境配置

项目支持多环境配置，通过环境变量和配置类实现：

- **开发环境** (`DevelopmentConfig`): 启用调试模式，详细日志输出
- **测试环境** (`TestingConfig`): 测试专用配置
- **生产环境** (`ProductionConfig`): 生产环境优化配置

### 主要配置项

```python
# 应用配置
PRODUCT_KEY = "flask_starter"           # 产品标识
RUN_PORT = 5000                         # 运行端口

# 功能模块
ENABLED_EXTENSION = ["loguru", "sentry"] # 启用的扩展
ENABLED_MODULE = []                      # 启用的业务模块

# 外部服务
USER_AUTH_URL = "http://127.0.0.1:5000" # 用户认证服务地址
SENTRY_DS = "your_sentry_dsn"           # Sentry 错误跟踪

# 数据库配置
SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"  # 数据库连接
```

### 环境变量

在生产环境中，建议使用环境变量覆盖敏感配置：

```bash
export RUN_PORT=8080
export USER_AUTH_URL=https://auth.example.com
export SENTRY_DS=your_production_sentry_dsn
export SQLALCHEMY_DATABASE_URI=postgresql://user:pass@localhost/db
```

## 🚀 部署指南

### 本地开发部署

```bash
# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export FLASK_ENV=development
export USER_AUTH_URL=http://localhost:5000

# 启动应用
python run.py
```

### Docker 部署

```bash
# 构建镜像
docker build -t flask-starter:latest .

# 运行容器
docker run -d \
  --name flask-starter \
  -p 5000:5000 \
  -e USER_AUTH_URL=http://auth.example.com \
  -e SENTRY_DS=your_sentry_dsn \
  flask-starter:latest
```

### Docker Compose 部署

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - USER_AUTH_URL=http://auth.example.com
      - SENTRY_DS=your_sentry_dsn
    volumes:
      - ./logs:/opt/www/log
    restart: unless-stopped
```

### 生产环境部署

建议使用以下配置进行生产环境部署：

```bash
# 使用 Gunicorn 作为 WSGI 服务器
pip install gunicorn

# 启动生产服务器
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## 🔧 开发指南

### 添加新模块

1. 在 `module/` 目录下创建新模块目录
2. 实现模块的 `init_app(app)` 函数
3. 在 `config.py` 中的 `ENABLED_MODULE` 列表中添加模块名

示例：

```python
# module/user/__init__.py
def init_app(app):
    """初始化用户模块"""
    from . import routes
    app.register_blueprint(routes.bp)
```

### 添加新扩展

1. 在 `extension/` 目录下创建扩展文件
2. 实现扩展的 `init_app(app)` 函数
3. 在 `config.py` 中的 `ENABLED_EXTENSION` 列表中添加扩展名

### API 开发规范

```python
from flask import Blueprint, jsonify, request
from flask_frame.util.response import Response

bp = Blueprint('user', __name__, url_prefix='/api/v1/user')

@bp.route('/', methods=['GET'])
def list_users():
    """获取用户列表"""
    try:
        # 业务逻辑
        users = get_users()
        return Response.success(users)
    except Exception as e:
        return Response.error(str(e))
```

### 测试

```bash
# 运行测试
pytest

# 生成测试覆盖率报告
pytest --cov=./ --cov-report=html
```

## 📦 技术栈

### 核心框架
- **[Flask](https://flask.palletsprojects.com/)** - 轻量级 Web 框架
- **[Flask-Frame](https://github.com/wuhanchu/flask_frame)** - 自研 Flask 扩展框架

### 扩展组件
- **[Loguru](https://github.com/Delgan/loguru)** - 现代化日志记录
- **[Sentry](https://sentry.io/)** - 错误监控和性能追踪
- **[SQLAlchemy](https://sqlalchemy.org/)** - ORM 数据库工具（可选）

### 开发工具
- **[pytest](https://pytest.org/)** - 单元测试框架
- **[Docker](https://docker.com/)** - 容器化部署
- **[Gunicorn](https://gunicorn.org/)** - WSGI HTTP 服务器

### 依赖管理
```bash
# 查看当前依赖
pip list

# 生成依赖文件
pip freeze > requirements.txt

# 安全审计
pip-audit
```

## 🤝 贡献指南

我们欢迎所有形式的贡献！请遵循以下步骤：

### 开发流程

1. **Fork 项目** 到你的 GitHub 账户
2. **创建特性分支**: `git checkout -b feature/amazing-feature`
3. **提交更改**: `git commit -m 'Add some amazing feature'`
4. **推送分支**: `git push origin feature/amazing-feature`
5. **提交 Pull Request**

### 代码规范

- 遵循 [PEP 8](https://pep8.org/) Python 代码风格
- 添加适当的文档字符串和注释
- 保持测试覆盖率 > 80%
- 使用类型提示（Python 3.8+）

### 提交信息规范

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

类型说明：
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具相关

### 问题反馈

如果你发现了 bug 或有功能建议，请：

1. 搜索 [已有 issues](https://github.com/wuhanchu/flask_starter/issues)
2. 如果没有相关问题，[创建新 issue](https://github.com/wuhanchu/flask_starter/issues/new)
3. 详细描述问题或建议

## 📄 许可证

该项目基于 MIT 许可证开源，详情请查看 [LICENSE](license.txt) 文件。

```
MIT License

Copyright (c) 2024 wuhanchu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个 Star！**

**📧 联系我们**: [whcwuhanchu@gmail.com](mailto:whcwuhanchu@gmail.com)

</div>
