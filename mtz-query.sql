-- set password secret
CREATE SECRET mysqlpass AS 'smilepwd';

-- set new connection
create connection mysql_conn to MYSQL (
	HOST 'host.docker.internal',
	PORT 3306,
	USER 'smileuser',
	PASSWORD SECRET mysqlpass
);


-- set new source
CREATE SOURCE mz_source
  FROM MYSQL CONNECTION mysql_conn
  FOR TABLES (smiledb.dummy_table);
 
-- set MV that directly reflect
CREATE MATERIALIZED VIEW dummy_table_mv AS
SELECT id, name, age, city,
	TO_CHAR(updated_at, 'YYYY-MM-DD HH24:MI:SS.MS') AS updated_at,
    CASE 
        WHEN age > 30 THEN 'Old'
        ELSE 'Young'
    END AS category
FROM dummy_table ;



-- check the table
select * from dummy_table_mv

-- set connection to kafka
CREATE CONNECTION kafka_connection TO KAFKA (
    BROKER 'host.docker.internal:9092',
    SECURITY PROTOCOL = 'PLAINTEXT'
);


-- sink into kafka topic
CREATE SINK dummy_table_mv_json
FROM dummy_table_mv
INTO KAFKA CONNECTION kafka_connection (TOPIC 'dummy_table_mv')
KEY(id)
FORMAT JSON
ENVELOPE UPSERT;