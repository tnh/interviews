FROM golang:alpine AS build

ENV GO111MODULE=on

WORKDIR /app

ADD ./ /app

RUN apk update --no-cache

RUN apk add git

RUN go build -o golang-test  .

# Use clean alpine to keep smallest possible
FROM alpine

RUN apk update --no-cache \
    &&  apk add git \
    && mkdir /app

WORKDIR /app

COPY --from=build /app/golang-test /app

ENTRYPOINT ["/app/golang-test"]

EXPOSE 8000
