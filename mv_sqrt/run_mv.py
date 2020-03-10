import requests

url = "http://127.0.0.1:8000/services/mv_sqrt"
#data = ["2"]
data = [{"location": "file:///tmp/servicelib-worker-mv-sqrt/T_an+T_fc48"}]

r = requests.post(url, json=data)

print("response={}".format(r.json()))

# curl -v \
#      -X POST \
#      -H 'Content-Type: application/json' \
#      -d '["2"]' \
#      http://127.0.0.1:8000/services/mv_sqrt