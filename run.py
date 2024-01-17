# encoding: utf-8
from flask_frame.app import create_app
from .config import config
from . import context


if context.app:
    app = context.app
else:
    from . import module
    
    # 初始化
    app = create_app(config)
    module.init_app(app)
    context.init_app(app)
    print(app.url_map)

    if __name__ == "__main__":
        app.run("0.0.0.0", port=app.config.get("RUN_PORT"), threaded=False)
