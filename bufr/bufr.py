# Copyright (c) ECMWF 2020.

from __future__ import absolute_import, unicode_literals

import json

from servicelib.process import Process


def bufr_dump_inline(context, bufr_file):
    fname = context.get_data(bufr_file)

    class p(Process):

        # By default `servicelib` reads only 10 KB of stdout.
        # The BUFR tools we're calling do output way more bytes.
        max_output_size = 10 * 1024 * 1024

        def __init__(self):
            super(p, self).__init__("bufr-dump", ["bufr_dump", "-ja", fname])

        def results(self):
            return json.loads(self.output.decode("utf-8"))

    return context.spawn_process(p())


def bufr_dump_ref(context, bufr_file):
    fname = context.get_data(bufr_file)
    res = context.create_result("application/json")

    class p(Process):

        # By default `servicelib` reads only 10 KB of stdout.
        # The BUFR tools we're calling do output way more bytes.
        max_output_size = 10 * 1024 * 1024

        def __init__(self):
            super(p, self).__init__("bufr-dump", ["bufr_dump", "-ja", fname])

        def results(self):
            with res:
                res.write(self.output)
            return res

    return context.spawn_process(p())


def main():
    from servicelib import service

    service.start_services(
        {"name": "bufr-dump-inline", "execute": bufr_dump_inline,},
        {"name": "bufr-dump-ref", "execute": bufr_dump_ref,},
    )
