from utils import validators


def test_hoper_os():
    assert validators.hoper_os('hoper')


def test2_hoper_os():
    assert not validators.hoper_os('pp')
