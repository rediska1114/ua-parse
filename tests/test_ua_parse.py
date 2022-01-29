import json
import functools
import parametrize_from_file

from ua_parse import parse_ua


@functools.wraps(json.load)
def _load_json(path):
    with open(path) as f:
        data = json.load(f)
        return {'data': data}


parametrize_from_file.add_loader('.json', _load_json)


def test_none_ua():
    assert parse_ua(None) is not None


def test_empty_ua():
    assert parse_ua('') is not None


@parametrize_from_file('assets/browsers.json', 'data')
def test_browsers(desc, ua, expect):
    res = parse_ua(ua)

    assert res['browser'] == expect


@parametrize_from_file('assets/cpus.json', 'data')
def test_cpus(desc, ua, expect):
    res = parse_ua(ua)

    assert res['cpu'] == expect


@parametrize_from_file('assets/devices.json', 'data')
def test_devices(desc, ua, expect):
    res = parse_ua(ua)

    assert res['device'] == expect


@parametrize_from_file('assets/engines.json', 'data')
def test_engines(desc, ua, expect):
    res = parse_ua(ua)

    assert res['engine'] == expect


@parametrize_from_file('assets/os.json', 'data')
def test_os(desc, ua, expect):
    res = parse_ua(ua)

    assert res['os'] == expect
