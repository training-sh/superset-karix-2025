docker compose exec -it clickhouse  bash


docker compose exec -it clickhouse clickhouse-client

CREATE DATABASE tpch;



```
CREATE TABLE IF NOT EXISTS tpch.regions
(
  r_regionkey Int32,
  r_name String,
  r_comment String
)
ENGINE = MergeTree()
ORDER BY r_regionkey;
```

```
CREATE TABLE IF NOT EXISTS tpch.nations
(
  n_nationkey Int32,
  n_name String,
  n_regionkey Int32,
  n_comment String
)
ENGINE = MergeTree()
ORDER BY n_nationkey;
```

```
CREATE TABLE IF NOT EXISTS tpch.suppliers
(
  s_suppkey Int32,
  s_name String,
  s_address String,
  s_nationkey Int32,
  s_phone String,
  s_acctbal Decimal(15,2),
  s_comment String
)
ENGINE = MergeTree()
ORDER BY s_suppkey;
```


```
CREATE TABLE IF NOT EXISTS tpch.customers
(
  c_custkey Int32,
  c_name String,
  c_address String,
  c_nationkey Int32,
  c_phone String,
  c_acctbal Decimal(15,2),
  c_mktsegment String,
  c_comment String
)
ENGINE = MergeTree()
ORDER BY c_custkey;
```


```
CREATE TABLE IF NOT EXISTS tpch.parts
(
  p_partkey Int32,
  p_name String,
  p_mfgr String,
  p_brand String,
  p_type String,
  p_size Int32,
  p_container String,
  p_retailprice Decimal(15,2),
  p_comment String
)
ENGINE = MergeTree()
ORDER BY p_partkey;
```


```
CREATE TABLE IF NOT EXISTS tpch.parts_suppliers
(
  ps_partkey Int32,
  ps_suppkey Int32,
  ps_availqty Int32,
  ps_supplycost Decimal(15,2),
  ps_comment String
)
ENGINE = MergeTree()
ORDER BY (ps_partkey, ps_suppkey);
```


```
CREATE TABLE IF NOT EXISTS tpch.orders
(
  o_orderkey Int32,
  o_custkey Int32,
  o_orderstatus String,       -- CHAR(1) -> String
  o_totalprice Decimal(15,2),
  o_orderdate Date,
  o_orderpriority String,
  o_clerk String,
  o_shippriority Int32,
  o_comment String
)
ENGINE = MergeTree()
ORDER BY o_orderkey;
```


```
CREATE TABLE tpch.lineitems
(
  l_orderkey    Int32,
  l_partkey     Int32,
  l_suppkey     Int32,
  l_linenumber  Int16,
  l_quantity    Decimal64(2),
  l_extendedprice Decimal64(2),
  l_discount    Decimal32(4),
  l_tax         Decimal32(4),
  l_returnflag  LowCardinality(String),
  l_linestatus  LowCardinality(String),
  l_shipdate    Date,
  l_commitdate  Date,
  l_receiptdate Date,
  l_shipinstruct LowCardinality(String),
  l_shipmode     LowCardinality(String),
  l_comment      String
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(l_shipdate)
ORDER BY (l_shipdate, l_orderkey, l_linenumber)
SETTINGS index_granularity = 4096;

```


```
exit
```


Now you must be in clickhouse bash or run below command to enter into clickhouse bash..
before running, validate whether you already into clickhouse bash..

```
docker compose exec -it clickhouse  bash
```

INSERT DATA USING STREAMING CLIENT 


```
clickhouse-client --query="INSERT INTO tpch.regions FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/regions.csv
```


```
clickhouse-client --query="INSERT INTO tpch.nations FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/nations.csv
```




```
clickhouse-client --query="INSERT INTO tpch.customers FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/customers.csv
```

```
clickhouse-client --query="INSERT INTO tpch.parts FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/parts.csv
```

```
clickhouse-client --query="INSERT INTO tpch.parts_suppliers FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/parts_suppliers.csv
```

```
clickhouse-client --query="INSERT INTO tpch.suppliers FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/suppliers.csv
```

```
clickhouse-client --query="INSERT INTO tpch.orders FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/orders.csv
```


```
clickhouse-client --query="INSERT INTO tpch.lineitems FORMAT CSVWithNames" < /var/lib/clickhouse/user_files/tpch_csv/lineitems.csv
```




