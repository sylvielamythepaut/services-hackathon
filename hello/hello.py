# Copyright (c) ECMWF 2020.

from __future__ import absolute_import, unicode_literals


def execute(context, arg):
    return "Hello, {}!".format(arg)


def main():
    from servicelib import service

    service.start_service()
