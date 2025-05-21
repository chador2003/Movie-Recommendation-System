# 🎬 Big Data Movie Recommendation System

An intelligent, scalable, and personalized movie recommendation system developed using Big Data technologies. This project integrates Apache Hadoop, Apache Spark, and K-Means clustering to suggest movies based on user preferences—tailored for modern streaming platforms struggling with content overload and decision fatigue.

> 🔍 Built to process 1 million+ movie records from TMDb with real-time insights using distributed frameworks.

---

## 📌 Table of Contents

- [✨ Features](#-features)
- [🎯 Objectives](#-objectives)
- [📚 Dataset](#-dataset)
- [🛠️ Tech Stack](#-tech-stack)
- [🏗️ Architecture Overview](#-architecture-overview)
- [🔎 Data Insights](#-data-insights)
- [🧠 Model & Evaluation](#-model--evaluation)
- [🚀 How to Use](#-how-to-use)
- [📈 Business & User Impact](#-business--user-impact)
- [📚 References](#-references)
- [👥 Contributors](#-contributors)

---

## ✨ Features

✅ Recommends movies based on content similarity  
✅ Scales to millions of records using Hadoop HDFS  
✅ Supports real-time search and interaction via Streamlit UI  
✅ Uses Spark NLP for text cleaning, lemmatization, and vectorization  
✅ Clusters similar movies using K-Means  
✅ Delivers fast, relevant, personalized recommendations

---

## 🎯 Objectives

- Develop a **content-based filtering** movie recommendation engine.
- Apply **Big Data tools** (Hadoop + Spark) for handling large-scale datasets.
- Integrate **NLP** and **TF-IDF** for semantic vectorization.
- Cluster similar movies for efficient querying and recommendation.

---

## 📚 Dataset

- 📦 [TMDB Movies Dataset (1M+ titles)](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies/data)
- Features include:
  - Titles, genres, keywords, overviews, ratings, release dates
  - Rich metadata ideal for building hybrid and content-based models

---

## 🛠️ Tech Stack

| Layer             | Technologies                                   |
|------------------|-------------------------------------------------|
| **Big Data**      | Apache Hadoop, HDFS, MapReduce                 |
| **Processing**    | Apache Spark, PySpark                          |
| **NLP & ML**      | TF-IDF, Lemmatization, Stopword Removal        |
| **Clustering**    | K-Means Algorithm                              |
| **Frontend**      | Streamlit UI for real-time interaction         |
| **Evaluation**    | Silhouette Score                               |
| **Storage**       | HDFS (distributed) + Local for app deployment  |

---

## 🏗️ Architecture Overview

1. **Data Ingestion**: Load TMDB dataset into HDFS
2. **Preprocessing (MapReduce & Spark)**:
   - Column filtering, null removal, text normalization
   - Feature generation from genres, tags, keywords, overview
3. **TF-IDF Vectorization**: Convert textual data into weighted vectors
4. **K-Means Clustering**: Group similar movies based on semantic features
5. **Recommendation Engine**: Match user-selected movie with its cluster
6. **Streamlit Integration**: Search & display recommendations interactively

---

## 🔎 Data Insights

📊 **Genre Distribution**: Drama, Comedy, and Thriller dominate  
📈 **Production Trends**: Spike in global releases post-1980  
💸 **Budget vs Revenue**: Higher budgets correlate with greater returns  
🎨 **Top Studios**: Warner Bros., Columbia, Paramount lead the industry  
🔥 **Popularity vs Rating vs Revenue**: Strong patterns in user preference

---

## 🧠 Model & Evaluation

### 🔍 Model: K-Means Clustering
- Based on TF-IDF features
- Grouping movies by semantic content

### ✅ Evaluation: Silhouette Score
- **Score: 0.826** → Strong clustering and high recommendation confidence

---
