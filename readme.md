# FLASK_STARTER(后端开发脚手架)

[项目地址](https://github.com/wuhanchu/flask_starter)
基于 flask 的框架，并整合一些常用框架。
基于一定的标准，快速创建 web 服务

## 目录

- [FLASK\_STARTER(后端开发脚手架)](#flask_starter后端开发脚手架)
  - [目录](#目录)
  - [上手指南](#上手指南)
    - [开发前的配置要求](#开发前的配置要求)
  - [文件目录说明](#文件目录说明)
  - [开发的架构](#开发的架构)
  - [编译](#编译)
  - [部署/运行](#部署运行)
  - [使用到的框架](#使用到的框架)
  - [版权说明](#版权说明)

## 上手指南

todo

### 开发前的配置要求

1. python 3.7+

## 文件目录说明

```
filetree
├── README.md -- 项目说明
├── /extension/ -- 通用组件
└── /util/ -- 通用工具
├── /module/ -- 业务模块
├── /frame/ -- 基础框架，统一标准和工具
│  ├── /docker/ -- docker 相关的表意脚本
│  ├── /http/ -- 请求和响应的统一接口和工具
│  ├── /util/ -- 公用工具类
│  ├── /requirements.txt -- 框架统一使用的依赖文件
├── run.py -- 程序运行文件
├── /requirements.txt -- 项目使用到的依赖包
├── /config.py -- 项目配置文件

```

## 开发的架构

todo 暂无

## 编译

```shell
docker build -f ./docker/Dockerfile -t wuhanchu/flask_flask_starer:master .
```

## 部署/运行

```shell
docker compose  -p project -f ./docker/docker-compose.yml --env-file ../run_config/env/flask_starter/test.env up -d
```

需要自定义环境变量文件

## 使用到的框架

todo 暂无

## 版权说明

该项目签署了 MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/shaojintian/Best_README_template/blob/master/LICENSE.txt)
