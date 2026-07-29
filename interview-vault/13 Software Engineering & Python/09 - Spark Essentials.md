# Spark Essentials (PySpark)

**Prev:** [[08 - SQL Cheatsheet]] · **Next:** [[10 - Python Interview Traps]]

---

## In plain English

**Spark** processes **big data** in parallel across a cluster. You write transformations (lazy); Spark executes an optimized plan. PySpark = pandas-like API at scale.

---

## When to use Spark

| Use Spark | Skip Spark |
|-----------|------------|
| Data doesn't fit in RAM on one machine | Fits comfortably in pandas |
| TB-scale logs, ETL pipelines | Quick notebook EDA on 100MB CSV |
| Need distributed joins / groupby | sklearn training on single node |

---

## Core concepts

| Concept | Meaning |
|---------|---------|
| **RDD** | Low-level distributed collection (legacy) |
| **DataFrame** | Structured API (like SQL table) — **prefer this** |
| **Partition** | Chunk of data on one executor |
| **Lazy eval** | `filter`, `select` build plan; `count`, `write` trigger execution |
| **Shuffle** | Redistributing data across nodes — **expensive** |

---

## PySpark examples

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("demo").getOrCreate()
df = spark.read.parquet("s3://bucket/events/")

# Transformations (lazy)
clean = (
    df.filter(F.col("date") >= "2024-01-01")
      .select("user_id", "event", "value")
      .groupBy("user_id")
      .agg(F.sum("value").alias("total"))
)

clean.show()           # action → runs job
clean.write.mode("overwrite").parquet("out/")
```

---

## Spark SQL

```python
df.createOrReplaceTempView("events")
spark.sql("""
    SELECT user_id, COUNT(*) AS n
    FROM events
    GROUP BY user_id
    HAVING n > 10
""").show()
```

---

## Performance tips (interview)

1. **Avoid wide shuffles** — filter early, reduce keys before join.
2. **Partition wisely** — too few = no parallelism; too many = overhead.
3. **Cache** (`df.cache()`) only if reused multiple times.
4. **Broadcast** small tables in joins: `F.broadcast(small_df)`.
5. Prefer **Parquet** over CSV (columnar, compressed).

---

## Spark vs pandas

| | pandas | Spark |
|---|--------|-------|
| Execution | Single machine | Distributed |
| API | Eager | Lazy |
| Data size | RAM limit | Cluster disk/RAM |

---

## Common traps

| Trap | Correct |
|------|---------|
| Calling `.collect()` on huge DF | OOM driver — `show()`, write to storage, or aggregate first |
| Too many small files | Coalesce/repartition before write |
| UDF for everything | Built-in `F.*` is optimized; UDFs are slow (Python) |
| Ignoring skew | Salting keys or adaptive execution for hot keys |
| `groupBy` after huge join | Filter **before** join when possible |

---

## Interview coding drills (4 classics)

Assume `events(user_id, event, value, date)` and `users(user_id, country)` Parquet on S3/HDFS.

### 1. Word count (map → reduceByKey style)

```python
from pyspark.sql import functions as F

lines = spark.read.text("logs/*.txt")
counts = (
    lines.select(F.explode(F.split(F.col("value"), " ")).alias("word"))
         .filter(F.col("word") != "")
         .groupBy("word")
         .count()
         .orderBy(F.desc("count"))
)
counts.show(20, truncate=False)
```

**Trap:** `collect()` on full counts — use `show()` or write to storage.

---

### 2. Filter early → join → aggregate

**Prompt:** Total `value` per `country` for events in 2024.

```python
from pyspark.sql import functions as F

events = spark.read.parquet("events/")
users = spark.read.parquet("users/")

result = (
    events.filter(F.col("date") >= "2024-01-01")
          .join(users, on="user_id", how="inner")
          .groupBy("country")
          .agg(F.sum("value").alias("total_value"))
)
```

**Trap:** Join before filter → larger shuffle. Broadcast **small** `users` if it fits: `F.broadcast(users)`.

---

### 3. Window: rank events per user by value

```python
from pyspark.sql.window import Window

w = Window.partitionBy("user_id").orderBy(F.desc("value"))
top_per_user = (
    events.withColumn("rn", F.row_number().over(w))
          .filter(F.col("rn") == 1)
          .select("user_id", "event", "value")
)
```

**Trap:** `rank()` vs `row_number()` — ties handled differently.

---

### 4. Write partitioned Parquet (production pattern)

```python
(
    result.repartition("country")          # or partitionBy when writing
            .write
            .mode("overwrite")
            .partitionBy("country")
            .parquet("s3://bucket/gold/country_totals/")
)
```

**Check job:** `result.explain()` — look for **Exchange** (shuffle) and reduce before write.

**Trap:** Thousands of tiny files → `coalesce(n)` or `repartition(n)` before write; avoid `collect()` on `result`.

---

## Interview one-liner

> "Spark is for distributed ETL and feature pipelines at scale. I minimize shuffles, filter early, use DataFrame API and Spark SQL, and only collect small results to the driver."

---

**Next:** [[11 - PyTorch Essentials]]
