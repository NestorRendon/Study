  
# Interview  DELVI  
  
## Education  
* Bachelor’s in Electronic Engineering  
* MSc in Machine Learning  
* PhD in Data Science & Statistical Modeling  
  
# Industrial Experience  
## 2017 – Intelligent Electronic Solutions  
* C++ / Object-Oriented developer  
* Development of gambling machines  
  
## 2018–2020 – Machine Learning Research in Soundscape Ecology I used machine learning to automatically detect hidden patterns in audio recordings.  
Timeseries, extreme gradient boosting,   
clustering   
Non labelled data  
Labelled data   
  
## 2020–2021 – Machine Learning Engineer at SUPSI-DTI (Switzerland)  
Developed deep learning pipelines for object detection systems,  yolo for detecting multiple insects  
* **Main challenges:**  
    * Lack of data  
    * Generation of synthetic images  
    * Data augmentation  
Datamanagement,   
Synthetic data generation   
DB data   
AWS   
Experiments :  
Developed software modules for data acquisition and preprocessing  
 Vision preprocessing  for images taking in not controlled environments   
Statistical analysis    
Product:  [https://www.xfarm.ag/en/xtrap-delta-pro](https://www.xfarm.ag/en/xtrap-delta-pro)  
  
  
## 2021–2024  
* Identified acoustic clusters to discover latent behaviors and associate them with functional animal/landscape characteristics  
**Challenge Identified:**  
*  determining the optimal number of clusters was difficult  
Based on this research gap, I began working on an metric to determine the correct number of clusters.  
*The approach modeled uncertainty by analyzing the probability of belonging to a class*  
While working on my PhD, I also collaborated with xFarm as a consultant (20–30%)  
* Implemented and fine-tuned object detection systems and computer vision algorithms (YOLO, segmentation)  
  
  
## 2024– until now   
* Designed modular software components for integrating AI vision models into production systems   
* Xtrap : counting insects, Labelling management , camera calibration, errors in positions   
* xScan:  resnet50 PyTorch to plant illness identifier   
       Farmview: Counting fruits: apples, apricots, pear  in not controlling environments  with embedded devices    
			Tracking   
			 Collaboration in detecting the density by use of intelrealsense point cloud/  3d occupancy grid  
* Developed multi-agent and agent-based orchestration frameworks for agronomic applications  
**Challenges handled:**  
**	Computational limitations: **  
**         Jetson nano realtime,**  
**         lack of data , **  
**         false positives **  
** 	variazioni della luce **  
  
Agent development   
* **Applications included:**  
    * Weather information  
    * Insect pest control  
    * Irrigation systems  
**Technologies used:**  
* LangGraph  
* LangChain  
Later, we decided to continue working with Google ADK (a framework for agent/tool-use APIs).  
**We experimented with:**  
* Embeddings  
* Fine-tuning  
* Guardrails  
* Evaluation metrics like  LLM-as-evaluator  
* Trajectory Success  
  
  
  
Fruit counting  embeded devises    
ONNX, TensorRT  
Density estimation   
intel realsense d435 : infrared mapping   
  
  
Cosas para aprender hoy :   
  
* 0ttima padronanza di Python  
* Esperienza con un linguaggio di programmazione a oggetti (preferibilmente Java)  
* Esperienza nella Computer Vision classica (specialmente OpenCV)  
* Esperienza con almeno uno dei principali framework di IA (preferibilmente PyTorch)  
* Esperienza con le Reti Neurali applicate alla computer vision e/o alla previsione di serie temporali (time series)  
  
  
Ciao, come da accordi intercorsi per le vie brevi di seguito il link del sito aziendale https://delvi.tech/  
ti lascio altresì la job description [https://www.techyon.it/candidati/aiengineer-ai-mendrisio.html](https://www.techyon.it/candidati/aiengineer-ai-mendrisio.html)  
  
  
  
**Prof. Jürgen Schmidhuber**  
reti neurali ricorrenti.  
  
**Long Short-Term Memory (LSTM)**  
Residual Networks (ResNets)  
**Generative Adversarial Networks (GANs)**  
  
Serial Peripheral Interface (SPI) is a de facto standard (with many variants) for synchronous serial communication, used primarily in embedded systems for short-distance wired communication between integrated circuits.   
The term **AOI protocol** can refer to several distinct concepts depending on the industry. Most commonly, it refers to the standardized steps for **Automated Optical Inspection** in electronics manufacturing,  
  
  
  
# delvi  
  
**reti neurali proprietarie e ottica avanzata 3D**  
  
  
**Tabla 1 — Resumen Intel RealSense D435 + Jetson Nano + ROS**  

| Componente | Descripción | Ventajas | Limitaciones |
| -------------------- | ------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| Intel RealSense D435 | Cámara RGB-D con percepción de profundidad | Compacta, económica, fácil integración con ROS | Sensible a luz solar y superficies reflectivas |
| Tecnología 3D | Stereo Vision Activa + Proyector IR | Profundidad densa en tiempo real | Menor precisión que LiDAR a larga distancia |
| NVIDIA Jetson Nano | Computador embebido para procesamiento edge | Bajo consumo, GPU CUDA | Recursos limitados para SLAM pesado |
| ROS | Middleware robótico | Modular, ecosistema grande | Curva de aprendizaje alta |
| Mapeo 3D | Integración depth + pose | Reconstrucción espacial en tiempo real | Requiere buena odometría |
  
**Tabla 2 — Algoritmos / Stack Recomendado para Mapping y Monitoreo**  

| Herramienta / Algoritmo | Función Principal | Uso Típico | Requerimiento Computacional |
| ----------------------- | ---------------------------------- | --------------------------------- | --------------------------- |
| RTAB-Map | RGB-D SLAM / Mapping 3D | Reconstrucción y navegación | Medio–Alto |
| ORB-SLAM3 | Visual SLAM preciso | Tracking / odometría visual | Medio |
| OctoMap | Mapa probabilístico 3D ocupacional | Navegación / planeación | Medio |
| ICP | Registro de nubes de puntos | Monitoreo de cambios / alineación | Medio |
| TSDF Fusion | Reconstrucción volumétrica densa | Escaneo 3D detallado | Alto |
| YOLO + Depth Fusion | Detección 3D de objetos | Monitoreo inteligente | Medio–Alto |
  
**Tabla 3 — Conceptos Técnicos Clave en ROS / Mapping 3D**  

| Concepto | Definición | Para Qué Sirve |
| ----------------- | ------------------------------------------------------------------------- | --------------------------------------- |
| Point Cloud | Conjunto de puntos 3D obtenidos por cámara/LiDAR | Representación geométrica del entorno |
| Occupancy Grid | Mapa discreto donde cada celda indica ocupación libre/ocupada | Navegación y planeación 2D |
| 3D Occupancy Grid | Extensión volumétrica de occupancy grid | Navegación y análisis espacial 3D |
| OctoMap | Estructura jerárquica octree para representar ocupación 3D probabilística | Mapas 3D eficientes en memoria |
| SLAM | Simultaneous Localization and Mapping | Localizar robot mientras construye mapa |
| Visual Odometry | Estimación de movimiento usando imágenes | Tracking de pose sin GPS |
| TF Tree | Árbol de transformaciones entre frames ROS | Coordinar sensores/robot/mapa |
| Voxel Grid | Discretización 3D del espacio en cubos volumétricos | Downsampling / representación espacial |
| Loop Closure | Corrección de drift al reconocer lugares visitados | Mejorar precisión global del mapa |
| ICP | Algoritmo de alineación de nubes de puntos | Registro / comparación temporal |
  
**Resumen breve de relación entre conceptos**  
```

Depth Camera
   ↓
Point Cloud
   ↓
Visual Odometry / SLAM
   ↓
Pose Estimation
   ↓
OctoMap / Occupancy Grid / TSDF
   ↓
Navigation / Monitoring / Inspection

```
  
  
  
3D Automated Optical Inspection (AOI) systems  
  
  
**3D AOI Methodology (Typical Workflow)**  

| Step | Process | Purpose |
| ------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------ |
| 1. Illumination / Projection | Project structured light, laser line, or fringe pattern onto object | Encode surface geometry into optical distortions |
| 2. Multi-view Image Capture | Cameras capture object from one or multiple angles | Acquire texture + distorted projected pattern |
| 3. 3D Reconstruction | Use triangulation / phase-shift / stereo algorithms | Recover height/depth map / point cloud |
| 4. Registration / Alignment | Align scan to CAD/reference/template | Normalize pose and coordinate frame |
| 5. Feature Extraction | Measure geometric/visual features | Height, volume, coplanarity, shape, texture |
| 6. Defect Detection / Classification | Rule-based or ML-based inspection | Detect anomalies / manufacturing defects |
| 7. Reporting / Feedback Loop | Generate pass/fail + analytics | Process control / QA traceability |
  
  
PCB on Conveyor  
      ↓  
3D Sensor Acquisition  
      ↓  
Calibration / Rectification  
      ↓  
3D Reconstruction  
      ↓  
Board Alignment  
      ↓  
ROI Extraction per Component  
      ↓  
Geometric Measurement  
      ↓  
Rule-Based / AI Defect Detection  
      ↓  
Pass / Fail + Defect Localization  
  
  
Instance segmentation is a computer vision task that combines object detection and semantic segmentation to identify, classify, and delineate the precise pixel-level boundaries of every individual object instance in an image.  
  
Semantic segmentation classifies every pixel in an image into categories (e.g., road, sky, car) but treats multiple objects of the same class as one group. Instance segmentation goes further by distinguishing and segmenting each individual object instance separately (e.g., identifying Car A, Car B, Car C)  
