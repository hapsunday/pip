# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os
import sys

_TMP_CA_FILE = None


def where():
    global _TMP_CA_FILE
    if not getattr(sys, 'oxidized', False):
        f = os.path.dirname(__file__)
        return os.path.join(f, 'cacert.pem')
    elif _TMP_CA_FILE is not None:
        return _TMP_CA_FILE
    else:
        from tempfile import mkstemp
        from importlib.resources import open_binary
        fd, path = mkstemp()

        with open(path, 'wb') as f:
            with open_binary('pip._vendor.certifi', 'cacert.pem') as fh:
                f.write(fh.read())
                pass
            pass
        _TMP_CA_FILE = path
        os.close(fd)
