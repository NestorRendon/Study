# AI Business Handbook

# State of the Art AI Stack (2026)

| Layer           | Best Tool                                                              |
| --------------- | ---------------------------------------------------------------------- |
| LLM             | GPT-5 / Claude 4 Opus                                                  |
| Agent Framework | LangGraph                                                              |
| RAG             | LlamaIndex                                                             |
| Vector DB       | Qdrant                                                                 |
| Embeddings      | OpenAI text-embedding-3-large, **Voyage AI** embedding models (Claude) |
| Evaluation      | LangSmith + DeepEval + Langfuse + Phoenix                              |
| Serving         | vLLM                                                                   |
| Backend         | FastAPI                                                                |
| Database        | PostgreSQL                                                             |
| Cache           | Redis                                                                  |
| Workflow        | Temporal                                                               |
| Containers      | Docker + Kubernetes                                                    |
| Cloud           | AWS or Google Cloud                                                    |

# AI for Business Stack

## End-to-End Flow

```text
Business Data
    |
Data Collection
    |
Storage
    |
ETL / Processing
    |
ML / LLM
    |
API / Backend
    |
Applications
    |
Monitoring
```

## Cloud Services Comparison

| Layer | AWS | Google Cloud | Azure | Open Source |
| --- | --- | --- | --- | --- |
| Data Storage | S3 | Cloud Storage | Blob Storage | MinIO |
| SQL Database | RDS | Cloud SQL | Azure SQL | PostgreSQL |
| NoSQL | DynamoDB | Firestore | Cosmos DB | MongoDB |
| Data Warehouse | Redshift | BigQuery | Synapse | ClickHouse |
| Streaming | Kinesis | Pub/Sub | Event Hub | Kafka |
| ETL | Glue | Dataflow | Data Factory | Airflow |
| Workflow | Step Functions | Workflows | Logic Apps | Prefect, Dagster |
| Serverless | Lambda | Cloud Functions | Azure Functions | OpenFaaS |
| Containers | ECS / EKS | GKE | AKS | Kubernetes |
| API Gateway | API Gateway | API Gateway | API Management | Kong, Traefik |
| Authentication | Cognito | Firebase Auth | Entra ID | Keycloak |
| Secrets | Secrets Manager | Secret Manager | Key Vault | Vault |
| Monitoring | CloudWatch | Cloud Monitoring | Azure Monitor | Grafana |
| Logging | CloudWatch Logs | Cloud Logging | Azure Monitor Logs | ELK |
| Messaging | SQS / SNS | Pub/Sub | Service Bus | RabbitMQ |

## AI & LLM Services

| Task              | AWS         | Google    | Azure             | Open Source          |
| ----------------- | ----------- | --------- | ----------------- | -------------------- |
| Foundation Models | Bedrock     | Vertex AI | Azure OpenAI      | Hugging Face         |
| GPT Models        | Bedrock     | Gemini    | Azure OpenAI      | OpenAI API           |
| Claude            | Bedrock     | Vertex AI | Azure             | Anthropic API        |
| Llama             | Bedrock     | Vertex AI | Azure             | Ollama, Hugging Face |
| Image Models      | Titan Image | Imagen    | DALL·E            | Stable Diffusion     |
| Embeddings        | Titan       | Gemini    | OpenAI Embeddings | BGE, E5              |

## Vector Databases

| AWS | Google | Azure | Alternatives |
| --- | --- | --- | --- |
| OpenSearch Vector | Vertex AI Vector Search | AI Search | Pinecone, Weaviate, Milvus, Qdrant, ChromaDB, pgvector |

## AI Frameworks

| Purpose | Tools |
| --- | --- |
| LLM Apps | LangChain |
| Multi-Agent | LangGraph |
| Multi-Agent | CrewAI |
| Multi-Agent | AutoGen |
| Agent SDK | OpenAI Agents SDK |
| Orchestration | Semantic Kernel |
| RAG | LlamaIndex |
| Pipelines | Haystack |

## Training

| Task | AWS | Google | Open Source |
| --- | --- | --- | --- |
| Training | SageMaker | Vertex AI | PyTorch |
| HPO | SageMaker | Vertex Vizier | Optuna |
| Distributed | SageMaker | Vertex | Ray |
| Tracking | SageMaker | Vertex | MLflow |
| Registry | SageMaker | Vertex | MLflow |

## Evaluation

| Category | Tools |
| --- | --- |
| LLM Evaluation | LangSmith |
| Prompt Testing | Promptfoo |
| Observability | Arize Phoenix |
| Tracing | Langfuse |
| RAG Evaluation | Ragas |
| Human Evaluation | Label Studio |

## Deployment

| Purpose | AWS | Google | Alternative |
| --- | --- | --- | --- |
| REST API | Lambda + API Gateway | Cloud Run | FastAPI |
| Containers | ECS | Cloud Run | Docker |
| Kubernetes | EKS | GKE | Kubernetes |
| CI/CD | CodePipeline | Cloud Build | GitHub Actions |

# Glossary

| Term | Definition |
| --- | --- |
| ETL | Extract, Transform, Load: move data from source systems, clean/transform it, then load it into a database or warehouse. |
| Data Lake | Repository for raw structured and unstructured data. |
| Data Warehouse | Optimized analytical database for reporting and BI. |
| API | Interface allowing software systems to communicate. |
| API Gateway | Single entry point for APIs, handling routing, auth, throttling, and monitoring. |
| Serverless | Execute code without managing servers. |
| Container | Packaged application with dependencies (e.g. Docker). |
| Kubernetes | Platform for deploying and scaling containers. |
| Workflow Orchestration | Coordinates multi-step tasks and dependencies. |
| RAG | Retrieval-Augmented Generation. Retrieves relevant documents before querying an LLM. |
| Embeddings | Dense numeric vectors representing semantic meaning. |
| Vector Database | Database optimized for similarity search over embeddings. |
| LLM | Large Language Model (GPT, Claude, Gemini, Llama). |
| Agent | LLM that can reason, call tools, and execute actions. |
| Multi-Agent System | Multiple specialized agents collaborating. |
| Prompt Engineering | Designing prompts for reliable outputs. |
| Fine-tuning | Additional training on domain-specific data. |
| Inference | Running a trained model to generate predictions or responses. |
| MLOps | Practices for deploying and maintaining ML systems. |
| Observability | Monitoring logs, metrics, traces, and model quality. |
| CI/CD | Continuous Integration / Continuous Deployment. |
| Event Streaming | Processing continuous event streams in real time. |
| SQL | Relational databases. |
| NoSQL | Non-relational databases for flexible schemas and scale. |
