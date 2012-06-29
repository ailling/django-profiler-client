
DEBUG = False

API_VERSION = 'v1'

API_USERNAME = ''
API_KEY = ''
APP_NAME = ''

if DEBUG:
    BASE_URL = 'http://localhost:8000'
else:
    BASE_URL = 'http://www.djangoperformance.com'

QUERY_LOG_HANDLER = BASE_URL + 'query-submit/'
BENCHMARK_HANDLER = BASE_URL + 'benchmark-submit/'
MEMORY_PROFILE_HANDLER = BASE_URL + 'memory-submit/'

QUERY_ENDPOINT = '%s/api/%s/query/?username=%s&%s' % (BASE_URL, API_VERSION, API_USERNAME, API_KEY)

