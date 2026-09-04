from flask_frame.extension.database import db
from flask_frame.api.exception import ResourceError
from module.example.model import Task


def query_task_list(page=1, size=20):
    """查询任务列表，返回 (items, total)"""
    query = db.session.query(Task)
    total = query.count()
    items = query.offset((page - 1) * size).limit(size).all()
    return items, total


def get_task(task_id):
    """查询单个任务，不存在则抛异常"""
    task = db.session.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise ResourceError(message="任务不存在", http_status=404)
    return task


def create_task(data):
    """创建任务"""
    task = Task(**data)
    db.session.add(task)
    db.session.flush()
    return task
