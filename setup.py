# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "1.0.0"
        self.company_name = "qt.hk"
        self.copyright = "qt.hk"
        self.name = "NVDA Remote Server"

test_wx = Target(
    # used for the versioninfo resource
    description = "NVDA Remote Server",

    # what to build
    script = "nrs.py",

##    icon_resources = [(1, "icon.ico")],
    dest_base = "nrs")

setup(
    options = {"py2exe": {"compressed": 0,
                          "optimize": 0,
                          # "ascii": 1,
                          "bundle_files": 3}},
    data_files = ['server.pem'],
    # zipfile = 'nrs.dll',
    console = [test_wx],
    # windows = [test_wx],
    )
