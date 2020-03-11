# syntax=docker/dockerfile:experimental

ARG base_tag
ARG os


FROM eccr-dev.ecmwf.int/servicelib/servicelib-${os}:${base_tag}

# Copy the Python services code.
COPY *.py /code/services/plot_slice/

# Copy the default configuration file
COPY servicelib.ini /etc/servicelib.ini

