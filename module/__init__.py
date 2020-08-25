# encoding: utf-8
"""
Modules
=======

Modules enable logical resource separation.

You may control enabled modules by modifying ``ENABLED_MODULES`` config
variable.
"""
from concurrent.futures.thread import ThreadPoolExecutor

executor = ThreadPoolExecutor(4)


def init_app(app, **kwargs):
    from importlib import import_module

    for module_name in app.config['ENABLED_MODULE']:
        import_module('.%s' % module_name,
                      package=__name__).init_app(app, **kwargs)
