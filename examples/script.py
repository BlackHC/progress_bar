import sys

from blackhc.progress_bar import with_progress_bar

for _ in with_progress_bar(range(100000)):
    pass
