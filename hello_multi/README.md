# Hello, World! in many languages

This worker implements two services, called `hello` and `bonjour`, which accept
one single argument, and returns the strings `"Hello, <arg>!"` and
`"Bonjour, <arg>!"`.


## Building the container image.

Run the usual:

    $ ./build hello_multi

from the top-level directory.

If you want to ensure a fresh build of the image, bypassing Docker's cache,
do the usual:

    $ env no_cache=1 ./build hello_multi

from the top-level directory.

The container image is built according to the [Dockerfile](./Dockerfile-debian)
in this directory.


## Running the worker

Once you've built the image, do the usual:

    $ ./run hello_multi

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


## Calling the service

You may use cURL or any other HTTP client, like in this example for service
`hello`:

```
$  curl -v \
     -X POST \
     -H 'Content-Type: application/json' \
     -d '["Pepe"]' \
     http://127.0.0.1:8000/services/hello
```

Or in this other example, for service `bonjour`:

```
$  curl -v \
     -X POST \
     -H 'Content-Type: application/json' \
     -d '["Pepe"]' \
     http://127.0.0.1:8000/services/bonjour
```

If you install [jq](https://stedolan.github.io/jq/), you may have a nicer time
deciphering the output of the services:

```
$  curl -v \
     -X POST \
     -H 'Content-Type: application/json' \
     -d '["Pepe"]' \
     http://127.0.0.1:8000/services/hello \
       | jq .
```
