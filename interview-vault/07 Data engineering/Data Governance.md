# Data Governance

> [!abstract] ¿Qué es Data Governance?
> **Data Governance** es el conjunto de reglas, procesos, responsabilidades y herramientas que permiten que los datos de una empresa sean **confiables, seguros, entendibles, trazables y utilizados correctamente**.

### En una frase

> **Data Engineering mueve y transforma los datos. Data Governance define cómo deben ser esos datos, quién puede usarlos y cómo sabemos que podemos confiar en ellos.**

---

---

# 2. Las principales áreas de Data Governance

Podemos dividirlo en seis áreas principales:

```text
                    DATA GOVERNANCE
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
   SECURITY             QUALITY            METADATA
       │                   │                   │
       ▼                   ▼                   ▼
     ACCESS              TRUST            KNOWLEDGE
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
           LINEAGE                  OWNERSHIP
```

| Área | Pregunta que responde |
| --- | --- |
| **Security & Access** | ¿Quién puede acceder a los datos? |
| **Data Quality** | ¿Podemos confiar en los datos? |
| **Metadata** | ¿Qué significan estos datos? |
| **Data Lineage** | ¿De dónde vienen los datos? |
| **Data Ownership** | ¿Quién es responsable de ellos? |
| **Policies & Compliance** | ¿Cómo podemos utilizar los datos? |

---

# 3. Data Security & Access

Determina **quién puede ver o modificar los datos**.

Por ejemplo:

```text
                    customers
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
     Analyst           Finance           Admin
       │                 │                 │
       ▼                 ▼                 ▼
     name              email          credit_score
     country           revenue        phone
```

Un Data Analyst podría tener:

```text
name          → ✅
country       → ✅
email         → 🟡
credit_score  → ❌
```

## Ejemplo

```text
Marketing Team
    ↓
Puede ver:
- customer_id
- country
- segment

NO puede ver:
- credit_score
- payment information
```

Esto se implementa mediante:

- Roles
- Permissions
- RBAC
- Row-level security
- Column-level security
- Data masking
- Encryption

---

# 4. Data Quality

Data Governance también significa asegurarse de que los datos sean **correctos y confiables**.

Por ejemplo:

```text
customer_id = NULL       ❌
email = "hello"          ❌
country = "Colombia"     ✅
age = -25                ❌
```

Podemos definir reglas:

```text
customer_id
    → NOT NULL

email
    → valid email

age
    → >= 0

country
    → valid country code
```

## Dimensiones comunes de Data Quality

| Dimensión | Pregunta |
| --- | --- |
| **Accuracy** | ¿El dato es correcto? |
| **Completeness** | ¿Faltan datos? |
| **Consistency** | ¿Es consistente entre sistemas? |
| **Validity** | ¿Cumple las reglas esperadas? |
| **Uniqueness** | ¿Hay duplicados? |
| **Timeliness** | ¿Está actualizado? |

---

# 5. Metadata

### ¿Qué es metadata?

> **Metadata = información sobre los datos.**

Por ejemplo:

```text
Table: customers

Description:
Registered customers.

Owner:
CRM Team

Update frequency:
Every 6 hours

Last update:
2026-08-09 10:00
```

Y para una columna:

```text
customer_id

Type:
INTEGER

Description:
Unique identifier for each customer.

Nullable:
NO
```

Esto permite que las personas entiendan **qué contienen los datos sin tener que inspeccionar todo el sistema**.

---

# 6. Data Catalog

Un **Data Catalog** es un inventario organizado de los datos disponibles.

Por ejemplo:

```text
DATA CATALOG

├── Customers
│   ├── customer_id
│   ├── name
│   ├── email
│   └── country
│
├── Sales
│   ├── order_id
│   ├── customer_id
│   ├── amount
│   └── date
│
└── Products
    ├── product_id
    ├── name
    └── category
```

Un catálogo permite encontrar:

