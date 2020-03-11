# syntax=docker/dockerfile:experimental

#
# Build stage:
#

ARG base_tag

FROM eccr-dev.ecmwf.int/servicelib/servicelib:${base_tag}

# Install ecbuild and other build-time dependencies.

USER root

RUN \
  set -ex \
  && apt-get update \
  && apt-get install --yes  \
  ca-certificates \
  curl \
  gpg \
  expat

RUN \
  pip install ecmwf-api-client

ENV TMPDIR /var/cache/servicelib

# Copy the Python services code.
COPY *.py /code/services/retrieve/

#COPY key /root/.ecmwfapirc

# Copy the default configuration file
COPY servicelib.ini /etc/servicelib.ini
