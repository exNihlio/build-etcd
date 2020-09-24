#!/usr/bin/env bash
set -e

which docker &>/dev/null

if [[ $? != 0 ]]; then
  echo "Docker does not appear to be installed"
  echo "Please install Docker or Docker for Mac/Windows and try again"
  exit 1
fi

source .env
# Build the container. This has our RPM in it.
docker build -t ${BUILD_IMAGE}:${BUILD_TAG} .

#Make the build output directory
mkdir -p ${OUTPUT_PATH}

# Run our container
docker run --detach \
           --rm \
           --mount type=bind,source=$(pwd)/${OUTPUT_PATH},target=${CONTAINER_PATH} \
           ${BUILD_IMAGE}:${BUILD_TAG}
