import os
from flask import Blueprint
from flask_frame.util.py_utils import import_dir

blueprint = Blueprint("example", __name__, url_prefix="/example")


def init_app(app, **kwargs):
    import_dir(os.path.dirname(__file__), __name__)
    app.register_blueprint(blueprint)
