# BUFR services

This worker implements two BUFR services:

* `bufr-dump-inline` accepts a reference to an HTTP-accessible BUFR file,
  and returns the output of the `bufr_dump -ja` command-line tool as a JSON
  object.
* `bufr-dump-ref`, which does the same job as `bufr-dump-inline`, but
   returns instead a reference to an HTTP-accessible JSON file.


## Building the container image.

Run the usual:

    $ ./build bufr

from the top-level directory.

If you want to ensure a fresh build of the image, bypassing Docker's cache,
do the usual:

    $ env no_cache=1 ./build bufr

from the top-level directory.

The container image is built according to the [Dockerfile](./Dockerfile-debian)
in this directory.


## Running the worker

Once you've built the image, do the usual:

    $ ./run bufr

from the top-level directory.

This will start a container process which:

* Listens on `http://127.0.0.1:8000` for calls to services and results
  downloads.
* Bind-mounts the worker's [config file](./servicelib.ini), so that you may
  tweak the worker's settings without having to rebuild the container image.
* Bind-mounts the host directory `/tmp/servicelib-worker-bufr` as
  `/var/cache/servicelib` inside the container process, where the worker
  generates its results and temporary files.
* Bind-mounts the worker's Python source code, so that any change in it will
  be detected by the worker process, without having to restart the container.

The worker's configuration is specified in the [servicelib.ini](./servicelib.ini)
config file.


## Calling the services

Both `bufr-dump-inline` and `bufr-dump-ref` expect a reference to an
HTTP-accessible BUFR file as their only argument, like this one:

```
{
    "location": "http://download.ecmwf.org/test-data/eccodes/data/bufr/airs_57.bufr"
}
```

The [eccodes test data](http://download.ecmwf.org/test-data/eccodes/data/bufr/)
collection hosts plenty of valid and invalid BUFR files that you may use as
input to the services implemented here.

You may use cURL or any other HTTP client, like in this example:

```
$  curl -v \
     -X POST \
     -H 'Content-Type: application/json' \
     -d '[{"location": "http://download.ecmwf.int/test-data/eccodes/data/bufr/airs_57.bufr"}]' \
     http://127.0.0.1:8000/services/bufr-dump-ref
```

If you install [jq](https://stedolan.github.io/jq/), you may have a nicer time
deciphering the output of the services:

```
$  curl -v \
     -X POST \
     -H 'Content-Type: application/json' \
     -d '[{"location": "http://download.ecmwf.int/test-data/eccodes/data/bufr/airs_57.bufr"}]' \
     http://127.0.0.1:8000/services/bufr-dump-ref \
       | jq .
```
