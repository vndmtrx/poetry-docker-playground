#!/usr/bin/env python

from hello_fastapi import __version__


def version_test():
    assert __version__ == "0.1.0"
