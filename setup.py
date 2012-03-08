from distutils.core import setup

from django_profiler_client import version

setup(
    name = "django_profiler_client",
    package_dir={'django_profiler_client': ''},
    packages = ['django_profiler_client',],
    include_package_data=False,
    version = version.__VERSION__,
    author = "Alan Illing",
    description = ("Django Profiler Client is the profiler client for a Django project, available at djangoprofiler.com"),
    license = "GPL",
    url = "https://github.com/ailling/django-profiler-client",

)