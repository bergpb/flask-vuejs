from flask_vuejs.__version__ import __version__


def test_version():
    assert __version__ == "1.0"
