To import bulk data into a cassandra container inside the docker with the help of a python program we have to follow the below steps.

1) Ensure python 2.7 or above is already installed
2) Install python pip
sudo apt-get install python-pip
3) Install cassandra-drriver
sudo pip install cassandra-driver

4) Install numpy

FROM alpine:3.2
ADD repositories /etc/apk/repositories
RUN apk add --update python python-dev gfortran py-pip build-base py-numpy@community

Content of repositories file
http://dl-cdn.alpinelinux.org/alpine/v3.2/main
@community http://dl-cdn.alpinelinux.org/alpine/edge/community


