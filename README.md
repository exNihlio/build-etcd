## What is this?
Build etcd for Centos/RHEL 7 and 8. The only requirements are Docker and Bash
Support for Debian and Ubuntu is coming.

## How does it work?
Ensure that Docker is running.

Change into the distro/release directory you want to build for.

`cd $distro/$release`

Run the `build.sh` script

`bash build.sh`

The `build.sh` script builds the Docker image. The Dockerfile downloads
all the relevant build tools, downloads etcd, and builds an RPM.

When the resulting Docker image is run, with `build.sh`, it copies out the RPM
to a directory on the local filesystem. By the default this is the local directory
`rpm`. This RPM can then be freely installed into your CentOS/RHEL system.

Etcd is built as a single Golang binary. It has no external dependencies.

## Environment variables, etc

When the Dockerfile builds, it downloads the etcd Github release specified by the 
`ETCD_VER` env variable. To build the latest release of etcd, simply update the `ETCD_VER`
variable.

The `.env` file is sourced by the `build.sh` script when it runs. This contains environmental
variables for the `build.sh` script. There are several key variables to address here:

First is `BUILD_TAG`. In this case, this variable is the tag assigned to the built image. While it
is not strictly necessary to increment it with the same `ETCD_VER` in the Dockerfile, failure to do so
may result in confusion. It is advised the keep these two the same.

`OUTPUT_PATH` is the local filesystem directory that the built rpm or dpkg will copied to.

`CONTAINER_PATH` is the directory inside the container that is bound the `OUTPUT_PATH`. The
`CONTAINER_PATH` in `.env` and the `CONTAINER_PATH` in the Dockerfile must match

## The Future

As said before, Debian/Ubuntu support is coming. Possibly others.

The next goal is support for Amazon CodeBuild, with the ability to push to S3 and/or S3 compatible
object store.