- tablas
- columnas
- datasets
- propietarios
- descripciones
- calidad
- lineage
- sensibilidad
- permisos

---

# 7. Data Lineage

### ¿Qué es?

**Data lineage = saber de dónde viene un dato y qué ocurrió con él.**

Por ejemplo:

```text
PostgreSQL
    │
    ▼
raw_customers
    │
    ▼
silver_customers
    │
    ▼
customer_analytics
    │
    ▼
Power BI
```

Si alguien pregunta:

> "¿De dónde salió este número del dashboard?"

podemos seguir el camino hacia atrás.

```text
Revenue Dashboard
       ↑
customer_analytics
       ↑
silver_sales
       ↑
raw_sales
       ↑
PostgreSQL
```

---

# 8. ¿Por qué Lineage es importante?

Imagina que alguien cambia:

```text
customer_id
```

en PostgreSQL.

Podríamos tener:

```text
PostgreSQL
     │
     ▼
ETL
     │
     ▼
Snowflake
     │
     ▼
ML Features
     │
     ▼
ML Model
     │
     ▼
Prediction API
```

Un cambio aparentemente pequeño puede romper:

- pipelines
- dashboards
- features
- modelos
- APIs
- agentes de AI

Con **Data Lineage** podemos identificar qué sistemas dependen del dato.

---

# 9. Data Ownership

Alguien debe ser responsable de cada conjunto de datos.

Por ejemplo:

| Dataset | Owner |
| --- | --- |
| Customers | CRM Team |
| Sales | Sales Team |
| Payments | Finance Team |
| Products | Product Team |
| Employees | HR Team |

El owner puede ser responsable de:

- definición
- calidad
- acceso
- documentación
- políticas
- lifecycle

No significa necesariamente que esa persona sea quien programa los pipelines.

---

# 10. Policies & Compliance

También necesitamos reglas sobre **qué podemos hacer con los datos**.

Por ejemplo:

```text
Customer Data

name
    → internal

email
    → personal data

phone
    → personal data

credit_card
    → highly sensitive
```

Una política podría establecer:

```text
Email
    → masked for analysts

Phone
    → restricted

Credit Card
    → encrypted
    → restricted access
```

---

# 11. Data Classification

Podemos clasificar datos según su sensibilidad.

Ejemplo:

| Clasificación | Ejemplo | Acceso |
| --- | --- | --- |
| Public | Product name | Público |
| Internal | Internal metrics | Empleados |
| Confidential | Customer information | Equipos autorizados |
| Restricted | Credit card data | Muy restringido |

Esto permite aplicar políticas automáticamente.

---

# 12. Data Governance en una arquitectura moderna

Supongamos:

```text
                    DATA SOURCES
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      PostgreSQL        APIs           Kafka
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                    DATA LAKE
                         │
                         ▼
                    SNOWFLAKE
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
         BI              ML             AI
```

Data Governance está presente en **todas las capas**:

```text
             ┌──────────────────────────────┐
             │       DATA GOVERNANCE        │
             │                              │
             │  Security                    │
             │  Quality                     │
             │  Metadata                    │
             │  Lineage                     │
             │  Ownership                   │
             │  Policies                    │
             │  Compliance                  │
             └──────────────┬───────────────┘
                            │
                            ▼
Sources → Lake → Warehouse → BI / ML / AI
```

---

# 13. Herramientas de Data Governance

| Función | Snowflake | Databricks | AWS | Google Cloud | Open Source |
| --- | --- | --- | --- | --- | --- |
| Data Catalog | Horizon | Unity Catalog | Glue Catalog | Dataplex | OpenMetadata |
| Access Control | RBAC | Unity Catalog | Lake Formation | IAM / Dataplex | Apache Ranger |
| Data Lineage | Horizon | Unity Catalog | Glue | Dataplex | OpenLineage |
| Data Quality | Data Quality | Expectations | Glue Data Quality | Dataplex | Great Expectations |
| Metadata | Horizon | Unity Catalog | Glue | Dataplex | OpenMetadata |
| Data Classification | Policies | Unity Catalog | Macie | Sensitive Data Protection | Depende |
| Data Masking | Dynamic Masking | ABAC / policies | Lake Formation | Policy tags | Depende |
| Encryption | Native | Native | KMS | Cloud KMS | Depende |

