# Generating the templates:

clone https://github.com/sylvielamythepaut/swagger-py-codegen.git


swagger_py_codegen --swagger-doc multi-hello-api.yaml multi_hello -tlp servicelib

# `servicelib` examples

This repository hosts several examples of services based on
[servicelib](https://git.ecmwf.int/scm/web/servicelib).

* [hello](./hello/): A worker hosting one simple service.
* [hello_multi](./hello_multi/): A worker hosting two simple services.
* [bufr](./bufr/): Two services for dumping BUFR files in JSON format.

Each directory contains instructions on how to build, run and call the
services.


## Getting started

### Create an Open Api Schema
You can use the swagger editor to draft you schema at https://editor.swagger.io/ and save it as ``openapi_myapp.yaml``.

### Display Schema-Yaml in Browser
Assuming you have your schema file at `/localdirectory/my-app/openapi/openapi_myapp.yaml`. You can run the swagger-ui Docker image and mount the local directory into the container:
```bash
docker run --rm -p 8083:8080 -v /localdirectory/my-app/openapi/openapi_myapp.yaml:/yaml/openapi.yaml --env SWAGGER_JSON=/yaml/openapi.yaml swaggerapi/swagger-ui:v3.25.0
```
You can now access an interactive website with your schema and the ability to test your api via http://localhost:8083 .

### Clone this repository

As usual:

    $ git clone https://git.ecmwf.int/scm/web/servicelib-examples

or, if you prefer SSH access:

    $ git clone ssh://git@git.ecmwf.int/web/servicelib-examples.git


### Install Docker

Either [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
or the Docker Engine for [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/),
[Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/) or any other
flavour or Linux you might be running.


### Access to ECMWF's container registry

The base `servicelib` image is hosted at [eccr-dev.ecmwf.int](https://eccr-dev.ecmwf.int/).
You need to be able to pull it in order to build these examples. Log in with
your usual ECMWF user name and password.

The X.509 certificate for `eccr-dev.ecmwf.int` has been issued by the
[QuoVadis Global SSL ICA G3](https://www.quovadisglobal.com/QVRepository/DownloadRootsAndCRL/QuoVadisGlobalSSLICAG3-PEM.aspx)
certificate authority. You need to install the CA'a certificate in your system.

On Linux:

    $ sudo mkdir -p /etc/docker/certs.d/eccr-dev.ecmwf.int
    $ sudo cp <the-pem-file-from-above> /etc/docker/certs.d/eccr-dev.ecmwf.int/ca.crt

On Mac: [Add to your keychain](https://support.apple.com/en-gb/guide/keychain-access/kyca2431/mac)
the PEM file linked above. Alternatively, from the command line:

    $ sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain <the-pem-file-from-above>

Then you have to restart Docker for Mac.


### Log in into `eccr-dev.ecmwf.int`

Once you've added QuoVadis CA cert to your local Docker installation, you need
to log in before yu may start pulling images. On a terminal, do the following:

    $ docker login eccr-dev.ecmwf.int

Use your usual ECMWF user name and password.


### Add your ECMWF credentials to `~/.netrc`

Building the example worker [bufr](./bufr/) requires cloning the ecCodes
Git repository from within the Docker image build process. One way to let
Docker do this is by adding your ECMWF credentials to your `~/.netrc`:

On Linux:

    $ touch ~/.netrc
    $ chmod 0600 ~/.netrc
    $ cat >> ~/.netrc <<EOF

    machine git.ecmwf.int
    login <your-user-id>
    password <your-password>
    EOF

On Mac: I don't know, but the snippet above might work.


### Build the worker images

Detailed instructions in each worker directory. In a nutshell, the command

    $ ./build hello

will build both Debian and CentOS 7 images for worker `hello`.


### Running the worker images

Detailed instructions in each worker directory, as well, together with sample
requests you may do with cURL.

In a nutshell, the command

    $ ./run hello

will run the Debian image for worker `hello`. If you want to run the CentOS 7
image, do instead:

    $ env os=centos7 ./run hello
