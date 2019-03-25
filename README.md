# Progress Bar

[![Build Status](https://travis-ci.org/BlackHC/progress_bar.svg?branch=master)](https://travis-ci.org/BlackHC/progress_bar)

A progress bar that is either using TQDM for nice outputs internally, or a log-friendly replacement that works well for piping into files.

## Installation

To install using pip, use:

```
pip install blackhc.progress_bar
```

To run the tests, use:

```
python setup.py test
```

## Example

```python
from blackhc.progress_bar import with_progress_bar

for _ in with_progress_bar(range(100000)):
    pass
```

