# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import





def plotslice(context, *args):
    return {}
    



def main():
    from servicelib import service

    service.start_services(
	    {"name": "plotslice", "execute": plotslice},
	    )
