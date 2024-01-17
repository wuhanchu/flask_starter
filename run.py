# encoding: utf-8

from flask_frame.extension import celery
from extension import permission

from flask_frame.app import create_app
import argparse
import module
from config import config
import context


if context.app:
    app = context.app
else:
    parser = argparse.ArgumentParser(description="manual to this script")
    parser.add_argument("--celery", action="store_true")
    parser.add_argument("--beat", action="store_true")

    # 初始化
    app = create_app(config)
    permission.init_app(app)
    module.init_app(app)
    context.init_app(app)
    print(app.url_map)

    if __name__ == "__main__":

        args = parser.parse_args()
        if args.celery:
            from flask_frame.extension.celery import celery

            log_level = app.config.get("LOG_LEVEL", "ERROR")

            if args.beat:
                celery.start(
                    argv=["beat", "-l", log_level, "-S", "redbeat.RedBeatScheduler"]
                )
            else:
                celery.worker_main(["worker"], "-c", app.config.get("CORE_NUM"))
        else:
            app.run("0.0.0.0", port=app.config.get("RUN_PORT"), threaded=False)
