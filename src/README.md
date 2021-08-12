# Simple Docker and Kubernetes Solution

## Requirements

- Docker
- kubectl
- Make

## Building

This directory contains all the code and tools to build the golang test
application into a docker container. This process can be started by running:

```
make build
```

The Dockerfile is located in the [app](app/Dockerfile) directory. It is a multi-
stage build that builds the app in a golang image, but copies over the compiled
app into a clean alpine image to keep it small.

## Testing

There is a  small test script located in the [tests](tests/) directory. This
tests each endpoint and ensure the responses are correct. It's run by running:

```
make tests
```

This starts up a test container which is defined in the [Dockerfile](tests/Dockerfile).
The [docker-compose.yml](docker-compose.yml) launches the recently built image the runs tests against
it.

## Distribution

Image can be pushed into DockerHub (assuming you are already logged in) by running:

```
make distribute
```

Images are build for AMD64 and Arm64v7 (so I can run on Raspberry Pi). They are 
tags with the SHA of the current HEAD.

## Deploy

A [deployment.yml](k8s/deployment.yaml) describes how the image is deployed into 
a kubernetes cluster. To deploy run the makefile command:

```
make deploy #deploy-pi
```

The [Makefile](Makefile) will deploy the latest tag to the cluster.

## CICD

[Github actions](../.github/workflows/ci.yml) have been implemented that run 
the commands describes above.