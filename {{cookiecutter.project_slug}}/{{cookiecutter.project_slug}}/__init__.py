# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


import views


def setup_routes(app):
    app.router.add_get('/', views.index)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
    app.router.add_static('/node_modules/',
                          path=PROJECT_ROOT / 'node_modules',
                          name='node_modules')

