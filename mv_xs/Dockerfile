# syntax=docker/dockerfile:experimental

#
# Build stage: Install eccodes for handling BUFR files.
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
  set -ex \
  && curl https://repo.anaconda.com/pkgs/misc/gpgkeys/anaconda.asc | gpg --dearmor > conda.gpg \
  && install -o root -g root -m 644 conda.gpg /usr/share/keyrings/conda-archive-keyring.gpg \
  && gpg --keyring /usr/share/keyrings/conda-archive-keyring.gpg --no-default-keyring --fingerprint 34161F5BF5EB1D4BFBBB8F0A8AEB4F8B29D82806 \
  && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/conda-archive-keyring.gpg] https://repo.anaconda.com/pkgs/misc/debrepo/conda stable main" > /etc/apt/sources.list.d/conda.list \
  && apt-get update \
  && apt-get install --yes --no-install-suggests --no-install-recommends \
  conda


RUN \   
  set -ex \
  && . /opt/conda/etc/profile.d/conda.sh \
  && conda clean -a \
  && conda install -c conda-forge metview-batch


RUN \
  pip install metview

ENV TMPDIR /var/cache/servicelib

# Copy the Python services code.
COPY *.py /code/services/mv_xs/

# Copy the default configuration file
COPY servicelib.ini /etc/servicelib.ini

USER worker
