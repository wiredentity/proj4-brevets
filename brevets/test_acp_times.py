
from acp_times import open_time, close_time

start = "2026-11-12T07:00:00-08:00"


def test_open_60():
    assert open_time(60, 200, start) == "2026-11-12T08:46:00-08:00"


def test_close_under_60():
    assert close_time(30, 200, start) == "2026-11-12T09:30:00-08:00"


def test_close_60():
    assert close_time(60, 200, start) == "2026-11-12T11:00:00-08:00"


def test_close_200():
    assert close_time(200, 200, start) == "2026-11-12T20:30:00-08:00"


def test_control_over_brevet():
    # Should use the brevet distance if the control is past it
    assert open_time(205, 200, start) == open_time(200, 200, start)
    assert close_time(205, 200, start) == close_time(200, 200, start)


def test_start_control():
    assert open_time(0, 200, start) == "2026-11-12T07:00:00-08:00"
    assert close_time(0, 200, start) == "2026-11-12T08:00:00-08:00"


def test_890():
    assert open_time(890, 1000, start) == "2026-11-13T12:09:00-08:00"
    assert close_time(890, 1000, start) == "2026-11-15T00:23:00-08:00"


def test_finish_times():
    finish_times = {
        200: "2026-11-12T20:30:00-08:00",
        300: "2026-11-13T03:00:00-08:00",
        400: "2026-11-13T10:00:00-08:00",
        600: "2026-11-13T23:00:00-08:00",
        1000: "2026-11-15T10:00:00-08:00"
    }

    for distance in finish_times:
        assert close_time(distance, distance, start) == finish_times[distance]
