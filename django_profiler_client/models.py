from django.db import models

from django.conf import settings



# -------------------------------------------
# SIGNAL REGISTRATION
# -------------------------------------------

import django.dispatch
from django_profiler_client import signals as profiler_signals
from django_profiler_client.signalcallbacks import ProfileSQLPerformanceCallback, ProfileViewBenchmarkCallback, ProfileMemoryCallback



profiler_signals.ProfileSQLPerformance.connect(ProfileSQLPerformanceCallback)
profiler_signals.ProfileViewBenchmark.connect(ProfileViewBenchmarkCallback)
profiler_signals.ProfileMemory.connect(ProfileMemoryCallback)



