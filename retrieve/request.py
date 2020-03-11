import os
from pathlib import Path
import requests


url = "http://127.0.0.1:8000/services/retrieve"
#data_file = "t_fc24.grib"
#data_path_docker = os.path.join("/var/cache/servicelib", data_file)
#data_path = os.path.join("/tmp/servicelib-worker-mv-sqrt", data_file)
#data_size = Path(data_path).stat().st_size



req = {
    'stream'    : "oper",
    'levtype'   : "pl",
    'levelist'  : "1000/850/700/500/300/100",
    'param'     : "t",
    'dataset'   : "interim",
    'step'      : "0",
    'grid'      : "0.75/0.75",
    'time'      : "00",
    'date'      : "2013-09-01",
    'type'      : "an",
    'class'     : "ei",
    'target'    : "interim_2013-09-01.grib"
}

""" req = {  "origin"    : "ecmf",
    "levtype"   : "sfc",
    "number"    : "1",
    "expver"    : "prod",
    "dataset"   : "tigge",
    "step"      : "0/6/12/18",
    "area"      : "70/-130/30/-60",
    "grid"      : "2/2",
    "param"     : "167",
    "time"      : "00/12",
    "date"      : "2020-02-09",
    "type"      : "pf",
    "class"     : "ti"} """


r = requests.post(url, json=[req])

print("response={}".format(r.json()))

# curl -v \
#      -X POST \
#      -H "Content-Type: application/json" \
#      -d '["2"]' \
#      http://127.0.0.1:8000/services/mv_sqrt
