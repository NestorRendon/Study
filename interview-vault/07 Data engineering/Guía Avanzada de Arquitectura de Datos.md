
## Database vs Data Warehouse vs Data Lake vs Data Lakehouse

> [!abstract] Resumen
> Las cuatro arquitecturas resuelven problemas diferentes. Una **Database OLTP** está optimizada para operar una aplicación; un **Data Warehouse** para análisis estructurado y BI; un **Data Lake** para almacenar grandes volúmenes de datos en diferentes formatos; y un **Data Lakehouse** añade una capa transaccional, de metadatos y gobierno sobre almacenamiento tipo lake para permitir analytics, BI y Machine Learning.

---

## 1. La idea fundamental

| Tecnología                | Pregunta principal                                                                |
| ------------------------- | --------------------------------------------------------------------------------- |
| **Database / OLTP**       | ¿Cómo guardo y modifico el estado actual de mi aplicación?                        |
| **Data Warehouse / OLAP** | ¿Cómo analizo el negocio y obtengo métricas?                                      |
| **Data Lake**             | ¿Cómo almaceno grandes cantidades de datos de cualquier tipo de forma económica?  |
| **Data Lakehouse**        | ¿Cómo tengo almacenamiento tipo Data Lake con tablas, ACID, gobierno y analytics? |
**OLTP** (Online Transaction Processing) manages real-time day-to-day operations like user checkouts and bank transfers. **OLAP** (Online Analytical Processing) analyzes large historical datasets to spot trends and build reports. ==OLTP runs fast single-row writes, while OLAP runs massive multi-row aggregations==


data warehouse is ==a central storage system that collects, cleans, and organizes current and historical data from different company sources==. It is optimized for fast queries, business reporting, and data analysis rather than everyday business operations
### Regla mental

```text
                         ¿Qué necesito?

                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
        OPERACIONES        ANALÍTICA       DATOS RAW /
          DIARIAS          EMPRESARIAL      ML / DATA SCIENCE
              │               │                │
              ▼               ▼                ▼
            OLTP          WAREHOUSE         DATA LAKE
                                               │
                                               ▼
                                      ¿Necesito SQL +
                                      ACID + gobierno +
                                      BI + ML?
                                               │
                                               ▼
                                          LAKEHOUSE
```

---

# 2. Base de Datos Tradicional — OLTP

## ¿Qué es?

Una **OLTP (Online Transaction Processing)** database mantiene el estado operacional de una aplicación.

Ejemplos:

- usuarios
- pedidos
- pagos
- inventario
- cuentas
- reservas
- productos

Tecnologías habituales:

- PostgreSQL
- MySQL
- Oracle Database
- Microsoft SQL Server

## Características

| Característica | OLTP |
| --- | --- |
| Objetivo | Operaciones de la aplicación |
| Consultas | Pequeñas y frecuentes |
| Latencia | Milisegundos |
| Datos | Principalmente estructurados |
| Diseño | Normalizado |
| Escrituras | Muchas escrituras pequeñas |
| Transacciones | ACID |
| Consumidores | Aplicaciones y APIs |
| Ejemplo | Crear un pedido |

### Ejemplo

```sql
INSERT INTO orders (
    user_id,
    product_id,
    quantity,
    created_at
)
VALUES (
    123,
    456,
    2,
    NOW()
);
```

### Consulta típica

```sql
SELECT
    id,
    name,
    email
FROM users
WHERE email = 'user@example.com'
LIMIT 1;
```

### Arquitectura

```text
                    APPLICATION
                         │
                         ▼
                    REST / API
                         │
                         ▼
                    PostgreSQL
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
          INSERT                  SELECT
          UPDATE                  DELETE
```

> [!tip] Cuándo usar OLTP
> Usa una base de datos OLTP cuando necesitas mantener el **estado operacional actual** de una aplicación y ejecutar muchas transacciones pequeñas y consistentes.

---

# 3. Data Warehouse — OLAP

## ¿Qué es?

Un **Data Warehouse** es un sistema optimizado para analizar grandes cantidades de datos estructurados.

**OLAP = Online Analytical Processing**

Mientras OLTP responde:

> "¿Cuál es el pedido de este usuario?"

OLAP responde:

