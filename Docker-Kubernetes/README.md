# Simple Docker and Kubernetes Tests

For the following tests:

1. Fork this repository.
2. Make fixes, changes and improvements as described below.
3. Create lightweight documentation in the repositories README.md with how it works and what your changes are.
4. (Optional) Create a public CI pipeline that builds the Docker image (e.g. Using Github Actions, GitLab CI etc....)

It is expected that we should be able to clone your fork, read the instructions / documentation, build the docker image and deploy the image to a simple Kubernetes cluster.

_While you may search the internet for answers, please do not ask others to assist or provide code for you._

---

The following test will require you to do the following:

1. Optimise Dockerfile for caching benefits.
2. Convert the current Dockerfile into a multistage build Dockerfile.
3. Write a simple Kubernetes manifest that could be used to deploy the image to a Kubernetes cluster.

### 1. Fix Dockerfile

The below Dockerfile in its current state does not compile.

1. Fix the Dockerfile to continue.
2. (Optional) Make any optimisations to the Dockerfile as you see fit, make sure you document your reasons.

For all the files that will be required they can be cloned from the following repository - [HERE](https://github.com/sammcj/technical-tests)

```Dockerfile
FROM golang:alpine
ENV GO111MODULE=on
WORKDIR /app
ADD ./ /app
RUN apk update --no-cache
RUN apk add git
RUN go build -o golang-test .
ENTRYPOINT ["/app/golang-test"]
EXPOSE 8000
```

### 2. Multistage build Dockerfile

1. Convert the Dockerfile to use a multistage build.

- The final multi-stage Dockerfile should only have the essential components.
- You should also consider optimisation for caching, and structure in your final solution.

## 3. Simple Kubernetes Deployment

1. Create a simple Kubernetes deployment manifest and add it to the repo.
2. Ensure that your application runs, has sensible configuration to handle failures and potential resourcing issues.
3. Remember to update your documentation.
