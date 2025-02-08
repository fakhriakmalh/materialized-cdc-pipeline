import requests
import time


# sync kafka into clickhouse
template_sink = {
    "name": "clickhouse-sink-connector-dummy-table",
    "config": {
        "connector.class": "com.clickhouse.kafka.connect.ClickHouseSinkConnector",
        "tasks.max": "1",
        "topics": "dummy_table_mv",
        "hostname": "host.docker.internal",
        "port": "8123",
        "username": "dwh_user",  # Ensure this is correct
        "password": "dwh_password",  # Ensure this is correct
        "database": "bronze_layer",
        "table": "dummy_table_mv",  # Ensure this matches the table in ClickHouse
        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
        "key.converter.schemas.enable": "false",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false",
        "consumer.override.auto.offset.reset": "latest"
    }
}


# sync kafka with clickhouse connect by defining url & headers
url = "http://localhost:8083/connectors"
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
    url = f"http://localhost:8083/connectors/{task}/status"
    response = requests.get(url)
    print(response.json())
print("finish getting status at debezium connector")