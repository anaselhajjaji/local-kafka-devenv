# Introduction

`Kafka` development environment using `Docker`.

[bitnami](https://hub.docker.com/r/bitnami/kafka) images for `Kafka` and `Zookeeper` is used instead of than the `wurstmeister` images because it is easier to setup and more actively maintained.

Note that `Kafka` depends on `Zookeepe`r to store metadata about the topics and partitions. For development purposes, we don't need to interact with it and we can safely ignore it.

`docker-compose` is used as well to manage the containers.

## Getting started

To start open python-devcontainer folder in `vscode` and start the devcontainer.

## Useful commands to interact with Kafka

[kafkacat](https://github.com/edenhill/kcat) tool is used.

- list all topics currently in kafka: `kafkacat -b kafka:9092 -L`
- To test out the producer (The default delimiter between messages is a newline. When you are done, press ctrl-d to send the messages): `kafkacat -b kafka:9092 -t test-topic -P`
- To read the messages you have produced, run the following command to start a consumer: `kafkacat -b kafka:9092 -t test-topic -C`
