import os
from pathlib import Path
import requests

url = "http://127.0.0.1:8080/services/retrieve"

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
    #'target'    : "interim_2013-09-01.grib"
}

r = requests.post(url, json=[req])
data = r.json()
print("response={}".format(data))



# curl -v \
#      -X POST \
#      -H "Content-Type: application/json" \
#      -d '["2"]' \
#      http://127.0.0.1:8000/services/mv_sqrt




url = "http://127.0.0.1:8000/services/mv_xs"
# data_file = "t_fc24.grib"
# data_path_docker = os.path.join("/var/cache/servicelib", data_file)
# data_path = os.path.join("/tmp/servicelib-worker-mv-xs", data_file)
# data_size = Path(data_path).stat().st_size

data = [
    {
     "file": data,
     "line": [-40.1, -105.6, 61.5, 85.1],
     "bottom_level" : 1000,
     "top_level": 50 
    }
    ]

r = requests.post(url, json=data)

print("response={}".format(r.json()))

# curl -v \
#      -X POST \
#      -H 'Content-Type: application/json' \
#      -d '["2"]' \
#      http://127.0.0.1:8000/services/mv_sqrt
