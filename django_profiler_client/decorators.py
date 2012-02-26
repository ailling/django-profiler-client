

from django_profiler_client import signals as profiler_signals
from django.db import connection
from django_profiler_client.signals import ProfileSQLPerformance
from functools import wraps
from django_profiler_client import memory

import stopwatch

import logging
logger = logging.getLogger(__name__)

def profile(fn):
    def wrapped(request, *args, **kwargs):
        logger.info('profile wrapper called')
        timer = stopwatch.Timer()
        
        response = fn(request)
        time = timer.stop()
        
        profiler_signals.ProfileViewBenchmark.send(sender=fn,
                                                   time=time,
                                                   request=request)
        
        
        profiler_signals.ProfileSQLPerformance.send(sender=fn,
                                                    queries=connection.queries,
                                                    request=request)
        
        
        profiler_signals.ProfileMemory.send(sender=fn,
                                            stats=memory.getMemcachedStats(),
                                            request=request)
        
        return response
    
    return wrapped


def profile_components(components=[]):
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            ls = map(lambda x: x.lower(), components)
            
            sql = 'sql' in ls
            benchmark = 'benchmark' in ls
            memcache = 'memcached' in ls or 'memcache' in ls
            
            if benchmark:
                timer = stopwatch.Timer()
                response = func(request)
                time = timer.stop()
                
                profiler_signals.ProfileViewBenchmark.send(sender=func,
                                                           time=time,
                                                           request=request)
            else:
                response = func(request)
            
            
            if sql:
                ProfileSQLPerformance.send(sender=func,
                                           queries=connection.queries,
                                           request=request)
            
            if memcache:
                profiler_signals.ProfileMemory.send(sender=func,
                                                    stats=memory.getMemcachedStats(),
                                                    request=request)
            
            response = func(request, *args, **kwargs)
            
            return response
        return wraps(func)(inner_decorator)
    return decorator





