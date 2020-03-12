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

TITLE = {
        "text_font_size": 1.1, "text_colour": 'black',
        #"text_line_space_ratio": 0.1
        }

LEGEND = {
        "legend_title": "on",
        "legend_text_colour": "black",
        "legend_title_text": "Atmospheric cross-section of temperature (K)",
        "legend_title_font_size": 0.6,
        "legend_entry_border": "off",
        "legend_values_list": [200.,225,250,275,300],
        "legend_text_composition": "user_text_only",
        "legend_display_type": 'continuous',
        }
CONTOUR = { 
        "legend": "on",
        "contour": "off",
        "contour_label": "off",
        "contour_shade": "on",
        "contour_shade_method" : "area_fill",
        "contour_level_selection_type": "list",
        "contour_shade_colour_method": "gradients",
        "contour_level_list": [-1e6,200,225,250,300,1e6],
        "contour_gradients_colour_list" : ["#30123b","#30123b","#18ddc2","#fbb637","#850702"],
        "contour_gradients_step_list": [1,25,25,50,1],
      }

def plotslice(context, source, variable):
    local_source = context.get_data(source)

    result = context.create_result('.png')

    output_inst = output(   
                output_formats = ['png'],
                output_name = os.path.basename(result.path),
                output_name_first_page_number = "off"
        )
    
    lat_varname = 'lat'
    lon_varname = 'lon'
    plev_varname = 't_lev'

    # Definition of the netCDF data and interpretation
    # Populate the following from meta
    data = mnetcdf(netcdf_filename = local_source,
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
    lats = inf.variables[lat_varname][:].flatten()
    lons = inf.variables[lon_varname][:].flatten()
    plevs = inf.variables[plev_varname][:].flatten()
    inf.close()
    latmin,latmax = lats[0], lats[-1]
    lonmin,lonmax = lons[0], lons[-1]
    plevmax,plevmin = plevs[0], plevs[-1]
    del lats, lons, plevs
    print(latmin, type(latmin))
    
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
    
    title = mtext(
            **TITLE
            )
    contour = mcont(
            **CONTOUR
            )
    legend = mlegend(
            **LEGEND
            )
    plot(output_inst, projection, horizontal, vertical, data, contour,
            title, legend)

    return result
    



def main():
    from servicelib import service

    service.start_services(
	    {"name": "plotslice", "execute": plotslice},
	    )