-- verify

```
docker compose exec -it clickhouse clickhouse-client
```

```
SELECT count(*) FROM tpch.regions;
SELECT * FROM tpch.regions ORDER BY r_regionkey LIMIT 5;
```



```
SELECT count(*) FROM tpch.nations;
```

```
SELECT * FROM tpch.nations ORDER BY n_nationkey LIMIT 5;
```

```
SELECT count(*) FROM tpch.suppliers;
```

```
SELECT * FROM tpch.suppliers ORDER BY s_suppkey LIMIT 5;
```

```
SELECT count(*) FROM tpch.orders;
```

```
SELECT * FROM tpch.orders ORDER BY o_orderkey LIMIT 5;
```

```
SELECT count(*) FROM tpch.lineitems;
```

```
SELECT * FROM tpch.lineitems ORDER BY l_orderkey, l_linenumber LIMIT 5;
```

==============


Denormalize or create materialized views for common Superset queries

```
CREATE MATERIALIZED VIEW tpch.hourly_sales_mv
ENGINE = AggregatingMergeTree()
PARTITION BY toYYYYMM(dt)
ORDER BY (dt, country_id, product_id)
AS
SELECT
    toStartOfHour(l_shipdate) AS dt,
    n_nationkey AS country_id,
    l_partkey AS product_id,
    sumState(l_extendedprice) AS sum_price_state,
    sumState(l_quantity) AS sum_qty_state
FROM tpch.lineitems
JOIN tpch.orders ON l_orderkey = o_orderkey
JOIN tpch.customers ON o_custkey = c_custkey
JOIN tpch.nations ON c_nationkey = n_nationkey
GROUP BY dt, country_id, product_id;
```


==========

-- preview CSV
```
SELECT * FROM file('tpch_csv/regions.csv','CSVWithNames') LIMIT 5;
```

-- server-side import (optional)
```
INSERT INTO tpch.regions
SELECT * FROM file('tpch_csv/regions.csv','CSVWithNames');
```

recommended client-side streaming (run from container bash)


# suppliers


```
SELECT * FROM file('tpch_csv/suppliers.csv','CSVWithNames') LIMIT 5;
```

-- optional server-side import
```
INSERT INTO tpch.suppliers
SELECT * FROM file('tpch_csv/suppliers.csv','CSVWithNames');
```


```
SELECT count(*) FROM tpch.customers;
```

```
SELECT * FROM tpch.customers ORDER BY c_custkey LIMIT 5;
```


```
SELECT count(*) FROM tpch.parts;
SELECT * FROM tpch.parts ORDER BY p_partkey LIMIT 5;
```


```
SELECT count(*) FROM tpch.parts_suppliers;
```
```
SELECT * FROM tpch.parts_suppliers ORDER BY ps_partkey, ps_suppkey LIMIT 5;
```


```
SELECT count(*) FROM tpch.lineitems;
```

```
SELECT * FROM tpch.lineitems ORDER BY l_orderkey, l_linenumber LIMIT 5;
```



A target AggregatingMergeTree table (holds aggregate states).

A safe backfill INSERT ... SELECT (casts Date → DateTime).

A Materialized View that will capture future inserts into tpch.lineitems (it joins to orders/customers/nations at insert time).

A read query that turns aggregate states into final numbers.

Optional chunked-backfill example if your source is large.

1) Create target aggregate table

```
CREATE TABLE IF NOT EXISTS tpch.hourly_sales_agg
(
  dt            DateTime,
  country_id    UInt32,
  product_id    UInt32,
  sum_price_state AggregateFunction(sum, Decimal64(2)),
  sum_qty_state   AggregateFunction(sum, Decimal64(2))
)
ENGINE = AggregatingMergeTree()
PARTITION BY toYYYYMM(dt)
ORDER BY (dt, country_id, product_id)
SETTINGS index_granularity = 4096;
```

2) Backfill existing historical data (one-shot)


```
INSERT INTO tpch.hourly_sales_agg
SELECT
  toStartOfHour(toDateTime(l_shipdate)) AS dt,
  n_nationkey                             AS country_id,
  l_partkey                               AS product_id,
  sumState(l_extendedprice)               AS sum_price_state,
  sumState(l_quantity)                    AS sum_qty_state
FROM tpch.lineitems AS l
JOIN tpch.orders    AS o ON l.l_orderkey = o.o_orderkey
JOIN tpch.customers AS c ON o.o_custkey = c.c_custkey
JOIN tpch.nations   AS n ON c.c_nationkey = n.n_nationkey
GROUP BY dt, country_id, product_id;
```

