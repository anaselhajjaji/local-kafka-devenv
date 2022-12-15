# Introduction

`Kafka` development environment using `Docker`.

[bitnami](https://hub.docker.com/r/bitnami/kafka) images for `Kafka` and `Zookeeper` is used instead of than the `wurstmeister` images because it is easier to setup and more actively maintained.

Note that `Kafka` depends on `Zookeepe`r to store metadata about the topics and partitions. For development purposes, we don't need to interact with it and we can safely ignore it.

`docker-compose` is used as well to manage the containers.
