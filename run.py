# encoding: utf-8
"""
应用程序入口文件
===============

用于创建和运行Flask应用程序实例。
"""

import sys
if "gevent" in sys.modules:
    from gevent import monkey
    monkey.patch_all()


from flask_frame.app import create_app
from config import config
import context


# 检查是否已存在应用实例
if context.app:
    app = context.app
else:
    import module

    # 创建并初始化应用
    app = create_app(config)
    module.init_app(app)  # 初始化模块
    context.init_app(app)  # 设置应用上下文

    # 打印URL映射表，便于调试
    print(app.url_map)

    # 作为主程序运行时启动服务器
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=app.config.get("RUN_PORT"), threaded=False)
