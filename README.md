# Introduction

`Kafka` development environment using `Docker`.

[bitnami](https://hub.docker.com/r/bitnami/kafka) images for `Kafka` and `Zookeeper` is used instead of than the `wurstmeister` images because it is easier to setup and more actively maintained.

Note that `Kafka` depends on `Zookeepe`r to store metadata about the topics and partitions. For development purposes, we don't need to interact with it and we can safely ignore it.

`docker-compose` is used as well to manage the containers.

## Getting started

To start open python-devcontainer folder in `vscode` and start the devcontainer.

- Run `consumer.py` that will wait for messages
- Run `producer.py` that will send the messages

## Useful commands to interact with Kafka

[kafkacat](https://github.com/edenhill/kcat) tool is used.

- list all topics currently in kafka: `kafkacat -b kafka:9092 -L`
- To test out the producer (The default delimiter between messages is a newline. When you are done, press ctrl-d to send the messages): `kafkacat -b kafka:9092 -t test-topic -P`
- To read the messages you have produced, run the following command to start a consumer: `kafkacat -b kafka:9092 -t test-topic -C`

## Configure clickhouse

Connect to clickhouse container and run: `clickhouse-client`

Then, create messages queue by running:

```sql
CREATE TABLE default.message_queue
(
  created_at DateTime,
  content String,
  author String
)
ENGINE = Kafka(
  'kafka:9092',
  'posts',
  'clickhouse',
  'JSONEachRow'
) settings kafka_thread_per_consumer = 1, kafka_num_consumers = 1;
```

Now, create the tables by running:

```sql
-- create messages table
CREATE TABLE default.messages
(
  created_at DateTime,
  content String,
  author String
)
ENGINE = MergeTree
ORDER BY created_at;

-- create materialized view
CREATE MATERIALIZED VIEW default.messages_mv
TO default.messages
AS SELECT * FROM default.message_queue;
```
