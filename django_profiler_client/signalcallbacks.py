

from django_profiler_client import actions
from django_profiler_client import tasks
from django.core.cache import cache
from django.conf import settings

from datetime import datetime

import pdb



def ProfileSQLPerformanceCallback(sender, **kwargs):
    if sender is not None:
        viewname = sender.__module__ + '.' + sender.__name__
    else:
        viewname = ''
    
    queries = kwargs.get('queries', None)
    request = kwargs.get('request', None)
    
    if request is not None:
        requesturl = request.build_absolute_uri()
    else:
        return
    
#    submission_timestamp = datetime.now()
#    app_key = settings.PROFILER_APP_KEY
#    app_domain = settings.PROFILER_APP_DOMAIN
    
    
    if hasattr(settings, 'PROFILER_SEND_ASYNC') and settings.PROFILER_SEND_ASYNC:
        tasks.TransmitSQLPerformanceTask.delay(viewname=viewname,
                                               queries=queries,
                                               requesturl=requesturl,
                                               submission_timestamp=datetime.now(),
                                               app_key=settings.PROFILER_APP_KEY,
                                               app_domain=settings.PROFILER_APP_DOMAIN)
    else:
        actions.TransmitQueries(viewname=viewname,
                                queries=queries,
                                requesturl=requesturl,
                                submission_timestamp=datetime.now(),
                                app_key=settings.PROFILER_APP_KEY,
                                app_domain=settings.PROFILER_APP_DOMAIN)


def ProfileViewBenchmarkCallback(sender, **kwargs):
    if sender is not None:
        viewname = sender.__module__ + '.' + sender.__name__
    else:
        viewname = ''
    
    benchmark_time = kwargs.get('time', None)
    if not benchmark_time:
        return
    
    request = kwargs.get('request', None)
    
    if request is not None:
        requesturl = request.build_absolute_uri()
    else:
        return
    
    name = kwargs.get('name', '')
    submission_timestamp = datetime.now()
    app_key = settings.PROFILER_APP_KEY
    app_domain = settings.PROFILER_APP_DOMAIN
    
    if hasattr(settings, 'PROFILER_SEND_ASYNC') and settings.PROFILER_SEND_ASYNC:
        tasks.TransmitBenchmarkTask.delay(time=benchmark_time,
                                          viewname=viewname,
                                          name=name,
                                          requesturl=requesturl,
                                          submission_timestamp=submission_timestamp,
                                          app_key=app_key,
                                          app_domain=app_domain)
    else:
        actions.TransmitBenchmark(time=benchmark_time,
                                  viewname=viewname,
                                  name=name,
                                  requesturl=requesturl,
                                  submission_timestamp=submission_timestamp,
                                  app_key=app_key,
                                  app_domain=app_domain)


def ProfileMemoryCallback(sender, **kwargs):
    if sender is not None:
        viewname = sender.__module__ + '.' + sender.__name__
    else:
        viewname = ''
    
    memstats = kwargs.get('stats', None)
    
    request = kwargs.get('request', None)
    
    if request is not None:
        requesturl = request.build_absolute_uri()
    else:
        return
    
    submission_timestamp = datetime.now()
    app_key = settings.PROFILER_APP_KEY
    app_domain = settings.PROFILER_APP_DOMAIN
    
    if hasattr(settings, 'PROFILER_SEND_ASYNC') and settings.PROFILER_SEND_ASYNC:
        tasks.TransmitMemoryProfileTask.delay(stats=memstats,
                                              viewname=viewname,
                                              requesturl=requesturl,
                                              submission_timestamp=submission_timestamp,
                                              app_key=app_key,
                                              app_domain=app_domain)
    else:
        actions.TransmitMemoryProfile(stats=memstats,
                                      viewname=viewname,
                                      requesturl=requesturl,
                                      submission_timestamp=submission_timestamp,
                                      app_key=app_key,
                                      app_domain=app_domain)