> "¿Cuáles fueron nuestros ingresos por país y producto durante los últimos 24 meses?"

Tecnologías habituales:

- Snowflake
- Google BigQuery
- Amazon Redshift
- Azure Synapse
- ClickHouse

## Características

| Característica | Data Warehouse |
| --- | --- |
| Objetivo | Analytics y BI |
| Consultas | Complejas y agregaciones |
| Latencia | Segundos a minutos |
| Datos | Estructurados / semi-estructurados |
| Diseño | Dimensional / desnormalizado |
| Lecturas | Grandes volúmenes |
| Escrituras | Batch, ELT o streaming |
| Transacciones | Generalmente soportadas |
| Usuarios | Data Analysts, BI, Data Scientists |
| Ejemplo | Revenue mensual |

## Modelo estrella

Un patrón muy común es el **Star Schema**.

```text
                    dim_customer
                         │
                         │
                         ▼
dim_product ─────► fact_sales ◄───── dim_date
                         │
                         │
                         ▼
                    dim_store
```

### Fact Table

Contiene eventos o métricas:

```text
fact_sales

sale_id
customer_id
product_id
date_id
store_id
quantity
revenue
discount
```

### Dimension Tables

Contienen información descriptiva:

```text
dim_customer
----------------
customer_id
name
country
segment
```

```text
dim_product
----------------
product_id
name
category
brand
```

## Consulta analítica

```sql
SELECT
    DATE_TRUNC('month', sale_date) AS month,
    SUM(net_amount) AS revenue
FROM sales
WHERE category = 'Electronics'
GROUP BY 1
ORDER BY 1;
```

---

# 4. Data Lake

## ¿Qué es?

Un **Data Lake** es un repositorio de almacenamiento de bajo costo capaz de conservar datos en diferentes formatos y niveles de procesamiento.

Puede almacenar:

- CSV
- JSON
- Parquet
- imágenes
- audio
- video
- PDFs
- logs
- eventos
- datos de IoT
- datasets de Machine Learning

Tecnologías de almacenamiento:

- Amazon S3
- Google Cloud Storage
- Azure Blob Storage
- MinIO

## Característica principal

Tradicionalmente se asocia con:

**Schema-on-Read**

```text
                    DATA LAKE

    CSV       JSON       Parquet      Images
     │          │           │            │
     └──────────┴───────────┴────────────┘
                       │
                       ▼
                 Object Storage
                       │
                       ▼
                Analytics / ML
```

Los datos pueden almacenarse primero y estructurarse posteriormente según la necesidad.

## Ejemplo de estructura

```text
s3://company-data/

├── raw/
│   ├── sales/
│   ├── customers/
│   ├── logs/
│   └── sensors/
│
├── processed/
│   ├── sales/
│   └── customers/
│
└── ml/
    ├── features/
    └── training/
```

> [!warning] Importante
> Un Data Lake no debería entenderse simplemente como "una carpeta gigante con archivos". Un lake empresarial necesita catálogo, gobierno, seguridad, particionamiento, formatos adecuados y procesos de calidad.

---

# 5. Data Lakehouse

## ¿Qué es?

Un **Data Lakehouse** combina características de un Data Lake y un Data Warehouse.

La idea central es:

```text
        Data Lake
    barato + flexible
             +
     Table Format
  ACID + metadata + schema
             +
       Query Engines
      SQL + Spark + ML
             =
        Data Lakehouse
```

## Tecnologías importantes

### Table Formats

- Apache Iceberg
- Delta Lake
- Apache Hudi

### Plataformas

- Databricks
- Snowflake
- AWS
- Google Cloud
- Microsoft Azure

> [!important] Concepto clave
> **S3, GCS o Azure Blob no son por sí solos un Lakehouse.**
>
> El Lakehouse aparece cuando el almacenamiento de objetos se combina con formatos de tabla, metadatos, transacciones, catálogo, gobierno y motores de consulta.

## ¿Qué aporta un Table Format?

Apache Iceberg y Delta Lake permiten trabajar con archivos como Parquet pero añadiendo capacidades como:

- schema evolution
- ACID transactions
- time travel
- snapshots
- partition evolution
- metadata management
- concurrent reads/writes

---

# 6. Arquitectura Lakehouse Moderna

