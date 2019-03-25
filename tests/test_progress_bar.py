import pytest

import blackhc.progress_bar as pb


def test_creates_tqdm():
    pb.use_tqdm = True
    progress_bar = pb.create_progress_bar(100)

    assert type(progress_bar) == pb.TQDMProgressBar


def test_creates_log_friendly():
    pb.use_tqdm = False
    progress_bar = pb.create_progress_bar(100)
    assert type(progress_bar) == pb.LogFriendlyProgressBar


def test_tqdm_coverage():
    pb.use_tqdm = True
    for _ in pb.with_progress_bar(range(100)):
        pass


def test_log_friendly_coverage():
    pb.use_tqdm = False
    for _ in pb.with_progress_bar(range(100)):
        pass
