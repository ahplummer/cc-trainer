FROM python:3.6-alpine

# create a new directory
RUN mkdir /cc-trainer

# download dependencies
RUN apk --no-cache add \
      bash

# update PATH
ENV PATH="PATH=$PATH:$PWD/cc-trainer"

# add the app to run, with the envconsul config
COPY ./*.py /cc-trainer/
COPY ./*.requirements.txt /cc-trainer/
RUN pip install -r /cc-trainer/requirements.txt