3) Create Materialized View to capture future inserts

```
CREATE MATERIALIZED VIEW IF NOT EXISTS tpch.hourly_sales_mv
TO tpch.hourly_sales_agg
AS
SELECT
  toStartOfHour(toDateTime(l_shipdate)) AS dt,
  n_nationkey                           AS country_id,
  l_partkey                             AS product_id,
  sumState(l_extendedprice)             AS sum_price_state,
  sumState(l_quantity)                  AS sum_qty_state
FROM tpch.lineitems AS l
JOIN tpch.orders    AS o ON l.l_orderkey = o.o_orderkey
JOIN tpch.customers AS c ON o.o_custkey = c.c_custkey
JOIN tpch.nations   AS n ON c.c_nationkey = n.n_nationkey
GROUP BY dt, country_id, product_id;

```


4) Read the aggregated final numbers

```
SELECT
  dt,
  country_id,
  product_id,
  sumMerge(sum_price_state) AS total_price,
  sumMerge(sum_qty_state)   AS total_qty
FROM tpch.hourly_sales_agg
GROUP BY dt, country_id, product_id
ORDER BY dt DESC, country_id, product_id
LIMIT 200;

```

5) Chunked backfill (if your lineitems is big or for batch)


-- example for one month

```
INSERT INTO tpch.hourly_sales_agg
SELECT
  toStartOfHour(toDateTime(l_shipdate)) AS dt,
  n_nationkey                           AS country_id,
  l_partkey                             AS product_id,
  sumState(l_extendedprice)             AS sum_price_state,
  sumState(l_quantity)                  AS sum_qty_state
FROM tpch.lineitems AS l
JOIN tpch.orders    AS o ON l.l_orderkey = o.o_orderkey
JOIN tpch.customers AS c ON o.o_custkey = c.c_custkey
JOIN tpch.nations   AS n ON c.c_nationkey = n.n_nationkey
WHERE l_shipdate BETWEEN '2024-01-01' AND '2024-01-31'
GROUP BY dt, country_id, product_id;
```


# EXAMPLES, DO NOT USE THESE COMMANDS



# Customers


```
SELECT * FROM file('tpch_csv/customers.csv','CSVWithNames') LIMIT 5;
```

-- optional server-side import

```
INSERT INTO tpch.customers
SELECT * FROM file('tpch_csv/customers.csv','CSVWithNames');
```


Streaming insert 


# parts

```
SELECT * FROM file('tpch_csv/parts.csv','CSVWithNames') LIMIT 5;
```

-- optional server-side import
```
INSERT INTO tpch.parts
SELECT * FROM file('tpch_csv/parts.csv','CSVWithNames');
```

# parts_suppliers

```
SELECT * FROM file('tpch_csv/parts_suppliers.csv','CSVWithNames') LIMIT 5;
```

-- optional server-side import
```
INSERT INTO tpch.parts_suppliers
SELECT * FROM file('tpch_csv/parts_suppliers.csv','CSVWithNames');
```



# orders


```
SELECT * FROM file('tpch_csv/orders.csv','CSVWithNames') LIMIT 5;
```
-- optional server-side import

```
INSERT INTO tpch.orders
SELECT * FROM file('tpch_csv/orders.csv','CSVWithNames');
```
 
# lineitems


```
SELECT * FROM file('tpch_csv/lineitems.csv','CSVWithNames') LIMIT 5;
```

-- optional server-side import

```
INSERT INTO tpch.lineitems
SELECT * FROM file('tpch_csv/lineitems.csv','CSVWithNames');
```

```
docker exec -it superset_clickhouse clickhouse-client --query "CREATE DATABASE mydb"


day2-clickhouse-1
docker logs day2-clickhouse-1 --tail 200



docker exec -it superset_app /bin/sh -c "curl -sS 'http://day2-clickhouse-1:8123/?query=SELECT%201+2' || true"

docker exec -it superset_app /bin/sh -c "curl --get --data-urlencode 'query=SELECT 1 + 2' 'http://day2-clickhouse-1:8123/'"
```
