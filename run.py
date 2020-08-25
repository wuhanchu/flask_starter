from extension import scheduler, ai_frame, celery
from frame.app import create_app
import module
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--celery',  action="store_true")

app = create_app()

# 初始化自定义组件
scheduler.init_app(app)
ai_frame.init_app(app)
celery.init_app(app)

# 初始化模块
module.init_app(app)

print(app.url_map)

if __name__ == '__main__':

    args = parser.parse_args()
    print(args.celery)
    if args.celery:
        print("celery work")
        from extension.celery import celery
        celery.worker_main(['worker'])
    else:
        app.run('0.0.0.0', port=app.config.get("RUN_PORT"), threaded=False)