---

# 14. Snowflake y Data Governance

Snowflake tiene una capa de governance integrada en su plataforma.

Conceptualmente:

```text
                     SNOWFLAKE
                         │
               ┌─────────┴─────────┐
               │                   │
             DATA              GOVERNANCE
               │                   │
               ▼                   ▼
           Tables              Access
           Views               Policies
           SQL                 Masking
           ML                  Lineage
                               Catalog
```

Puedes controlar:

```text
WHO
 │
 ├── Can access?
 │
 ├── Can modify?
 │
 └── Can see?
          │
          ▼
WHAT DATA
          │
          ▼
UNDER WHICH POLICY?
```

---

# 15. Databricks y Unity Catalog

En Databricks, **Unity Catalog** cumple una función central de governance.

Conceptualmente:

```text
Unity Catalog
      │
      ├── Catalogs
      │
      ├── Schemas
      │
      ├── Tables
      │
      ├── Views
      │
      ├── Models
      │
      ├── Permissions
      │
      ├── Lineage
      │
      └── Policies
```

Esto permite gestionar datos y otros assets desde una capa central.

---

# 16. Data Governance + Machine Learning

Esto es especialmente importante en ML.

Supongamos:

```text
Data
  │
  ▼
Features
  │
  ▼
Training
  │
  ▼
Model
  │
  ▼
Prediction
```

Governance permite responder:

```text
¿De dónde vienen las features?
        │
        ▼
¿Quién puede utilizarlas?
        │
        ▼
¿Qué versión de los datos se utilizó?
        │
        ▼
¿Qué modelo fue entrenado?
        │
        ▼
¿Quién puede utilizar el modelo?
```

Esto conecta:

```text
Data Governance
       +
ML Governance
       +
Model Governance
```

---

# 17. Data Governance + AI

Con sistemas de AI aparecen todavía más preguntas.

Por ejemplo, un **AI Agent** recibe una pregunta:

> "Dame la información financiera de este cliente."

Antes de responder, el sistema debería considerar:

```text
User
 │
 ▼
Authentication
 │
 ▼
Authorization
 │
 ▼
¿Puede acceder a este dato?
 │
 ├── NO → Reject
 │
 └── YES
       │
       ▼
   Retrieve Data
       │
       ▼
    Validate
       │
       ▼
      LLM
       │
       ▼
   Response
```

Por eso Data Governance es una pieza importante de la arquitectura de AI empresarial.

---

# 18. Data Governance vs Data Engineering

Una diferencia fácil de recordar:

| Data Engineering | Data Governance |
| --- | --- |
| Construye pipelines | Define reglas |
| Mueve datos | Define quién puede acceder |
| Transforma datos | Define estándares |
| Optimiza procesos | Controla calidad |
| Construye infraestructura | Define ownership |
| Implementa ETL/ELT | Define políticas |
| Trabaja con Spark, SQL, Airflow | Trabaja con catalog, policies, lineage |

### Pero trabajan juntos

```text
Data Governance
       │
       │ defines rules
       ▼
Data Engineering
       │
       │ implements rules
       ▼
Data Platform
       │
       ▼
Trusted Data
```

---

# 19. Ejemplo completo

Imagina una empresa de e-commerce.

Tiene:

```text
PostgreSQL
    │
    ▼
Customer Data
```

Los datos llegan a:

```text
Snowflake
```

Tenemos:

```text
customers

customer_id
name
email
phone
country
credit_score
```

### Governance define:

