# base image
FROM ubuntu:latest

# configure env
ENV DEBIAN_FRONTEND 'noninteractive'


# update apt, install core apt dependencies and delete the apt-cache
# note: this is done in one command in order to keep down the size of intermediate containers
RUN apt-get update && \
    apt-get install -y locales iputils-ping curl wget git-core htop python-pip vim unzip && \
    rm -rf /var/lib/apt/lists/*


# install libraries
RUN pip install awscli
RUN pip install boto3

# everything should be installed under the root user's home directory
WORKDIR /root

ADD . /root

RUN ls -all
