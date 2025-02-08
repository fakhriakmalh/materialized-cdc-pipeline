# Real-Time CDC Pipeline with Materialize and Kafka

[![Materialize](https://img.shields.io/badge/Materialize-3.0.1-blue)](https://materialize.com/)
[![ClickHouse](https://img.shields.io/badge/ClickHouse-24.8-green)](https://clickhouse.com/)
[![Debezium](https://img.shields.io/badge/Debezium-2.7.3-red)](https://debezium.io/)
[![Kafka](https://img.shields.io/badge/Kafka-3.6.0-blue)](https://kafka.apache.org/)


A real-time Change Data Capture (CDC) pipeline demonstrating:
- **MySQL** database to get changes capture
- **Materialize** for stream processing database ()
- **Kafka** for event streaming
- **Debezium** for connector into Clickhouse 
- **ClickHouse** for analytics storage (OLAP)

## Key features
- Real-time data transformation with Materialize SQL
- Automatic schema evolution handling
- Exactly-once processing semantics
- Millisecond-latency analytics in ClickHouse

## Architecture Overview
MySQL -> Materialize -> Kafka -> Debezium -> Clickhouse


## Why using materialized
Using Materialize as a streaming database provides several advantages, particularly for real-time analytics and event-driven applications. Here’s why Materialize is a great choice for this use case:

1. Unlike traditional databases that execute queries on static data, Materialize continuously processes and updates query results as new data arrives. So, no need to manually refresh materialized view

2. Materialize is wire-compatible with PostgreSQL. You can use standard PostgreSQL drivers and tools

3. Strong support for streaming data sources, like kafka, debezium, CDC, etc. 

4. Materialize support CDC which make us easier to capture without resource extensive (https://materialize.com/docs/ingest-data/mysql/)

## Quick start

- Clone Repository
```
git clone https://github.com/fakhriakmalh/materialized-cdc-pipeline.git
cd materialize-cdc-pipeline
```

- Start the infrastructure using docker-compose

```
docker-compose up -d
```

- Set mysql to binlog enable 
```
docker exec -it mysql-container /bin/bash
mysql -u root -p (type the pass)
GRANT RELOAD, FLUSH_TABLES ON *.* TO '<username>'@'%';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '<username>'@'%';
FLUSH PRIVILEGES;

```

- Go to dbeaver (or any db management app) to create dummy table and run from **mysql-query.sql**

- Access materialized UI at host:6875 or go into dbaver to run some queries from **mtz-query.sql**

- Run debezium-new.py to connect clickhouse with kafka topic using debezium. Inside script contains payload hit the debezium API.

