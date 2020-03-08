# Copyright (c) ECMWF 2020.

from __future__ import absolute_import, unicode_literals


def hello(context, arg):
    return "Hello, {}!".format(arg)


def bonjour(context, arg):
    return "Bonjour, {}!".format(arg)


def main():
    from servicelib import service

    service.start_services(
        {"name": "hello", "execute": hello}, {"name": "bonjour", "execute": bonjour},
    )
