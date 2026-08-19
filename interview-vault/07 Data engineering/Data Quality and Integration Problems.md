# Data Quality & Data Integration Problems

> [!abstract] What is this document about?
> These are the problems that show up **over and over** when you combine data from multiple sources or try to trust it: duplicate records, the same customer with two IDs, fields that don't line up, schemas that change, conflicting values, etc.
> Explained simply here, with example, cause, and **how to solve** each one — meant for a quick review before an interview.

### In one sentence

> **Entity Resolution is the most famous problem in this family, but it's just one of many. They all share the same question: "does this data represent the same thing, and which version do I trust?"**

---

# 1. The full map

```text
                DATA QUALITY / INTEGRATION PROBLEMS
                             │
        ┌───────────────────┼───────────────────────┐
        │                   │                        │
        ▼                   ▼                        ▼
   "IS IT THE SAME?"   "WHAT DOES IT MEAN?"     "WHICH ONE IS RIGHT?"
        │                   │                        │
        ▼                   ▼                        ▼
 Entity Resolution   Schema Matching          Data Fusion /
 Record Linkage      Schema Mapping           Conflict Resolution
 Deduplication       Schema Evolution         Golden Record (MDM)
 Coreference Res.
        │                   │                        │
        └───────────────────┼────────────────────────┘
                             ▼
                    "IS THE DATA GOOD?"
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       Data Cleaning   Missing Data    Anomaly / Outlier
       Standardization  Imputation       Detection
```

| Problem | Question it answers |
| --- | --- |
| **Entity Resolution / Record Linkage** | Do these records refer to the same real-world entity? |
| **Deduplication** | Does this record already exist in the same source? |
| **Schema Matching/Mapping** | Is this field in A the same concept as that field in B? |
| **Data Fusion / Conflict Resolution** | If two sources disagree, which value do I use? |
| **Golden Record / MDM** | What's the single, trustworthy version of this entity? |
| **Data Cleaning** | Is the data well-formed? |
| **Missing Data** | What do I do when a value is missing? |
| **Anomaly Detection** | Is this value suspicious? |
| **Referential Integrity** | Does this FK point to something that actually exists? |
| **Schema Evolution** | What happens when the source changes its structure? |
| **CDC Consistency** | Is my copy still in sync with the source? |
| **Slowly Changing Dimensions** | How do I store the history of changes for an entity? |

---

# 2. Entity Resolution (ER) / Record Linkage

> [!abstract] Definition
> Determining whether two or more records — from the same source or from different sources — represent **the same real-world entity** (person, company, product), even if they're written differently.

```text
"Nestor Rendon"   vs   "N. Rendon"        → same person?
"IBM Corp"        vs   "International
                        Business Machines"  → same company?
```

### Why it happens

- Typos, inconsistent formats, abbreviations
- No shared unique identifier across systems
- Sources capturing the same real-world fact independently

### How it's solved — typical pipeline

```text
1. BLOCKING
   Group candidates so you don't compare everything against everything (O(n²))
        │
        ▼
2. SIMILARITY
   Compare fields: Jaro-Winkler, Levenshtein, embeddings
        │
        ▼
3. CLASSIFICATION
   Is it a match or not? → rules, Fellegi-Sunter, ML, LLM
        │
        ▼
4. CLUSTERING
   Group all matches into a single entity
        │
        ▼
5. GOLDEN RECORD
   Merge into one trustworthy record
```

| Technique | When to use it |
| --- | --- |
| Rules / thresholds | Few fields, simple logic, needs to be explainable |
| Fellegi-Sunter (probabilistic) | Classic statistical baseline, solid theory |
| Supervised ML (XGBoost, etc.) | You have labeled match/non-match pairs |
| Deep learning (Ditto, Siamese nets) | Very messy data / free text |
| LLM prompting | Few examples, ambiguous cases, quick prototypes |

**Tools:** Dedupe, Splink, Zingg, OpenRefine

| Tool | Approach | Scale | Best for |
| --- | --- | --- | --- |
| **Dedupe** (Python) | Active learning — you label a handful of pairs, it trains a matching model | Small/medium (single machine, in-memory) | Quick projects, prototypes, when you don't have pre-labeled training data |
| **Splink** (UK Ministry of Justice) | Probabilistic (Fellegi-Sunter), runs on Spark/DuckDB/SQL engines | Large scale (millions of rows) | Production pipelines, when you want statistical rigor and full SQL transparency |
| **Zingg** | ML-based, similar workflow to Dedupe but built for big data | Large scale (runs on Spark) | When you need Dedupe-style active learning but at big-data scale |
| **OpenRefine** | Interactive, manual/GUI-driven clustering (facets, clustering algorithms) | Small (desktop tool) | Exploratory data cleaning, one-off manual dedup, non-engineers |

