FROM golang:alpine as baseimage
ENV GO111MODULE=on
RUN apk update --no-cache \
&& apk add git


FROM baseimage as build
WORKDIR /app
ADD ./ /app
RUN go build -o golang-test  .
ENTRYPOINT ["/app/golang-test"]
