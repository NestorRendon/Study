# Key Technical Projects — Interview Summary

**Prev:** [[03 - Industry Experience]] · **Related:** [[01 - Interview Narrative]]

---

## Índice

1. [[#1. xTrap — AI-Based Pest Monitoring System]]
2. [[#2. xAgent — LLM-Based Intelligent Agent for xFarm]]
3. [[#3. UF-CIVI — Uncertainty Fréchet Distance Cluster Validation Index]]
4. [[#Common thread between the three projects]]
5. [[#Strongest interview angle]]
6. [[#4. FarmView — Irrigation Management]]
7. [[#5. xFarm — Plant Identification]]
8. [[#FarmView vs Plant Identification — comparison]]
9. [[#Preguntas abiertas por preparar]]

---

## 1. xTrap — AI-Based Pest Monitoring System

### Problem

xFarm needed an automated way to monitor agricultural pests using images captured by field devices. The challenge was to process large volumes of images and automatically identify and classify pests without requiring manual inspection of every image.

### My contribution

I worked on the development of the **AI inference and data pipeline** behind xTrap, integrating computer vision models with cloud infrastructure.

The system involved:

```text
xTrap Device
     ↓
Images
     ↓
Cloud Storage
     ↓
Data Processing
     ↓
YOLOv5 Inference
     ↓
Pest Detection
     ↓
Database / API
     ↓
xFarm Platform
```

Technologies: Python, YOLOv5, AWS Lambda, AWS S3, Docker, PostgREST, GCP, Label Studio.

### Technical challenges

One of the main challenges was deploying computer vision inference in a way that was:

- scalable
- cost-efficient
- reliable
- suitable for processing large numbers of images

I worked on the integration between the ML model and the cloud pipeline, including image storage, inference and communication with downstream services.

### Key engineering considerations

```text
Large number of images
        ↓
Cloud-based processing
        ↓
Serverless inference
        ↓
Automatic detection
        ↓
Structured results
```

The architecture allowed the ML component to be integrated into a larger agricultural monitoring platform rather than being an isolated research model.

### What this demonstrates

Computer Vision · ML deployment · Cloud architecture · Serverless computing · Data pipelines · Model inference · Production ML · Integration between ML and backend systems

### 30-second version

> "At xFarm, I worked on xTrap, an AI-based pest monitoring system. The system used images captured by field devices and computer vision models such as YOLOv5 to automatically detect pests. I worked on the ML inference pipeline and its integration with cloud infrastructure, including AWS Lambda, S3 and APIs. The interesting engineering challenge was making computer vision inference scalable and reliable enough to operate as part of a real agricultural platform rather than just as an offline ML experiment."

---

## 2. xAgent — LLM-Based Intelligent Agent for xFarm

### Problem

xFarm had a large amount of agricultural information and functionality distributed across different systems. Users needed a more natural way to interact with this information and perform tasks.

A traditional chatbot would only generate text, but the goal was to build a system capable of **reasoning, retrieving information and interacting with external tools and services**.

### My contribution

I worked on the design and development of an **LLM-based conversational agent** and its underlying agentic architecture.

Conceptually:

```text
                         User
                           ↓
                      xFarm Agent
                           ↓
                         LLM
                           ↓
              ┌────────────┼────────────┐
              ↓            ↓            ↓
           Tools        Retrieval     Context
              ↓            ↓            ↓
        xFarm APIs    Knowledge/Data   State
              │            │            │
              └────────────┼────────────┘
                           ↓
                       Response
```

The system was designed to move beyond simple prompt → response interactions.

### Ontology vs knowledge base vs knowledge graph

| Term | Plain English | Analogy |
|------|---------------|---------|
| **Ontology** | Allowed types & rules | Database **schema** |
| **Knowledge base** | All stored knowledge | The **database** |
| **Knowledge graph** | KB as nodes + edges | **Graph** view of the KB |

**Open world assumption (OWL):** "If we don't know, it might still be true" — vs SQL closed world.

### Key capabilities

Natural language understanding · LLM reasoning · Retrieval · Tool/API calls · Context management · Multi-step workflows · Interaction with business data

### Architectural challenge

One of the main challenges was deciding how much responsibility should be given to the LLM versus deterministic software components.

I treated the LLM as a reasoning component while keeping critical business operations behind controlled interfaces and tools.

```text
LLM
 ↓
Decision / reasoning
 ↓
Tool selection
 ↓
Controlled API
 ↓
Business system
```

This reduces the risk of allowing the model to directly modify critical systems.

### Engineering considerations

latency · reliability · hallucination control · tool execution · observability · error handling · scalability · cost of LLM inference · maintainability

### What this demonstrates

LLM applications · Agentic AI · RAG / retrieval · Tool calling · API integration · AI architecture · Backend engineering · Production AI · AWS/cloud infrastructure

### 30-second version

> "I also worked on xAgent, an LLM-based conversational agent for xFarm. The goal was to move beyond a traditional chatbot and allow the system to reason, retrieve information and interact with business systems through tools and APIs. I worked on the agent architecture and the integration between the LLM, retrieval components and external services. One of the key design decisions was keeping critical business operations behind controlled APIs rather than allowing the LLM to directly modify systems."

---

## 3. UF-CIVI — Uncertainty Fréchet Distance Cluster Validation Index

### Problem

During my PhD research, I worked on **unsupervised clustering for ecoacoustic data**.

A major challenge in unsupervised learning is that there is usually no ground-truth label telling us which clustering solution is correct — e.g. is 3 clusters better than 4? Traditional metrics such as Silhouette Score can provide useful information, but they do not always capture the uncertainty and structure of complex ecological data.

### My contribution

I developed an **Uncertainty Clustering Internal Validity Index based on the Fréchet distance**, referred to as **UF-CIVI**, to evaluate clustering solutions while explicitly considering the **uncertainty associated with cluster assignments**.

Conceptually:

```text
Ecoacoustic Data
       ↓
Unsupervised Clustering
       ↓
Cluster Membership / Uncertainty
       ↓
Distribution of Cluster Characteristics
       ↓
Fréchet Distance
       ↓
Cluster Validation Score
```

### Why Fréchet Distance?

Fréchet distance measures similarity between distributions or trajectories while considering their overall structure. I used this concept to compare clustering structures and evaluate how well-defined and distinguishable the resulting clusters were — moving beyond "how far apart are the cluster centers?" to "how different are the structures/distributions represented by the clusters?"

### Methodology

```text
Ecoacoustic Recordings
          ↓
Acoustic Features
          ↓
Feature Engineering
          ↓
GMM Clustering
          ↓
Cluster Uncertainty
          ↓
UF-CIVI
          ↓
Compare different K
          ↓
Select / evaluate clustering solution
```

I used **Gaussian Mixture Models (GMMs)** because they provide probabilistic cluster assignments rather than only hard labels — useful because ecological acoustic environments are not necessarily cleanly separated:

```text
Point
70% → Cluster A
25% → Cluster B
 5% → Cluster C
```

That uncertainty contains useful information.

### Comparison with other metrics

I compared the proposed methodology with traditional internal clustering validation approaches, including Silhouette, MR, BH, SD, WG — to determine whether the uncertainty-based approach provides useful information for selecting and interpreting clustering structures.

### Ecological application

```text
Audio Recordings
       ↓
Acoustic Indicators
       ↓
Unsupervised Clustering
       ↓
Cluster Validation
       ↓
Spatial / Temporal Patterns
       ↓
Ecological Interpretation
```

The resulting clusters could then be compared with ecological and environmental indicators to determine whether the discovered acoustic patterns corresponded to meaningful ecological differences.

### 30-second version

> "During my PhD, I worked on unsupervised clustering of ecoacoustic data. One of the challenges was evaluating clustering solutions without ground-truth labels. I developed an internal cluster validation methodology based on uncertainty and Fréchet distance, using probabilistic clustering with Gaussian Mixture Models. The idea was to incorporate cluster assignment uncertainty and compare the structure of the resulting clusters rather than relying only on distance between cluster centers. I evaluated the methodology against several traditional internal clustering validation metrics and applied it to ecological acoustic monitoring."

---

## Common thread between the three projects

These projects may look very different, but they demonstrate the same engineering/research pattern:

```text
                    COMPLEX PROBLEM
                          ↓
                  Understand the data
                          ↓
                  Build a model/system
                          ↓
                  Evaluate performance
                          ↓
                  Identify uncertainty
                          ↓
                  Make engineering decisions
                          ↓
                     Deploy / Apply
                          ↓
                    Measure results
```

| Project | Core mix |
|---|---|
| xTrap | Computer Vision + Cloud + ML deployment |
| xAgent | LLM + Agents + APIs + Cloud |
| UF-CIVI | Machine Learning + Statistics + Uncertainty + Research |

Together, they demonstrate experience across:

| Area | Experience |
|---|---|
| Machine Learning | ✓ |
| Computer Vision | ✓ |
| LLMs | ✓ |
| Agentic AI | ✓ |
| Data Science | ✓ |
| Statistics | ✓ |
| Cloud | ✓ |
| AWS | ✓ |
| APIs | ✓ |
| ML Deployment | ✓ |
| Data Pipelines | ✓ |
| Uncertainty Modeling | ✓ |
| Research | ✓ |
| Production AI | ✓ |
| Ecological / Agricultural AI | ✓ |

---

## Strongest interview angle

The most valuable story is **not** simply:

> "I know YOLO, LLMs and GMM."

Instead:

> **"I have worked across the entire lifecycle of intelligent systems: from data and modeling, through evaluation and uncertainty, to cloud deployment and integration with real business systems."**

That connects your PhD experience with your industry experience:

```text
                  YOUR PROFILE
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
   Research        Industry          AI Systems
       │               │                │
       ↓               ↓                ↓
Statistics        Cloud/ML           LLM Agents
GMM               AWS                RAG
Uncertainty       APIs               Tools
Validation        Deployment         Workflows
       │               │                │
       └───────────────┼────────────────┘
                       ↓
              Production AI Engineer
```

---

## 4. FarmView — Irrigation Management

### Problem

Farmers need to decide **when and how much to irrigate** their crops. The challenge is that irrigation decisions depend on multiple factors: soil moisture, weather conditions, rainfall, temperature, crop type, crop growth stage, historical data, field characteristics.

The goal was to transform these heterogeneous data sources into useful irrigation information for the farmer.

### Architecture

```text
                    FARM / FIELD
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
    Soil Sensors      Weather       Satellite
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  Data Ingestion
                         │
                         ↓
                  Data Processing
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
        Historical Data        Real-time Data
              │                     │
              └──────────┬──────────┘
                         ↓
                   ML / Analytics
                         │
                         ↓
                Irrigation Model
                         │
                         ↓
              Irrigation Recommendation
                         │
                         ↓
                    FarmView
                         │
                         ↓
                     Farmer
```

### Data Flow

```text
Sensors
   ↓
Measurements
   ↓
Cloud ingestion
   ↓
Validation / Cleaning
   ↓
Feature Engineering
   ↓
ML / Agronomic Model
   ↓
Irrigation Recommendation
   ↓
FarmView
```

The system combines different sources of information rather than relying on a single sensor.

### Example

Suppose the system receives:

```text
Soil moisture      = Low
Temperature        = High
Rain forecast      = Low
Crop stage         = Flowering
Historical demand  = High
```

The system can infer:

```text
Water stress risk = High
        ↓
Irrigation needed
```

The final information can then be exposed through FarmView.

### Main technical challenges

**1. Heterogeneous data**

Different sources have different sampling frequencies, formats, units, missing values, time zones, spatial resolutions. Therefore, the pipeline needs a normalization layer.

```text
Sensor Data
     +
Weather
     +
Satellite
     ↓
Normalization
     ↓
Common representation
```

**2. Time-series data**

Irrigation is fundamentally a temporal problem. For example:

```text
Day 1 → Soil moisture = 35%
Day 2 → Soil moisture = 31%
Day 3 → Soil moisture = 27%
Day 4 → Soil moisture = 22%
```

The trend is often more informative than a single measurement.

**3. Missing data**

Sensors can fail or produce incomplete measurements. The system needs mechanisms for missing values, outliers, sensor failures, unexpected measurements.

### What this demonstrates

IoT data · Time-series data · Machine Learning · Data pipelines · Cloud architecture · Feature engineering · Agricultural AI · Decision-support systems

### 30-second version

> "FarmView is an agricultural decision-support system focused on irrigation. The challenge is combining heterogeneous sources such as soil sensors, weather and other agricultural data to estimate crop water requirements. The architecture involves data ingestion, normalization, time-series processing and agronomic or ML models that transform raw measurements into actionable irrigation recommendations."

---

## 5. xFarm — Plant Identification

### Problem

Farmers and agronomists may need to identify plants from images. The system uses computer vision to recognize plants from photographs. The challenge is that images can vary significantly because of lighting, camera angle, plant growth stage, background, occlusion, image quality, and different species.

The objective is to transform an image into a useful plant identification result.

### Architecture

```text
                         USER
                          │
                          ↓
                    Take / Upload
                       Image
                          │
                          ↓
                       xFarm
                          │
                          ↓
                     API Layer
                          │
                          ↓
                  Image Processing
                          │
                          ↓
                 Computer Vision Model
                          │
                          ↓
              ┌───────────┴───────────┐
              ↓                       ↓
          Detection              Classification
              │                       │
              └───────────┬───────────┘
                          ↓
                  Plant Identification
                          │
                          ↓
                  Confidence Score
                          │
                          ↓
                       xFarm
                          │
                          ↓
                        User
```

### ML pipeline

```text
Image
  ↓
Image Validation
  ↓
Pre-processing
  ↓
Object Detection
  ↓
Plant Region
  ↓
Classification
  ↓
Prediction
  ↓
Confidence
  ↓
Plant Identification
```

### Example

Input: image.

The computer vision model produces:

```text
Plant: Tomato
Confidence: 94%
```

Or:

```text
Plant: Corn
Confidence: 87%
```

The application can then use the identification result to provide additional agricultural information.

### Object Detection vs Classification

These are two different problems.

**Classification** — the model receives an image and answers "What is this?" → `Tomato`.

**Object Detection** — the model answers "What is this?" **+** "Where is it?" The output includes Class + Bounding Box + Confidence.

### Production architecture

```text
Mobile / Web
     │
     ↓
API Gateway
     │
     ↓
Image Service
     │
     ├──────────────→ Object Storage (S3)
     │
     ↓
Inference Service
     │
     ↓
Computer Vision Model
     │
     ↓
Prediction
     │
     ↓
Database
     │
     ↓
xFarm Application
```

### Important engineering considerations

**Latency** — if the user expects an immediate result, upload → inference → prediction needs to happen quickly. For slower inference, use asynchronous processing:

```text
Upload → Queue → Worker → Inference → Result
```

**Model performance** — Accuracy, Precision, Recall, F1, and for object detection specifically, **mAP** (mean Average Precision), plus inference latency.

**Data quality** — computer vision performance depends heavily on training data:

```text
Images → Annotation (Label Studio) → Dataset → Train/Val/Test → Model → Evaluation
```

Watch for class imbalance, annotation quality, data augmentation, and variability in lighting, cameras, and plant growth stages.

### 30-second version

> "The plant identification system uses computer vision to identify plants from images. The pipeline starts with image acquisition and preprocessing, followed by object detection or classification and then returns the predicted plant and confidence score. From an engineering perspective, the main challenges are model accuracy, image variability, inference latency and integrating the ML model into a reliable production API."

---

## FarmView vs Plant Identification — comparison

| Aspect | FarmView Irrigation | Plant Identification |
|---|---|---|
| Main problem | Irrigation decision support | Identify plants |
| Data | Sensors, weather, agricultural data | Images |
| ML type | Time-series / predictive modeling | Computer Vision |
| Input | Structured + time-series | Images |
| Output | Irrigation recommendation | Plant + confidence |
| Main challenge | Data integration + temporal modeling | Image variability + model accuracy |
| Infrastructure | Data pipeline + ML | Image pipeline + inference |
| Key metrics | Prediction error / agronomic metrics | Accuracy, Precision, Recall, mAP |
| Main users | Farmers / agronomists | Farmers / agronomists |
| AI role | Decision support | Visual recognition |

### Common architecture pattern

Although the two systems solve different problems, they follow the same fundamental architecture:

```text
                  REAL WORLD
                      ↓
                  Data Capture
                      ↓
                 Data Ingestion
                      ↓
                Data Processing
                      ↓
                ML / AI Model
                      ↓
                   Prediction
                      ↓
               Business Logic
                      ↓
                  xFarm App
                      ↓
                    User
```

> "I've worked on different types of agricultural AI systems, from sensor and time-series based decision support to computer vision. The common challenge is taking real-world, noisy data, building reliable ML pipelines around it, and integrating the models into production applications where the output needs to be actionable for farmers."

---

## Preguntas abiertas por preparar

- **Entity matching / record linkage:** Necesitas determinar si dos registros de empresa (nombres distintos, formato distinto, posiblemente distinto idioma) se refieren a la misma empresa real. ¿Cómo abordarías construir y evaluar un sistema de matching? Estás decidiendo entre usar un LLM para clasificar/matchear vs. un enfoque más barato basado en embeddings o reglas, a volumen de producción. ¿Cómo decidirías, y qué te haría elegir uno sobre el otro?
  - *Nota:* a diferencia del caso de `item_id` (ver Technical Interview Cheat Sheet, sección de algoritmos), aquí SÍ aplica un enfoque de similaridad — no hay un identificador exacto compartido entre los dos registros.
