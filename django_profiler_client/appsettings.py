
DEBUG = False

if DEBUG:
    BASE_URL = 'http://localhost:8001/'
else:
    BASE_URL = 'http://djangoprofiler.com/'

QUERY_LOG_HANDLER = BASE_URL + 'query-submit/'
BENCHMARK_HANDLER = BASE_URL + 'benchmark-submit/'
MEMORY_PROFILE_HANDLER = BASE_URL + 'memory-submit/'
