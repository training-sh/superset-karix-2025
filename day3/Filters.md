fact_sales_lineitems



```
docker exec -it superset_mysql bash
```

 ```
mysql -uroot -pmysql_root_pass
```

```
use tpch;
```

we have too old data, try to offset 27 years to get data aligned to 2025, 2024..

```
UPDATE orders
SET o_orderdate = DATE_ADD(o_orderdate, INTERVAL 27 YEAR);
```


SELECT  o_orderdate, DATE_SUB(o_orderdate, INTERVAL 27 YEAR) from orders LIMIT 10;
SET o_orderdate = DATE_ADD(o_orderdate, INTERVAL 27 YEAR);


```
UPDATE lineitems
SET 
  l_shipdate    = DATE_ADD(l_shipdate, INTERVAL 27 YEAR),
  l_commitdate  = DATE_ADD(l_commitdate, INTERVAL 27 YEAR),
  l_receiptdate = DATE_ADD(l_receiptdate, INTERVAL 27 YEAR);
```

-- 1) CTAS - create the denormalized fact table

```
CREATE TABLE IF NOT EXISTS fact_sales_lineitems
ENGINE=InnoDB
AS
SELECT
  -- identity keys
  l.l_orderkey,
  l.l_linenumber,

  -- order-level fields
  o.o_orderdate,
  o.o_totalprice AS order_totalprice,
  o.o_orderpriority,
  o.o_clerk,
  o.o_shippriority,

  -- customer fields
  c.c_custkey,
  c.c_name AS cust_name,
  c.c_mktsegment AS cust_mktsegment,
  c.c_acctbal  AS cust_acctbal,

  -- customer geography (nation/region)
  cn.n_name     AS cust_nation,
  cr.r_name     AS cust_region,

  -- supplier fields
  s.s_suppkey,
  s.s_name      AS supp_name,
  s.s_acctbal   AS supp_acctbal,

  -- supplier geography (nation/region)
  sn.n_name     AS supp_nation,
  sr.r_name     AS supp_region,

  -- part fields
  p.p_partkey,
  p.p_name      AS part_name,
  p.p_mfgr      AS part_mfgr,
  p.p_brand     AS part_brand,
  p.p_type      AS part_type,
  p.p_size      AS part_size,
  p.p_retailprice,

  -- lineitem / shipment fields (time columns)
  l.l_shipdate,
  l.l_commitdate,
  l.l_receiptdate,
  l.l_shipmode,

  -- measures
  l.l_quantity,
  l.l_extendedprice,
  l.l_discount,
  l.l_tax,
  (l.l_extendedprice * (1 - l.l_discount)) AS net_sales,

  -- derived time metrics (example)
  DATEDIFF(l.l_shipdate, o.o_orderdate) AS ship_delay_days,
  DATEDIFF(l.l_receiptdate, l.l_commitdate) AS commit_to_receipt_days,

  -- small helpful flags / categories
  CASE WHEN l.l_returnflag = 'R' THEN 1 ELSE 0 END AS is_returned,
  CASE WHEN l.l_linestatus = 'F' THEN 1 ELSE 0 END AS is_fulfilled

FROM lineitems l
JOIN orders    o ON o.o_orderkey = l.l_orderkey
JOIN customers c ON c.c_custkey  = o.o_custkey
LEFT JOIN nations cn ON cn.n_nationkey = c.c_nationkey
LEFT JOIN regions cr  ON cr.r_regionkey = cn.n_regionkey
JOIN suppliers s ON s.s_suppkey = l.l_suppkey
LEFT JOIN nations sn ON sn.n_nationkey = s.s_nationkey
LEFT JOIN regions sr  ON sr.r_regionkey = sn.n_regionkey
LEFT JOIN parts p ON p.p_partkey = l.l_partkey
;
```

```
SELECT count(*) from fact_sales_lineitems;
```

-- 2) add a composite primary key (orderkey + linenumber)
ALTER TABLE fact_sales_lineitems
  ADD PRIMARY KEY (l_orderkey, l_linenumber);

-- 3) helpful indexes for Superset filtering & grouping

CREATE INDEX idx_fact_orderdate     ON fact_sales_lineitems (o_orderdate);
CREATE INDEX idx_fact_shipdate      ON fact_sales_lineitems (l_shipdate);
CREATE INDEX idx_fact_receiptdate   ON fact_sales_lineitems (l_receiptdate);
CREATE INDEX idx_fact_commitdate    ON fact_sales_lineitems (l_commitdate);

CREATE INDEX idx_fact_cust_region   ON fact_sales_lineitems (cust_region);
CREATE INDEX idx_fact_supp_region   ON fact_sales_lineitems (supp_region);
CREATE INDEX idx_fact_cust_segment  ON fact_sales_lineitems (cust_mktsegment);
CREATE INDEX idx_fact_shipmode      ON fact_sales_lineitems (l_shipmode);



-- 4) Optional: analyze / optimize table statistics (run after large load)
ANALYZE TABLE fact_sales_lineitems;


Notes

```
Time Range - we cannot select columns 

Time Grain - we cannot select columns
  range or unit 

  seconds
  minutes
  hours
  days
  weeks
  month
  year


Original data
order_date
2025-09-01 12:00 PM ...   10
2025-09-01 13:00 PM ...   20
2025-09-02 ...            25
2025-09-03 ...            25 

days, aggregate data based on days
Time grain 

2025-09-01   30   (10 + 20)
2025-09-02  25
2025-09-03  25


weeks, aggregate data based on weeks
Time grain 

2025-09-01-2025-09-07    80



months, aggregate data based on months
Time grain 

2025-09-01-2025-09-30    80

--
Filter Time Column

pick the first column
point a column as temporal - dataset

when we have more than 1 date, which date column, the superset must pick?

Time Column
   order_date
   commit_date
   shipment_date
   ..
```
