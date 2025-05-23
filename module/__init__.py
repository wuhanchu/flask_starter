# encoding: utf-8
"""
模块
=======

模块实现了逻辑资源的分离。

你可以通过修改 ``ENABLED_MODULES`` 配置变量来控制启用的模块。
"""
from concurrent.futures.thread import ThreadPoolExecutor

# 创建线程池执行器，最大线程数为4
executor = ThreadPoolExecutor(max_workers=4)


def init_app(app, **kwargs):
    """
    初始化应用程序的模块
    
    Args:
        app: Flask应用实例
        **kwargs: 额外的参数
    """
    from importlib import import_module

    # 导入并初始化所有在配置中启用的模块
    for module_name in app.config['ENABLED_MODULE']:
        import_module(f'.{module_name}', package=__name__).init_app(app, **kwargs)
