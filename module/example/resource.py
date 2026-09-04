from flask_frame.api.response import Response
from flask_frame.api.request import get_request_param
from module.example import blueprint
from module.example.service import query_task_list, create_task, get_task
from module.example.schema import TaskSchema


@blueprint.route("/task", methods=["GET"])
def task_list():
    """
    任务列表_查询

    查询任务列表，支持分页。

    ---
    tags:
      - 示例/任务管理
    parameters:
      - name: page
        in: query
        required: false
        type: integer
        description: 页码
        default: 1
      - name: size
        in: query
        required: false
        type: integer
        description: 每页条数
        default: 20
    responses:
      200:
        description: 任务列表
    """
    params, _ = get_request_param()
    page = int(params.get("page", 1))
    size = int(params.get("size", 20))
    tasks, total = query_task_list(page, size)
    schema = TaskSchema(many=True)
    return Response(data={"list": schema.dump(tasks), "total": total}).make_flask_response()


@blueprint.route("/task", methods=["POST"])
def task_create():
    """
    任务_创建

    创建新任务。

    ---
    tags:
      - 示例/任务管理
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              description: 任务标题
            description:
              type: string
              description: 任务描述
            status:
              type: string
              description: "状态|pending:待处理,done:已完成"
              enum: [pending, done]
              default: pending
    responses:
      200:
        description: 创建成功
    """
    params, _ = get_request_param()
    task = create_task(params)
    schema = TaskSchema()
    return Response(data=schema.dump(task)).make_flask_response()


@blueprint.route("/task/<int:task_id>", methods=["GET"])
def task_detail(task_id):
    """
    任务_查询

    查询单个任务详情。

    ---
    tags:
      - 示例/任务管理
    parameters:
      - name: task_id
        in: path
        required: true
        type: integer
        description: 任务ID
    responses:
      200:
        description: 任务详情
    """
    task = get_task(task_id)
    schema = TaskSchema()
    return Response(data=schema.dump(task)).make_flask_response()