```text
                           DATA SOURCES
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
     PostgreSQL              APIs / SaaS           IoT / Logs
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                                ▼
                         INGESTION LAYER
                    Kafka / Pub/Sub / Kinesis
                                │
                                ▼
                       OBJECT STORAGE / LAKE
                         S3 / GCS / ADLS
                                │
                     ┌──────────┴──────────┐
                     │                     │
                     ▼                     ▼
                  RAW DATA             TABLE FORMAT
                                      Iceberg / Delta
                                           │
                                           ▼
                                  CATALOG + GOVERNANCE
                                           │
                         ┌─────────────────┼─────────────────┐
                         │                 │                 │
                         ▼                 ▼                 ▼
                       SQL             Spark / ML          BI
                    Trino/Athena       Databricks       Power BI
                    BigQuery/etc.                         Looker
```

---

# 7. Comparación Completa

| Característica | OLTP Database | Data Warehouse | Data Lake | Data Lakehouse |
| --- | --- | --- | --- | --- |
| Objetivo | Operaciones | Analytics / BI | Almacenamiento masivo | Analytics + ML + BI |
| Datos | Estructurados | Estructurados / semi-estructurados | Cualquier formato | Estructurados / semi-estructurados + archivos |
| Volumen | GB–TB | TB–PB | PB–EB | PB–EB |
| Latencia | ms | s–min | Variable | s–min |
| Schema | Schema-on-Write | Schema-on-Write | Schema-on-Read | Schema + evolución |
| ACID | Sí | Sí | No necesariamente | Sí, mediante table format |
| Storage | Database storage | Managed storage | Object storage | Object storage |
| Coste de storage | Medio | Medio–alto | Bajo | Bajo |
| SQL | Excelente | Excelente | Mediante query engine | Excelente |
| BI | Limitado | Excelente | Posible | Excelente |
| Machine Learning | Posible | Posible | Excelente | Excelente |
| Datos no estructurados | Limitado | Limitado | Excelente | Excelente como almacenamiento |
| Gobierno | Alto | Alto | Requiere herramientas | Alto |
| Time Travel | Depende de DB | Depende | No estándar | Sí |
| Schema Evolution | Depende | Sí | Manual | Sí |
| Ejemplos | PostgreSQL, MySQL | BigQuery, Snowflake, Redshift | S3, GCS, ADLS | Databricks + Delta/Iceberg |

---

# 8. ETL vs ELT

## ETL

**Extract → Transform → Load**

```text
SOURCE
  │
  ▼
EXTRACT
  │
  ▼
TRANSFORM
  │
  ▼
LOAD
  │
  ▼
WAREHOUSE
```

Los datos se transforman **antes** de entrar al sistema destino.

## ELT

**Extract → Load → Transform**

```text
SOURCE
  │
  ▼
EXTRACT
  │
  ▼
LOAD
  │
  ▼
DATA LAKE / WAREHOUSE
  │
  ▼
TRANSFORM
  │
  ▼
ANALYTICS
```

En arquitecturas cloud modernas, **ELT es muy común**, especialmente con:

- BigQuery
- Snowflake
- Redshift
- Databricks
- Lakehouses

Esto no significa que ETL haya desaparecido. ETL sigue siendo útil cuando necesitas transformar, validar o anonimizar datos antes de almacenarlos.

---

# 9. Medallion Architecture

Una arquitectura Lakehouse muy común utiliza tres niveles:

```text
                  DATA SOURCES
                       │
                       ▼
                  ┌─────────┐
                  │ BRONZE  │
                  │  RAW    │
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │ SILVER  │
                  │ CLEANED │
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │  GOLD   │
                  │ BUSINESS│
                  └────┬────┘
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
            BI         ML       APIs
```

## Bronze

Datos prácticamente en estado original.

```text
Bronze
- raw events
- raw JSON
- raw CDC
- raw logs
```

## Silver

Datos limpios y normalizados.

```text
Silver
- validated records
- deduplicated data
- standardized schemas
- enriched data
```

## Gold

Datos preparados para consumidores.

```text
Gold
- business metrics
- aggregates
- customer 360
- ML features
- BI datasets
```

---

# 10. Ejemplo de Arquitectura Empresarial

Imaginemos un e-commerce:

