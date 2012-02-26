
import memcache, re
from django.conf import settings
from datetime import datetime, timedelta

class MemcachedStats:
    """
    Dynamically populated container of statistics from the memcache server
    """
    pass


def getMemcachedStats():
    try:
        if not hasattr(settings, 'CACHE_BACKEND'):
            return None
        
        m = re.match("memcached://([.\w]+:\d+)", settings.CACHE_BACKEND)
        if not m:
            return None
        
        host = memcache._Host(m.group(1))
        host.connect()
        host.send_cmd("stats")
        
        stats = MemcachedStats()
        
        while True:
            line = host.readline().split(None, 2)
            if line[0] == "END":
                break
            stat, key, value = line
            try:
                value = int(value)
                if key == "uptime":
                    value = timedelta(seconds=value)
                elif key == "time":
                    value = datetime.fromtimestamp(value)
            except ValueError:
                pass
            
            setattr(stats, key, value)
        
        host.close_socket()
        
        return stats
    
    except Exception:
        return None




