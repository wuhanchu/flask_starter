# FLASK_STARTER (后端开发脚手架)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[项目地址](https://github.com/wuhanchu/flask_starter)

基于 Flask 的轻量级后端框架，整合常用组件，遵循一致的开发规范，帮助开发者快速搭建高质量 Web 服务。

## 目录

- [FLASK_STARTER (后端开发脚手架)](#flask_starter-后端开发脚手架)
  - [目录](#目录)
  - [项目特点](#项目特点)
  - [上手指南](#上手指南)
    - [开发前的配置要求](#开发前的配置要求)
    - [安装步骤](#安装步骤)
  - [文件目录说明](#文件目录说明)
  - [开发架构](#开发架构)
  - [编译与部署](#编译与部署)
    - [Docker 镜像构建](#docker-镜像构建)
    - [服务部署运行](#服务部署运行)
  - [使用到的框架](#使用到的框架)
  - [贡献指南](#贡献指南)
  - [版权说明](#版权说明)

## 项目特点

- 遵循 RESTful API 设计规范
- 模块化架构，便于扩展
- 内置常用开发组件
- 统一错误处理机制
- Docker 容器化支持

## 上手指南

### 开发前的配置要求

- Python 3.7+
- pip 或 pipenv
- Docker & Docker Compose (可选，用于容器化部署)

### 安装步骤

1. Clone 项目到本地
```bash
git clone https://github.com/wuhanchu/flask_starter.git
cd flask_starter
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动开发服务器
```bash
python run.py
```

## 文件目录说明

```
flask_starter/
├── README.md              # 项目说明文档
├── run.py                 # 程序入口文件
├── config.py              # 全局配置文件
├── requirements.txt       # 项目依赖包清单
│
├── /extension/            # 通用扩展组件
├── /util/                 # 通用工具类
├── /module/               # 业务模块目录
│   ├── /user/             # 用户模块示例
│   └── /...               # 其他业务模块
│
└── /frame/                # 基础框架，统一标准和工具
    ├── /docker/           # Docker 相关配置脚本
    ├── /http/             # 请求和响应的统一接口
    ├── /util/             # 框架工具类
    └── /requirements.txt  # 框架依赖文件
```

## 开发架构

基于 Flask 的 MVC 架构，遵循 RESTful API 设计规范，采用模块化开发方式。

详细架构文档请参考 [Wiki](https://github.com/wuhanchu/flask_starter/wiki)

## 编译与部署

### Docker 镜像构建

```bash
docker build -f ./docker/Dockerfile -t wuhanchu/flask_starter:latest .
```

### 服务部署运行

```bash
docker compose -p project -f ./docker/docker-compose.yml --env-file ../run_config/env/flask_starter/test.env up -d
```

> 注意：需要自定义环境变量文件，请参考 `example.env` 创建自己的环境配置

## 使用到的框架

- Flask - Web 框架
- SQLAlchemy - ORM 数据库工具
- Flask-RESTful - RESTful API 支持
- Marshmallow - 数据序列化/反序列化
- Pytest - 单元测试

## 版权说明

该项目签署了 MIT 授权许可，详情请参阅 [LICENSE](https://github.com/wuhanchu/flask_starter/blob/master/LICENSE)
