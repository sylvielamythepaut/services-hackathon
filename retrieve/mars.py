#!/usr/bin/env python
from ecmwfapi import ECMWFService 
server = ECMWFService("mars", url="https://api.ecmwf.int/v1",key="9182bc70a68dd50cee8ee720d3d69bc8",email="Iain.Russell@ecmwf.int")
# To run this example, you need an API key 
# available from https://api.ecmwf.int/v1/key/

server.execute({
    'class' : 'od',
    'stream' : 'oper',
    'grid'   : '1/1',
    'param'  : 't'},
    target = 't.grib'
)

