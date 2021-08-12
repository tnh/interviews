FROM golang:alpine AS build

# Better caching
ENV GO111MODULE=on
WORKDIR /app
ARG opts

# Less layers
RUN apk update --no-cache \
    && apk add git

ADD . /app/
RUN printenv \
    && env ${opts} go build -o golang-test .

# Use clean alpine to keep smallest possible
FROM alpine

# Single layer
RUN apk update --no-cache \
    &&  apk add git \
    && mkdir /app

# Moving up for caching
ENTRYPOINT ["/app/golang-test"]
EXPOSE 8000

COPY --from=build /app/golang-test /app