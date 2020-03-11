# Copyright (c) ECMWF 2020.

from __future__ import absolute_import, unicode_literals

import json
import sys, os

os.environ["METVIEW_PYTHON_START_CMD"] = "/opt/conda/bin/metview"
os.environ["PATH"] = os.getenv("PATH") + ":/opt/conda/bin"
# os.environ["METVIEW_DEBUG"] = "1"
print("TMPDIR={}".format(os.getenv("TMPDIR")))
print("PATH={}".format(os.getenv("PATH")))

from servicelib.process import Process
import json
#import metview as mv


def run_mv(context, arg):
    print("args", arg)
    fname = context.get_data(arg)
    arg.pop("location")
    params = arg
    res = context.create_result("application/x-netcdf")
    print("res={}".format(res))

    macro_txt = """
    #Metvie macro
f = read("{}")

nc = mcross_sect(
    bottom_level : {},
    top_level    : {},
    line         : {},
    data : f
)

write("{}", nc)
""".format(
    fname, 
    params.get("bottom_level", 1000),
    params.get("top_level", 50),
    params.get("line", "[0, -180, 0, 180]"),
    res.path)

    print("macro_txt=", macro_txt)
    macro_file = "/var/cache/servicelib/xs.mv"
    with open(macro_file, "w") as f:
        f.write(macro_txt)

    cmd = "metview -slog -nocreatehome -b {}".format(macro_file)
    print("cmd=", cmd)
    os.system(cmd)
    print('res file status=', os.path.exists(res.path))

    return res

    # f = mv.read("/var/cache/servicelibT_an+T_fc48")
    # f = mv.read(arg["path"])
    #f = mv.read(fname)

    # nc = mv.mcross_sect(
    #     #bottom_level = 1000.0,
    #     #top_level    = 1,
    #     line         = [-40.1, -105.6, 61.5, 85.1], #lat,lon,lat,lon
    #     data = f
    # )


def main():
    from servicelib import service

    service.start_services({"name": "mv_sqrt", "execute": run_mv})


# if __name__ == "__main__":
#     print(run_mv(None, 23))
