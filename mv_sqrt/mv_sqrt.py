# Copyright (c) ECMWF 2020.

from __future__ import absolute_import, unicode_literals

import json
import sys, os

os.environ["METVIEW_PYTHON_START_CMD"] = "/opt/conda/bin/metview"
# os.environ["METVIEW_DEBUG"] = "1"
print('TMPDIR={}'.format(os.getenv("TMPDIR")))

from servicelib.process import Process
import json
import metview as mv

def run_mv(context, arg):
    print(arg)
    #fname = context.get_data(arg)
    fname = "/var/cache/servicelib/T_an+T_fc48"
    #res = context.create_result("application/json")
    res = context.create_result(".nc")
    print('res={}'.format(res))
    #x = float(arg)

    #f = mv.read("/var/cache/servicelibT_an+T_fc48")
    #f = mv.read(arg["path"])
    f = mv.read(fname)

    # nc = mv.mcross_sect(
    #     #bottom_level = 1000.0,
    #     #top_level    = 1,
    #     line         = [-40.1, -105.6, 61.5, 85.1], #lat,lon,lat,lon
    #     data = f
    # )

    nc = f
    print("loc", res.path)
    print(type(nc))
    #os.system("touch " + os.path.dirname(res.path) + "/hello.txt")
    mv.write(res.path, nc)
    print("WRITTEN")
    #res["value"] = x
    return res
    #return json.dumps({"value": mv.sqrt(x)})
    # return str(mv.sqrt(x))

def main():
    from servicelib import service

    service.start_services(
        {"name": "mv_sqrt", "execute": run_mv}
    )
# if __name__ == "__main__":
#     print(run_mv(None, 23))