```text
customer_id
→ Primary identifier

email
→ Personal information

phone
→ Personal information

credit_score
→ Restricted

Owner
→ CRM Team

Update
→ Every 6 hours
```

### Security

```text
Marketing
    → name, country

Sales
    → name, email, country

Finance
    → credit_score

Admin
    → everything
```

### Quality

```text
customer_id → NOT NULL
email       → valid format
country     → valid country
credit_score → 0–1000
```

### Lineage

```text
PostgreSQL
    ↓
raw_customers
    ↓
silver_customers
    ↓
customer_analytics
    ↓
Power BI
```

Ahora tenemos un dataset:

> **Confiable + documentado + protegido + trazable.**

Eso es el objetivo de Data Governance.

---

# 20. Governance Checklist

Cuando diseñes una arquitectura de datos, pregunta:

### 🔐 Security

- [ ] ¿Quién puede acceder?
- [ ] ¿Quién puede modificar?
- [ ] ¿Hay datos sensibles?
- [ ] ¿Necesitamos masking?
- [ ] ¿Necesitamos encryption?

### ✅ Quality

- [ ] ¿Los datos son correctos?
- [ ] ¿Hay duplicados?
- [ ] ¿Hay valores NULL?
- [ ] ¿Los datos están actualizados?
- [ ] ¿Existen reglas de validación?

### 📖 Metadata

- [ ] ¿Qué significa cada tabla?
- [ ] ¿Qué significa cada columna?
- [ ] ¿Cuándo se actualizó?
- [ ] ¿Quién la utiliza?

### 🔎 Lineage

- [ ] ¿De dónde vienen los datos?
- [ ] ¿Qué pipelines los transforman?
- [ ] ¿Qué dashboards dependen de ellos?
- [ ] ¿Qué modelos ML los utilizan?

### 👤 Ownership

- [ ] ¿Quién es responsable?
- [ ] ¿Qué equipo mantiene el dataset?
- [ ] ¿Quién aprueba cambios?

### ⚖️ Policies

- [ ] ¿Qué usos están permitidos?
- [ ] ¿Hay restricciones legales?
- [ ] ¿Cuánto tiempo debemos conservar los datos?
- [ ] ¿Podemos utilizar estos datos para ML/AI?

---

# 21. Resumen

```text
DATA GOVERNANCE
│
├── Security
│   └── ¿Quién puede acceder?
│
├── Quality
│   └── ¿Podemos confiar?
│
├── Metadata
│   └── ¿Qué significa?
│
├── Lineage
│   └── ¿De dónde viene?
│
├── Ownership
│   └── ¿Quién es responsable?
│
└── Policies
    └── ¿Cómo podemos utilizarlo?
```

### La idea que debes recordar

> **Data Governance convierte datos que simplemente existen en datos que una organización puede confiar y utilizar de manera controlada.**

Y en una arquitectura moderna:

```text
Data Engineering
        ↓
    DATA PLATFORM
        ↓
Data Governance
        ↓
  TRUSTED DATA
        ↓
 ┌──────┼──────┐
 ▼      ▼      ▼
 BI     ML     AI
```

---

# 22. Conceptos relacionados

Si estás aprendiendo Data Engineering / AI Architecture, los siguientes conceptos están directamente relacionados:

```text
Data Governance
│
├── Data Quality
├── Data Catalog
├── Data Lineage
├── Data Ownership
├── Data Security
├── Data Classification
├── Data Privacy
├── Access Control
├── Data Contracts
├── Master Data Management
├── Metadata Management
└── Compliance
```

Y estos se conectan con:

```text
Data Engineering
        │
        ├── ETL / ELT
        ├── Data Pipelines
        ├── Data Lake
        ├── Data Warehouse
        └── Lakehouse
                 │
                 ▼
          Data Governance
                 │
          ┌──────┴──────┐
          ▼             ▼
         ML            AI
          │             │
          ▼             ▼
       MLOps       AI Governance
```