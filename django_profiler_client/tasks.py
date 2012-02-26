
from django_profiler_client import actions

from celery.decorators import task


@task(name="tasks.TransmitSQLPerformanceTask")
def TransmitSQLPerformanceTask(**kwargs):
    actions.TransmitQueries(**kwargs)


@task(name="tasks.TransmitBenchmarkTask")
def TransmitBenchmarkTask(**kwargs):
    actions.TransmitBenchmark(**kwargs)


@task(name="tasks.TransmitMemoryProfileTask")
def TransmitMemoryProfileTask(**kwargs):
    actions.TransmitMemoryProfile(**kwargs)

