# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

import os
from Magics.macro import *
import netCDF4 as nc



def plotslice(context, source, variable):
    local_source = source

    result = context['result']

    output_inst = output(   
                output_formats = ['png'],
                output_name = os.path.basename(result),
                output_name_first_page_number = "off"
        )
    
    lat_varname = 'lat'
    lon_varname = 'lon'
    plev_varname = 't_lev'

    # Definition of the netCDF data and interpretation
    # Populate the following from meta
    data = mnetcdf(netcdf_filename = source,
      netcdf_value_variable = variable,
      netcdf_type = "matrix",
      #netcdf_field_scaling_factor = scale_factor,
      netcdf_y_variable = plev_varname,
      netcdf_x_variable = lon_varname,
      netcdf_x_auxiliary_variable = lat_varname
    )
    print(data)
    
    # file variable names from input
    inf = nc.Dataset(local_source, 'r')
    latmin,latmax = inf.variables[lat_varname][0], inf.variables[lat_varname][-1]
    lonmin,lonmax = inf.variables[lon_varname][0], inf.variables[lon_varname][-1]
    plevmax,plevmin = inf.variables[plev_varname][0,0], inf.variables[plev_varname][-1,-1]
    ##inf.close()

    print(type(latmin))
    latmin,latmax = 30, 50
    lonmin,lonmax = 10, 40
    plevmax,plevmin = 10, 1000
    
    # Setting the cartesian view
    projection = mmap(
        subpage_map_projection='cartesian',
        subpage_x_axis_type='geoline',
        subpage_y_axis_type='logarithmic',   # Populate from metadata?
        subpage_x_min_latitude=latmin,  
        subpage_x_max_latitude=latmax,
        subpage_x_min_longitude=lonmin,
        subpage_x_max_longitude=lonmax,
        subpage_y_min=plevmin,
        subpage_y_max=plevmax,
        )
    print(projection)
    # Vertical axis
    vertical = maxis(
        axis_orientation='vertical',
        axis_grid='on',
        axis_type='logarithmic',
        axis_tick_label_height=0.4,
        axis_tick_label_colour='charcoal',
        axis_grid_colour='charcoal',
        axis_grid_thickness=1,
        axis_grid_reference_line_style='solid',
        axis_grid_reference_thickness=1,
        axis_grid_line_style='dash',
        axis_title='on',
        axis_title_text='Pressure',
        axis_title_height=0.6,
        )
    print(vertical)
    # Horizontal axis
    horizontal = maxis(
        axis_orientation='horizontal',
        axis_type='geoline',
        axis_tick_label_height=0.4,
        axis_tick_label_colour='charcoal',
        axis_grid='on',
        axis_grid_colour='charcoal',
        axis_grid_thickness=1,
        axis_grid_line_style='dash',
        )
    print(horizontal)
    
    contour = mcont()
    plot(output_inst, projection, horizontal, vertical, data, contour)    

    return result
    



def main():
    location = '/perm/ma/maec/Work_Proj/WEB_services_hackathon/servicelib-examples/mv_xs/res.nc'
    variable = 't'
    plotslice( {'result':'res.png'}, location, variable)

if __name__=='__main__':
    main()
