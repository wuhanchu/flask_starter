from flask_frame.extension.database import db, BaseModel


class Task(BaseModel, db.Model):
    """示例任务表

    Fields:
        id: 主键
        title: 任务标题
        description: 任务描述
        status: 状态|pending:待处理,done:已完成
        created_at: 创建时间
        updated_at: 更新时间
    """

    __table_args__ = {"schema": "example", "extend_existing": True}
    __tablename__ = "task"
