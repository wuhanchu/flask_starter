from marshmallow import EXCLUDE
from flask_frame.extension.marshmallow import ma
from module.example.model import Task


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        unknown = EXCLUDE
