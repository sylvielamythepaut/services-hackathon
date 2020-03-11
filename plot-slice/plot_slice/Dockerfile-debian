# syntax=docker/dockerfile:experimental

ARG base_tag
ARG os


FROM ecmwf/magics:4.2.6 AS build 

# Open current image for working:
FROM eccr-dev.ecmwf.int/servicelib/servicelib-${os}:${base_tag}

# Copy the Python services code.
COPY *.py /code/services/plot_slice/

# Copy the default configuration file
COPY servicelib.ini /etc/servicelib.ini

# Install run-time depencencies.
# Delete resources after installation
RUN set -ex \
    && apt-get update \
    && apt-get install --yes --no-install-suggests --no-install-recommends \
       ca-certificates \
       curl \
       ghostscript \
       imagemagick \
       ksh \
       libarmadillo9 \
       libbz2-1.0 \
       libcairo-gobject2 \
       libcairo-script-interpreter2 \
       libcairo2 \
       libcroco3 \
       libcurl4 \
       libexif12 \
       libexpat1 \
       libfontconfig1 \
       libfreetype6 \
       libfribidi0 \
       libgdal20 \
       libgeoip1 \
       libgeos-c1v5 \
       libgif7 \
       libgomp1 \
       libgssrpc4 \
       libharfbuzz0b \
       libhdf5-103 \
       libicu63    \
       libilmbase23 \
       libjbig0 \
       libjpeg62-turbo \
       libjs-jquery \
       liblcms2-2 \
       liblqr-1-0 \
       libncurses5 \
       libnetcdf13 \
       libopenexr23 \
       libpangocairo-1.0-0 \
       libpangoxft-1.0-0 \
       libpcre3 \
       libpcrecpp0v5 \
       libpng16-16 \
       libproj13 \
       libreadline7 \
       libsqlite3-0 \
       libssl1.1 \
       libtiff5 \
       libtiffxx5 \
       libwebp6 \
       libxft2 \
       libxml2 \
       libxslt1.1 \
       poppler-utils \
       rsync \
       zlib1g \
    && rm -rf /var/lib/apt/lists/*


# Copy Python run-time and ECMWF softwate.
COPY --from=build /usr/local/share/eccodes/ /usr/local/share/eccodes/
COPY --from=build /usr/local/share/magics/ /usr/local/share/magics/
COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY --from=build /usr/local/lib/ /usr/local/lib/

# Ensure shared libs installed by the previous step are available.
RUN set -ex \
    && /sbin/ldconfig

# Configure Python runtime.
ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

