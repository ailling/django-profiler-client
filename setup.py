#!/usr/bin/env python

from distutils.core import setup

from django_profiler_client import version

setup(
    name = "django_profiler_client",
    packages = ['django_profiler_client',],
    version = version.__VERSION__,
    author = "Alan Illing",
    description = ("Django Profiler Client for profiling services at djangoprofiler.com"),
    license = "GPL",
    url = "https://github.com/ailling/django-profiler-client",
)
