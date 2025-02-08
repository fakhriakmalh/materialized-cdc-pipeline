import requests
import time

# sync kafka into clickhouse
template_sink = {
  "name": "clickhouse-sink",
  "config": {
    "connector.class": "com.clickhouse.kafka.ClickHouseSinkConnector",
    "tasks.max": "1",
    "topics": "materialize_output_topic",
    "clickhouse.server.url": "http://host.docker.internal:8123",
    "clickhouse.database": "bronze_layer",
    "clickhouse.table": "dummy_table",
    "clickhouse.user": "dwh_user",
    "clickhouse.password": "dwh_password",
    "insert_mode": "INSERT",
    "format": "JSONEachRow",
    "auto.create": "true",
    "auto.evolve": "true"
  }
}

# sync kafka with clickhouse connect by defining url & headers
url = "http://host.docker.internal:8083/connectors"
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=template_sink, headers=headers)
    print("Connector created successfully:", response.json())
except requests.exceptions.RequestException as e:
    print("Error creating connector:", e)

print("finish getting status after syncing kafka with clickhouse")


time.sleep(5)


# list task running at debezium & check status
response_exist = requests.get(url)
tasks = response_exist.json()
print("task existing after sync debezium with kafka")
print(tasks)


# check status
for task in tasks[::-1]:
    url = f"http://host.docker.internal:8083/connectors/{task}/status"
    response = requests.get(url)
    print(response.json())
print("finish getting status at debezium connector")