> [!tip] Short interview answer
> "ER combines blocking to cut down candidates, similarity scoring to compare fields, and a classifier (rules, probabilistic, or ML) to decide match/non-match. Then clustering groups everything that belongs to the same entity."

---

# 3. Deduplication

> [!abstract] Definition
> A special case of ER: removing duplicate records **within a single source**, without needing to merge attributes across different systems.

```text
customers
│
├── id=1  "John Smith"  john@mail.com
├── id=2  "Jon Smith"   john@mail.com   ← duplicate
└── id=3  "Ana Gomez"   ana@mail.com
```

**Solution:** same pipeline as ER (blocking + similarity + matching), but scoped to one table. Simple cases are typically handled with `ROW_NUMBER() OVER (PARTITION BY ...)` in SQL; fuzzy cases use the same ER libraries.

---

# 4. Schema Matching / Schema Mapping

> [!abstract] Definition
> Before you can compare records, you need to know that **the fields mean the same thing**.

```text
System A             System B
─────────            ─────────
cust_name      ≈      full_name
cust_email     ≈      email_address
dob            ≈      birth_date
```

### How it's solved

- **Manual mapping**: documented by a data steward (most reliable, doesn't scale)
- **Name similarity**: comparing column names (string similarity)
- **Value similarity**: comparing distributions/data types between columns
- **ML/embeddings**: models that learn mappings from historical examples
- **Data Contracts**: agree on the schema upfront between producer/consumer teams to prevent the problem altogether

---

# 5. Data Fusion / Conflict Resolution

> [!abstract] Definition
> You already know two records are the same entity. **Which value do you keep when the fields disagree?**

```text
Source A: phone = "300-123-4567"   (updated: 2026-01-01)
Source B: phone = "300-999-8888"   (updated: 2026-08-01)
                    │
                    ▼
              Which one is correct?
```

### Common strategies

| Strategy                | Logic                                                |
| ----------------------- | ---------------------------------------------------- |
| **Most recent**         | The value with the newest timestamp wins             |
| **Most trusted source** | A source hierarchy is defined (e.g., CRM > web form) |
| **Majority vote**       | With 3+ sources, the most repeated value wins        |
| **Completeness-based**  | The record with fewer empty fields wins              |
| **Manual review**       | High-impact cases get reviewed by a human            |
Un CRM (_Customer Relationship Management_ o gestión de relaciones con los clientes) es una ==herramienta digital que centraliza toda la información de contactos, ventas, llamadas y correos en un solo lugar==. A
---

# 6. Golden Record / Master Data Management (MDM)

> [!abstract] Definition
> The end result of ER + Data Fusion: **a single trustworthy version of each entity**, used across the whole organization.

```text
CRM:        "John Smith", john.s@mail.com
Billing:    "J. Smith",   jsmith@old-mail.com
Support:    "John S.",    john.s@mail.com
                    │
                    ▼
            ENTITY RESOLUTION
                    │
                    ▼
            DATA FUSION
                    │
                    ▼
┌─────────────────────────────────┐
│         GOLDEN RECORD           │
│  name: John Smith               │
│  email: john.s@mail.com         │
│  source_ids: [CRM:1, BIL:9]     │
└─────────────────────────────────┘
```

**Tools:** Reltio, Informatica MDM, Profisee — or built custom on top of Splink/Zingg + fusion rules.

---

# 7. Data Cleaning / Standardization

> [!abstract] Definition
> Normalizing formats **before** trying to compare or load the data — otherwise ER and everything downstream breaks.

```text
"usa"        → "United States"
"US"         → "United States"
"+1 555..."  → "+15551234567"
"2026/08/12" → "2026-08-12"
```

**Solution:** normalization rules, parsing libraries (e.g. `libpostal` for addresses), format validation (regex for emails, phone numbers).

---

# 8. Missing Data / Imputation

> [!abstract] Definition
> What to do when a field is empty or null.

| Strategy | When to use it |
| --- | --- |
| Drop the record | Low null %, and the field is critical |
| Default value | Categorical fields with a valid "unknown" bucket |
| Statistical imputation (mean/median/mode) | Numeric fields, to avoid breaking aggregations |
| Model-based imputation (regression, KNN) | Strong correlation with other columns |
| Leave it explicitly NULL | When "we don't know" is itself valid information |

---

# 9. Anomaly / Outlier Detection

> [!abstract] Definition
> Catching suspicious values that likely indicate a capture error or an upstream pipeline bug.

```text
age = -25         ❌
age = 900         ❌
revenue = -100000 ❌ (if it should never be negative)
```

**Solution:** range rules (`age BETWEEN 0 AND 120`), z-score / standard deviation, Isolation Forest, or frameworks like **Great Expectations** / **Soda** that run these checks as part of the pipeline (data quality gates).

---

# 10. Referential Integrity

> [!abstract] Definition
> A foreign key points to a record that doesn't exist (or was deleted/duplicated).

```text
orders.customer_id = 445
                │
                ▼
customers.id = 445   → does it exist? ❌
```

**Solution:** database-level constraints when possible; in batch pipelines, orphan-record checks before publishing a table (e.g. `LEFT JOIN ... WHERE right.id IS NULL`).

---

# 11. Schema Evolution

> [!abstract] Definition
> The source changes its structure (adds/renames/drops columns) and breaks everything downstream that depends on it.

```text
v1: { "name": "John" }
v2: { "first_name": "John", "last_name": "Smith" }   ← breaking change
```

**Solution:** schema versioning (Schema Registry in Kafka/Avro/Protobuf), **Data Contracts** between producer and consumer, compatibility checks (backward/forward compatible) before deploying changes.

---

# 12. Change Data Capture (CDC) Consistency

> [!abstract] Definition
> Keeping a downstream copy in sync with the source, without duplicating or losing changes to an entity.

```text
PostgreSQL (source)
    │  INSERT / UPDATE / DELETE
    ▼
CDC (Debezium, etc.)
    │
    ▼
Kafka topic
    │
    ▼
Data Warehouse (replica)
```

**Risks:** duplicate events (at-least-once delivery), out-of-order events, or the consumer crashing and losing its offset. **Solution:** idempotent operations (upsert by PK), ordering by timestamp/LSN, offset checkpointing.

---

# 13. Slowly Changing Dimensions (SCD)

> [!abstract] Definition
> How to store the **history** of changes for an entity in a Data Warehouse, instead of just the current value.

| Type | Behavior |
| --- | --- |
| **Type 0** | Never changes (immutable) |
| **Type 1** | Overwrites the old value (history is lost) |
| **Type 2** | Creates a new row with a date range (`valid_from`/`valid_to`) — full history |
| **Type 3** | Keeps only the previous value in an extra column (`previous_value`) |

```text
Type 2 example:

customer_id | address        | valid_from | valid_to   | current
1           | 10th Street    | 2024-01-01 | 2025-06-01 | false
1           | 45th Street    | 2025-06-01 | NULL       | true
```

---

# 14. Privacy-Preserving Record Linkage (PPRL)

> [!abstract] Definition
> Doing ER **across two different organizations** without either one exposing raw PII to the other — common in healthcare, government, banking.

```text
Hospital A                          Hospital B
"John Smith, SSN 123"               "J. Smith, SSN 123"
        │                                   │
        ▼                                   ▼
   Bloom Filter Hash  ───────────────  Bloom Filter Hash
        │                                   │
        └─────────────── ▼ ─────────────────┘
                   Compare hashes
                (without seeing raw data)
```

**Techniques:** Bloom filter encoding, secure multi-party computation (SMPC), hashing with a shared salt.

---

# 15. Summary — quick interview table

| Problem | One-sentence solution |
| --- | --- |
| Entity Resolution | Blocking + similarity + classifier (rules/ML) + clustering |
| Deduplication | ER applied within a single source |
| Schema Matching | Compare column names/values, or use Data Contracts |
| Data Fusion | Priority rules: most recent / most trusted / majority vote |
| Golden Record (MDM) | ER + Fusion, maintained as the single source of truth |
| Data Cleaning | Normalize format before comparing |
| Missing Data | Drop, default, or impute depending on the case |
| Anomaly Detection | Valid ranges, z-score, or frameworks like Great Expectations |
| Referential Integrity | DB constraints or orphan-record checks |
| Schema Evolution | Schema Registry + Data Contracts + compatibility checks |
| CDC Consistency | Idempotent upserts + ordering + checkpointing |
| SCD | Type 2 to keep full history |
| PPRL | Bloom filters / SMPC for linkage without exposing PII |

```text
DATA ENGINEERING PROBLEM FAMILY
│
├── Is it the same?        → Entity Resolution, Deduplication
├── What does it mean?     → Schema Matching, Schema Evolution
├── Which one is right?    → Data Fusion, Golden Record / MDM
├── Is the data good?      → Cleaning, Missing Data, Anomalies
├── Is it still in sync?   → CDC, Referential Integrity
└── How do I store change? → Slowly Changing Dimensions
```

> [!tip] The idea to remember
> All of these problems are variations of the same underlying challenge: **data comes from different systems, captured in different ways, and your job is to make it trustworthy and coherent before someone makes a decision with it.**

---

# 16. Related concepts

```text
Data Quality / Integration
│
├── Entity Resolution
├── Record Linkage
├── Deduplication
├── Schema Matching
├── Data Fusion
├── Master Data Management
├── Data Cleaning
├── Data Contracts
├── Change Data Capture
└── Slowly Changing Dimensions
```

Related to → [[Data Governance]] (Data Quality is one of its core areas).