```text
                         USERS
                           │
                           ▼
                     E-COMMERCE APP
                           │
                           ▼
                       FASTAPI
                           │
                           ▼
                     PostgreSQL
                       (OLTP)
                           │
                  CDC / Batch / Events
                           │
                           ▼
                    Kafka / Kinesis
                           │
                           ▼
                     S3 DATA LAKE
                           │
                           ▼
                     BRONZE LAYER
                           │
                           ▼
                   Spark / Databricks
                           │
                           ▼
                     SILVER LAYER
                           │
                           ▼
                      GOLD LAYER
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           BI / SQL        ML       Analytics
              │            │            │
           Power BI     Training     Python
```

---

# 11. Ejemplo: PostgreSQL → Data Lake → Warehouse

Una arquitectura empresarial puede utilizar diferentes sistemas simultáneamente.

```text
                    APPLICATION
                         │
                         ▼
                    PostgreSQL
                      OLTP DB
                         │
                  CDC / ETL / ELT
                         │
                         ▼
                    Object Storage
                         │
                  ┌──────┴──────┐
                  ▼             ▼
               Parquet       Raw JSON
                  │
                  ▼
              Lakehouse
                  │
          ┌───────┼────────┐
          ▼       ▼        ▼
         SQL      BI       ML
```

No es necesario elegir **una sola** tecnología.

Una empresa puede tener:

```text
PostgreSQL + S3 + Iceberg + BigQuery + Redis
```

porque cada componente resuelve un problema diferente.

---

# 12. Ejemplos Prácticos de Consulta

## 12.1 OLTP — PostgreSQL

```sql
SELECT
    id,
    name,
    email,
    created_at
FROM users
WHERE email = 'user@example.com'
LIMIT 1;
```

Busca pocos registros, normalmente utilizando índices.

---

## 12.2 Data Warehouse — BigQuery / Snowflake

```sql
SELECT
    DATE_TRUNC(sale_date, MONTH) AS month,
    category,
    SUM(net_amount) AS revenue,
    COUNT(*) AS transactions
FROM sales
WHERE sale_date >= '2026-01-01'
GROUP BY
    month,
    category
ORDER BY
    month;
```

Esta consulta está diseñada para analizar grandes cantidades de datos.

---

## 12.3 Data Lake — Athena

Supongamos que tenemos JSON almacenado en:

```text
s3://company-data/raw/iot/
```

