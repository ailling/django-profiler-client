
import django.dispatch


ProfileSQLPerformance = django.dispatch.Signal(providing_args=["queries", "request"])

ProfileViewBenchmark = django.dispatch.Signal(providing_args=["time", "request", "name"])

ProfileMemory = django.dispatch.Signal(providing_args=["request", 'stats'])

