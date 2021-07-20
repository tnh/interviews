# interviews

These are interview scenarios. Please pick of the scenarios and then submit them to the HR contact.

Do not hesitate to reach out to the HR contact if you have any questions.

1. Docker-Kubernetes

1.1 Optimise Dockerfile for caching benefits.

- Put the mod download layer on top so any codes changes will not overwrite the package download layer

- remove the git install, we seems to no need it.

- disable cgo and set build target to linux

  1.2 Convert the current Dockerfile into a multistage build Dockerfile.

Use distroless as minimal base image to package binary

1.3 Write a simple Kubernetes manifest that could be used to deploy the image to a Kubernetes cluster.

- add hpa to ensure app can scale out

- add liveness to ensure handle app faults
