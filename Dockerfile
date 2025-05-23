# 基于官方 Python 3.12 镜像（非 Alpine）
FROM python:3.12

# 设置容器时区为上海(UTC+8)
ENV TZ=Asia/Shanghai

# 配置系统时区：
# 1. 创建符号链接将正确的时区文件链接到系统时钟配置
# 2. 将时区信息写入timezone文件供系统程序读取
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 禁用Python输出缓冲，确保日志实时显示（对调试和容器日志收集很有用）
ENV PYTHONUNBUFFERED=1

# 设置应用程序的工作目录路径
ENV API_SERVICE_HOME=/opt/www

# 创建并切换到指定的工作目录
WORKDIR "$API_SERVICE_HOME"

# 先只复制 requirements.txt
COPY requirements.txt ./

# 安装依赖（利用缓存）
RUN --mount=type=cache,target=/cache pip3 install  --cache-dir=/cache/pip   --prefer-binary -r ./requirements.txt   -i https://mirrors.cloud.tencent.com/pypi/simple/ --extra-index-url  https://pypi.org/simple/

# 再复制剩余代码
COPY ./ ./

# 给脚本设置执行权限
RUN chmod +x ./script/run.sh

# 设置容器启动时执行的命令
CMD ./script/run.sh
