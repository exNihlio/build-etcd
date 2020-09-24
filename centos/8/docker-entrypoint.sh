#!/usr/bin/env bash

set -e

cp /root/rpmbuild/RPMS/x86_64/*.rpm ${CONTAINER_PATH}/
