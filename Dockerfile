FROM jazzdd/alpine-flask:latest
MAINTAINER Sheshagiri Rao Mallipedhi <msheshagirirao@gmail.com>
COPY app.py /app/app.py
# entrypoint is already defined in the base image.