Podemos consultar los datos mediante Amazon Athena:

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS sensor_readings (
    sensor_id STRING,
    temperature DOUBLE,
    timestamp TIMESTAMP
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://company-data/raw/iot/';
```

Después:

```sql
SELECT
    sensor_id,
    AVG(temperature) AS avg_temperature
FROM sensor_readings
GROUP BY sensor_id;
```

Aquí:

```text
S3      → storage
Athena  → query engine
```

---

# 13. Lakehouse — Apache Iceberg

Con Iceberg, una tabla puede almacenarse sobre object storage.

Conceptualmente:

```text
S3
│
├── data/
│   ├── part-0001.parquet
│   ├── part-0002.parquet
│   └── part-0003.parquet
│
└── metadata/
    ├── snapshots
    ├── manifests
    └── metadata files
```

El motor puede consultar la tabla como una tabla SQL:

```sql
SELECT
    category,
    SUM(net_amount) AS revenue
FROM sales
WHERE sale_date >= DATE '2026-01-01'
GROUP BY category;
```

La diferencia es que el usuario trabaja con una **tabla gestionada**, aunque los datos físicamente estén en object storage.

---

# 14. Lakehouse — PySpark / Delta Lake

```python
from pyspark.sql import functions as F

df = spark.read.table(
    "sales_lakehouse.fact_transactions"
)

result = (
    df
    .filter(F.col("category") == "Electronics")
    .groupBy("month")
    .agg(
        F.sum("net_amount").alias("revenue")
    )
)

result.show()
```

---

# 15. ¿Dónde entra Machine Learning?

El Data Lake y el Lakehouse son especialmente importantes para ML porque permiten almacenar diferentes tipos de datos.

```text
                    DATA LAKEHOUSE
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   Tabular Data        Images            Text/PDF
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                     Data Preparation
                          │
                          ▼
                       Training
                          │
                          ▼
                        Model
                          │
                          ▼
                      Inference
```

---

# 16. Data Architecture + AI

Para sistemas modernos de AI:

```text
                         DATA SOURCES
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
     PostgreSQL             APIs                 Files
         │                    │                    │
         └────────────────────┼────────────────────┘
                              ▼
                        INGESTION
                    Kafka / Kinesis / Pub/Sub
                              │
                              ▼
                       DATA LAKEHOUSE
                   S3 + Iceberg / Delta
                              │
               ┌──────────────┼──────────────┐
               │              │              │
               ▼              ▼              ▼
             SQL            BI / ML        RAG
               │              │              │
               │              │              ▼
               │              │        Chunking + Embeddings
               │              │              │
               │              │              ▼
               │              │         Vector DB
               │              │              │
               └──────────────┼──────────────┘
                              ▼
                         AI APPLICATION
                              │
                              ▼
                           LLM / Agent
```

---

# 17. ¿Cuándo usar cada arquitectura?

## Usa PostgreSQL / OLTP cuando:

- tienes una aplicación transaccional
- necesitas consistencia inmediata
- haces muchas operaciones pequeñas
- necesitas relaciones y constraints
- el usuario interactúa directamente con los datos

Ejemplos:

```text
E-commerce
Banking
CRM
Booking system
ERP
```

---

## Usa un Data Warehouse cuando:

- necesitas BI
- tienes dashboards
- haces agregaciones
- necesitas SQL analítico
- los datos están relativamente estructurados
- quieres una plataforma gestionada

Ejemplos:

```text
Sales analytics
Financial reporting
Marketing analytics
Business intelligence
```

---

## Usa un Data Lake cuando:

- tienes grandes cantidades de datos
- tienes múltiples formatos
- necesitas almacenamiento barato
- necesitas guardar datos raw
- haces Data Science o ML
- todavía no sabes exactamente cómo utilizarás todos los datos

Ejemplos:

```text
IoT
Images
Videos
Logs
ML datasets
Raw events
```

---

## Usa un Lakehouse cuando:

- quieres combinar BI + SQL + ML
- necesitas ACID sobre object storage
- necesitas schema evolution
- necesitas time travel
- necesitas gobernanza
- quieres reducir duplicación entre Lake y Warehouse
- tienes grandes volúmenes de datos

---

# 18. Decision Matrix

| Necesidad | Mejor opción |
| --- | --- |
| Aplicación transaccional | PostgreSQL / MySQL |
| CRUD | OLTP Database |
| Dashboard empresarial | Data Warehouse |
| BI | Data Warehouse |
| Raw data | Data Lake |
| Imágenes / audio / video | Data Lake |
| Machine Learning datasets | Data Lake / Lakehouse |
| SQL + ML sobre los mismos datos | Lakehouse |
| ACID sobre object storage | Lakehouse |
| Petabytes de datos | Lake / Lakehouse |
| Data Science | Lake / Lakehouse |
| Enterprise analytics | Warehouse / Lakehouse |

---

# 19. Arquitectura Híbrida Moderna

En la práctica, muchas organizaciones utilizan varias arquitecturas simultáneamente.

```text
                         APPLICATIONS
                              │
                              ▼
                         PostgreSQL
                           OLTP
                              │
                         CDC / Events
                              │
                              ▼
                    ┌──────────────────┐
                    │   DATA PLATFORM  │
                    │                  │
                    │ S3 / GCS / ADLS  │
                    │ + Iceberg/Delta  │
                    └────────┬─────────┘
                             │
                 ┌───────────┼───────────┐
                 │           │           │
                 ▼           ▼           ▼
               BI/SQL       ML          RAG
                 │           │           │
                 ▼           ▼           ▼
            Warehouse     Models     Vector DB
                 │           │           │
                 └───────────┼───────────┘
                             ▼
                        AI APPLICATION
```

La arquitectura correcta no consiste en reemplazar PostgreSQL por un Lakehouse.

Cada componente tiene una función diferente.

---

# 20. Conceptos que debes conocer

| Concepto | Definición |
| --- | --- |
| **OLTP** | Online Transaction Processing; sistemas para operaciones transaccionales. |
| **OLAP** | Online Analytical Processing; sistemas para análisis y agregaciones. |
| **ETL** | Extract, Transform, Load. Transformación antes de cargar. |
| **ELT** | Extract, Load, Transform. Carga primero y transforma después. |
| **Data Lake** | Almacenamiento económico de datos en múltiples formatos. |
| **Data Warehouse** | Plataforma optimizada para análisis estructurado. |
| **Lakehouse** | Arquitectura que combina Data Lake con capacidades de tablas, ACID, gobierno y analytics. |
| **Object Storage** | Almacenamiento de objetos como S3, GCS o Azure Blob. |
| **Schema-on-Write** | El esquema se valida antes o durante la escritura. |
| **Schema-on-Read** | El esquema se interpreta al leer los datos. |
| **ACID** | Atomicity, Consistency, Isolation, Durability. |
| **CDC** | Change Data Capture; captura cambios de una base de datos. |
| **Data Catalog** | Inventario de datasets, tablas, columnas, propietarios y metadatos. |
| **Data Governance** | Políticas y controles para seguridad, calidad, acceso y cumplimiento. |
| **Data Lineage** | Seguimiento del origen y transformación de los datos. |
| **Partitioning** | División lógica de datos para reducir lecturas y mejorar performance. |
| **Columnar Storage** | Almacenamiento por columnas, eficiente para analytics. |
| **Parquet** | Formato columnar abierto muy utilizado en Data Lakes y Lakehouses. |
| **Iceberg** | Formato de tabla abierto para Data Lakes/Lakehouses. |
| **Delta Lake** | Formato/capa de tablas que añade transacciones y gestión de metadatos sobre Data Lakes. |
| **Hudi** | Formato de tabla orientado a ingestión y actualización incremental. |
| **Star Schema** | Modelo dimensional con fact tables y dimension tables. |
| **Fact Table** | Tabla que contiene eventos y métricas. |
| **Dimension Table** | Tabla descriptiva utilizada para analizar hechos. |
| **Query Engine** | Motor que ejecuta consultas sobre datos, como Athena o Trino. |
| **Medallion Architecture** | Organización Bronze → Silver → Gold. |
| **Data Quality** | Medición y control de exactitud, completitud, consistencia y validez. |
| **Data Mesh** | Enfoque donde dominios poseen y publican productos de datos. |
| **Data Fabric** | Arquitectura que integra datos mediante metadatos, automatización y gobierno. |

---

# 21. Resumen Mental

```text
                         DATA ARCHITECTURE

                              DATA
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
           OPERATE          ANALYZE          STORE RAW
              │                │                │
              ▼                ▼                ▼
            OLTP           WAREHOUSE        DATA LAKE
                                               │
                                               │
                                               ▼
                                         + ACID / TABLES
                                         + GOVERNANCE
                                         + SQL
                                         + TIME TRAVEL
                                               │
                                               ▼
                                          LAKEHOUSE
```

### La regla más importante

> **OLTP = ejecutar el negocio.**

> **Warehouse = analizar el negocio.**

> **Lake = almacenar los datos.**

> **Lakehouse = almacenar + gestionar + analizar + preparar datos para ML sobre una plataforma tipo lake.**

---

# 22. Ejemplo Final: Arquitectura AI Empresarial

Una arquitectura completa para una empresa moderna podría ser:

```text
                         ┌──────────────┐
                         │  Customers   │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │ Application  │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │  PostgreSQL  │
                         │    OLTP      │
                         └──────┬───────┘
                                │
                           CDC / Events
                                │
                                ▼
                    ┌──────────────────────┐
                    │   Data Lakehouse     │
                    │                      │
                    │ S3 + Iceberg/Delta   │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
          Analytics            ML              RAG
             │                 │                 │
             ▼                 ▼                 ▼
        Data Warehouse      Training         Embeddings
             │                 │                 │
             ▼                 ▼                 ▼
            BI              Models          Vector DB
                                                 │
                                                 ▼
                                          AI Application
                                                 │
                                                 ▼
                                             LLM / Agent
```

### Arquitectura por responsabilidades

```text
PostgreSQL       → operaciones
Lakehouse        → plataforma de datos
Warehouse        → analytics / BI
Object Storage   → datos masivos
Vector DB        → búsqueda semántica
ML Platform      → entrenamiento
LLM / Agents     → inteligencia
```

---

# 23. Checklist de Arquitectura

Antes de diseñar una plataforma de datos, pregunta:

- [ ] ¿Los datos son transaccionales o analíticos?
- [ ] ¿Necesito baja latencia?
- [ ] ¿Cuánto volumen de datos tengo?
- [ ] ¿Qué tipos de datos tengo?
- [ ] ¿Necesito almacenar datos raw?
- [ ] ¿Necesito SQL?
- [ ] ¿Necesito BI?
- [ ] ¿Necesito Machine Learning?
- [ ] ¿Necesito RAG?
- [ ] ¿Necesito ACID?
- [ ] ¿Necesito schema evolution?
- [ ] ¿Necesito time travel?
- [ ] ¿Necesito CDC?
- [ ] ¿Cómo voy a hacer data governance?
- [ ] ¿Cómo voy a controlar data quality?
- [ ] ¿Cómo voy a gestionar data lineage?
- [ ] ¿Quién consumirá los datos?
- [ ] ¿Cuánto costará storage?
- [ ] ¿Cuánto costará compute?
- [ ] ¿Qué parte debe ser managed service?

---

# 24. Regla de Diseño

La pregunta correcta no es:

> **"¿Data Warehouse o Data Lake?"**

La pregunta correcta es:

> **"¿Qué workloads tengo y qué sistema está optimizado para cada uno?"**

Una arquitectura empresarial madura normalmente separa:

```text
Operational Workloads
        │
        ▼
      OLTP
        │
        ▼
   Data Platform
        │
        ▼
 ┌──────┼────────┐
 ▼      ▼        ▼
 BI     ML       AI
```

Por eso es completamente normal tener:

```text
PostgreSQL
    +
S3 / GCS
    +
Iceberg / Delta
    +
BigQuery / Snowflake
    +
Redis
    +
Vector Database
    +
ML Platform
    +
LLM / Agents
```

La arquitectura no se trata de encontrar **una única tecnología que haga todo**, sino de asignar cada workload al componente que mejor lo resuelve.


| Función / Capa             | Qué hace                                    | Snowflake                           | Databricks                   | Apache Iceberg             | AWS                     | Google Cloud              | Open Source / Otros       |
| -------------------------- | ------------------------------------------- | ----------------------------------- | ---------------------------- | -------------------------- | ----------------------- | ------------------------- | ------------------------- |
| **OLTP Database**          | Transacciones de aplicaciones               | Snowflake no es la opción principal | No                           | No                         | RDS / Aurora            | Cloud SQL / AlloyDB       | PostgreSQL, MySQL         |
| **Object Storage**         | Almacenar archivos/data lake                | Internal/External stages            | S3/ADLS/GCS                  | Usa object storage         | **S3**                  | **GCS**                   | MinIO                     |
| **Data Lake**              | Almacenar raw/structured/unstructured data  | External tables / stages            | Lakehouse storage            | **Iceberg tables**         | **S3 + Glue**           | **GCS + BigLake**         | MinIO                     |
| **Table Format**           | ACID, metadata, schema evolution, snapshots | Snowflake Tables                    | **Delta Lake**               | **Iceberg**                | Iceberg / Delta         | Iceberg / BigLake         | Hudi, Delta               |
| **Data Warehouse**         | Analytics SQL                               | **Snowflake**                       | Databricks SQL               | No                         | **Redshift**            | **BigQuery**              | ClickHouse                |
| **Query Engine**           | Ejecutar SQL sobre datos                    | Snowflake Engine                    | Databricks SQL / Photon      | No                         | Athena / Redshift       | BigQuery                  | Trino, Presto, Spark      |
| **Distributed Processing** | Procesar grandes datasets                   | Snowpark                            | **Apache Spark / Photon**    | No                         | EMR / Glue              | Dataproc / Dataflow       | Spark                     |
| **ETL / ELT**              | Transformar datos                           | SQL / Snowpark / dbt                | Workflows / Spark / DLT      | No                         | Glue / EMR / dbt        | Dataflow / Dataproc / dbt | dbt, Airflow              |
| **Streaming**              | Procesamiento de eventos en tiempo real     | Snowpipe Streaming                  | Structured Streaming         | Puede ser destino          | **Kinesis / MSK**       | **Pub/Sub / Dataflow**    | Kafka / Flink             |
| **Batch Processing**       | Procesamiento periódico                     | Tasks / SQL                         | Spark / Workflows            | No                         | Glue / EMR              | Dataproc                  | Spark                     |
| **CDC**                    | Capturar cambios de DB                      | Streams / connectors                | DLT / connectors             | No directamente            | DMS / Debezium          | Datastream                | Debezium                  |
| **Orchestration**          | Coordinar pipelines                         | Tasks / Workflows                   | **Workflows**                | No                         | MWAA / Step Functions   | Composer                  | Airflow, Dagster, Prefect |
| **Data Transformation**    | Transformar datasets                        | SQL / Snowpark                      | Spark / SQL / dbt            | No                         | Glue / dbt              | Dataform / dbt            | dbt                       |
| **Data Quality**           | Validar calidad                             | Data Quality / expectations         | Lakeflow / expectations      | No                         | Glue Data Quality       | Dataplex                  | Great Expectations        |
| **Data Catalog**           | Descubrir y documentar datasets             | Horizon Catalog                     | **Unity Catalog**            | No                         | Glue Catalog            | Dataplex / Data Catalog   | OpenMetadata              |
| **Data Governance**        | Seguridad, políticas, ownership             | Horizon                             | **Unity Catalog**            | No                         | Lake Formation          | Dataplex                  | Apache Ranger             |
| **Data Lineage**           | Seguir origen → transformación → destino    | Horizon                             | Unity Catalog                | Metadata limitada          | Glue                    | Dataplex                  | OpenLineage               |
| **BI**                     | Dashboards / reporting                      | Snowsight / partners                | Databricks SQL               | No                         | QuickSight              | **Looker**                | Superset                  |
| **ML Platform**            | Entrenamiento y lifecycle                   | Snowflake ML                        | **Databricks ML**            | No                         | **SageMaker**           | **Vertex AI**             | MLflow                    |
| **Experiment Tracking**    | Registrar experimentos                      | MLflow / Snowflake ML               | **MLflow**                   | No                         | SageMaker MLflow        | Vertex AI Experiments     | MLflow                    |
| **Model Registry**         | Versionar modelos                           | Snowflake Model Registry            | **MLflow Model Registry**    | No                         | SageMaker Registry      | Vertex AI Model Registry  | MLflow                    |
| **Model Serving**          | Servir modelos                              | Snowflake Model Serving             | Databricks Model Serving     | No                         | SageMaker Endpoints     | Vertex AI Endpoints       | KServe, BentoML           |
| **Feature Store**          | Gestionar features ML                       | Snowflake Feature Store             | **Databricks Feature Store** | No                         | SageMaker Feature Store | Vertex AI Feature Store   | Feast                     |
| **Vector Search**          | Búsqueda semántica                          | Cortex Search                       | Mosaic AI Vector Search      | No                         | OpenSearch / Aurora     | Vertex AI Vector Search   | Qdrant, Milvus, Weaviate  |
| **LLM / GenAI**            | LLMs y aplicaciones AI                      | Cortex AI                           | **Mosaic AI**                | No                         | Bedrock                 | Vertex AI                 | Hugging Face              |
| **RAG**                    | Retrieval + LLM                             | Cortex Search / AI                  | Mosaic AI                    | Puede almacenar documentos | Bedrock Knowledge Bases | Vertex AI Search          | LangChain, LlamaIndex     |
| **Agentic AI**             | Agentes y workflows                         | Cortex Agents                       | Mosaic AI Agent Framework    | No                         | Bedrock Agents          | Vertex AI Agent Engine    | LangGraph, CrewAI         |
| **Monitoring**             | Monitorizar pipelines/modelos               | Snowflake monitoring                | Databricks monitoring        | No                         | CloudWatch / SageMaker  | Cloud Monitoring / Vertex | Evidently, Grafana        |
| **CI/CD**                  | Deployment automático                       | Git integration                     | Databricks Asset Bundles     | No                         | CodePipeline / GitHub   | Cloud Build               | GitHub Actions, GitLab CI |
| **Infrastructure as Code** | Crear infraestructura                       | Terraform                           | Terraform                    | No                         | **Terraform / CDK**     | Terraform                 | Terraform, Pulumi         |

