# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

import os
from Magics.macro import *




def plotslice(context, source):
    source = context.get_data(source)

    result = context.create_result('.png')

    output = output(   
                output_formats = ['png'],
                output_name = os.path.basename(result.path),
                output_name_first_page_number = "off"
        )
    # Setting the cartesian view
    projection = mmap(
        subpage_map_projection='cartesian',
        subpage_x_axis_type='geoline',
        subpage_y_axis_type='logarithmic',
        subpage_x_min_latitude=50.,
        subpage_x_max_latitude=30.,
        subpage_x_min_longitude=-90.,
        subpage_x_max_longitude=-60.,
        subpage_y_min=1020.,
        subpage_y_max=200.,
        )
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
    # Definition of the netCDF data and interpretation
    data = mnetcdf(netcdf_filename = result.path,
      netcdf_value_variable = "p13820121030000000000001",
      netcdf_field_scaling_factor = 100000.,
      netcdf_y_variable = "levels",
      netcdf_x_variable = "longitude",
      netcdf_x_auxiliary_variable = "latitude"
    )
    contour = mcont()
    plot(output, projection, horizontal, vertical, data, contour)    

    return result
    



def main():
    from servicelib import service

    service.start_services(
	    {"name": "plotslice", "execute": plotslice},
	    )
