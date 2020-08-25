from frame.app import create_app
import module

app = create_app()

# todo 初始化自定义组件

# 初始化模块
module.init_app(app)

print(app.url_map)

if __name__ == '__main__':
    app.run('0.0.0.0', port=app.config.get("RUN_PORT"), threaded=False)