# Copyright (c) ECMWF 2020.

from __future__ import absolute_import, unicode_literals

import json
import sys, os

os.environ["METVIEW_PYTHON_START_CMD"] = "/opt/conda/bin/metview"
os.environ["PATH"] = os.getenv("PATH") + ":/opt/conda/bin"
# os.environ["METVIEW_DEBUG"] = "1"
print("TMPDIR={}".format(os.getenv("TMPDIR")))
print("PATH={}".format(os.getenv("PATH")))

print("tmp status", os.path.exists(os.getenv("TMPDIR")))

from servicelib.process import Process
import metview as mv

def run_mv(context, arg):
    print("args", arg)
    print("file=", arg["file"])
    fname = context.get_data(arg["file"])
    print("fname=", fname)
    #arg.pop("location")
    #arg.pop("contentLength")
    arg.pop("file")
    params = arg
    res = context.create_result("application/x-netcdf")
    print("res={}".format(res))

    f = mv.read(str(fname))
    params["data"] = f
    print("params=", params)
    nc = mv.mcross_sect(**params)
    mv.write(str(res.path), nc)

    nc_vars = mv.variables(nc)
    nc_param = None
    nc_level_param = None
    for v in nc_vars:
        if v not in ["time", "lat", "lon"] and "_" not in v:
            nc_param = v
            break

    if nc_param:
        for v in nc_vars:
            if nc_param + "_" in v:
                nc_level_param = v
                break

    if not nc_param:
        raise Exception("Parameter to plot not found in resulting netcdf")

    if not nc_level_param:
        raise Exception("Vertical level param not found in resulting netcdf")

    #res["line"] = [0, -180, 0, 180]

    print("nc_param=", nc_param)
    print("nc_level_param=", nc_level_param)

    #NETCDF_MISSING_ATTRIBUTE = _FillValue,
    res["plotter"] = "magics"
    res["verb"] = "netcdf_xy_matrix"
    res["netcdf_value_variable"] = nc_param
    res["netcdf_y_variable"] = nc_level_param
    res["netcdf_dimension_setting_method"] = "index"
    res["netcdf_dimension_setting"] = "time:0"
    res["netcdf_x_variable"] = "lon"
    res["netcdf_x_auxiliary_variable"] = "lat"
    res["netcdf_x_geoline_convention"] = "lonlat"

    return res


def main():
    from servicelib import service

    service.start_services({"name": "mv_xs", "execute": run_mv})


# if __name__ == "__main__":
#     print(run_mv(None, 23))
