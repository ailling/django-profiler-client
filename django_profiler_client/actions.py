
import urllib, urllib2


from django_profiler_client import appsettings
#import appsettings
from django.conf import settings
from datetime import datetime

import logging
logger = logging.getLogger(__name__)

def TransmitQueries(**kwargs):
    """
    Transmits profiled query data to djangoprofiler.com
    """
    queries = kwargs.get('queries', None)
    
    if queries is None:
        return
    
    for query in queries:
        values = {'appusername': appsettings.API_USERNAME,
                  'appname': appsettings.APP_NAME,
                  'viewname': kwargs.get('viewname', ''),
                  'submission_timestamp': str(datetime.now()),
                  'sql': query['sql'],
                  'execution_time': query['time'],
                  }
        print 'sending query to %s' % appsettings.QUERY_ENDPOINT
        
        resp = requests.post(appsettings.QUERY_ENDPOINT,
                             data=json.dumps(values),
                             headers={'content-type': 'application/json'})
        print 'response: ', resp
        
#    values = {'requesturl': kwargs.get('requesturl', 'Unknown'),
#              'viewname': kwargs.get('viewname', ''),
#              'submission_timestamp': kwargs.get('submission_timestamp', ''),
#              'app_key': kwargs.get('app_key', ''),
#              'app_domain': kwargs.get('app_domain', '')}
#    
#    for i, query in enumerate(queries):
#        sqlkey = 'sql-%d' % i
#        timekey = 'time-%d' % i
#        values[sqlkey] = query['sql']
#        values[timekey] = query['time']
#    
#    
#    try:
#        data = urllib.urlencode(values)
#        urllib2.urlopen(appsettings.QUERY_LOG_HANDLER, data)
#    except Exception, e:
#        logger.info('Error sending queries: %s' % e.message)
#        return


def TransmitBenchmark(**kwargs):
    """
    Transmits profiled benchmark data to djangorpofiler.com
    """
    benchmark_time = kwargs.get('time', None)
    if benchmark_time is None:
        return
    
    
    values = {'benchmark_time': benchmark_time,
              'viewname': kwargs.get('viewname', ''),
              'name' : kwargs.get('name', ''),
              'submission_timestamp': kwargs.get('submission_timestamp', datetime.now()),
              'requesturl': kwargs.get('requesturl', 'Unknown'),
              'app_key': kwargs.get('app_key', ''),
              'app_domain': kwargs.get('app_domain', '')}
    
    try:
        data = urllib.urlencode(values)
        urllib2.urlopen(appsettings.BENCHMARK_HANDLER, data)
    except Exception, e:
        logger.info('Error sending benchmarks: %s' % e.message)
        return


def TransmitMemoryProfile(**kwargs):
    """
    Transmits profiled memcache data to djangoprofiler.com
    """
    memstats = kwargs.get('stats', None)
    
    if memstats is None:
        return
    
    values = {'requesturl': kwargs.get('requesturl', 'Unknown'),
              'viewname': kwargs.get('viewname', ''),
              'submission_timestamp': kwargs.get('submission_timestamp', datetime.now()),
              'app_key': kwargs.get('app_key', ''),
              'app_domain': kwargs.get('app_domain', ''),
              'kilobytes': memstats.bytes / 1024.0,
              'connections': memstats.curr_connections,
              'kilobytes_read': memstats.bytes_read / 1024.0,
              'kilobytes_written': memstats.bytes_written / 1024.0,
              'limit_maxkb': memstats.limit_maxbytes / 1024.0,
              'hits': memstats.get_hits,
              'misses': memstats.get_misses,
              'get_commands': memstats.cmd_get,
              'set_commands': memstats.cmd_set}
    
    try:
        data = urllib.urlencode(values)
        urllib2.urlopen(appsettings.MEMORY_PROFILE_HANDLER, data)
    except Exception, e:
        logger.info('Error sending memory profile: %s' % e.message)
        return



