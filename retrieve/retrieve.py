# Copyright (c) ECMWF 2020.

from __future__ import absolute_import, unicode_literals

import json
import sys, os

print("TMPDIR={}".format(os.getenv("TMPDIR")))
print("PATH={}".format(os.getenv("PATH")))

from servicelib.process import Process
import json
from ecmwfapi import ECMWFDataServer
from shutil import copyfile



def retrieve(context, arg):
    print("args", arg)
    params = arg
    print('type arg', type(params))
    #fname = "/var/cache/servicelib/t_fc24.grib"
    # res = context.create_result("application/json")
    res = context.create_result(".grib")
    print("res={}".format(res))
    # x = float(arg)
    print('respath', type(res.path))
    arg['target'] = str(res.path)
    server = ECMWFDataServer()    
    server.retrieve(arg)
    #orig_fname = "/code/services/retrieve/t.grib"
    #new_fname = res.path
    #copyfile(orig_fname, new_fname)

    return res


def main():
    from servicelib import service

    service.start_services({"name": "retrieve", "execute": retrieve})


# if __name__ == "__main__":
#     print(run_mv(None, 23))
