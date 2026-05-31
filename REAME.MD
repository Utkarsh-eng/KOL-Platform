# KOL AI Analysis System

## Overview

This project is an AI-powered Key Opinion Leader (KOL) analysis system that extracts researcher information from multiple public sources, generates semantic researcher profiles, computes similarity scores using embeddings, ranks researchers based on influence metrics, clusters similar researchers, and generates AI-powered insights using Gemini.

The project was developed as part of a KOL capability evaluation assignment.

---

## Objectives

* Extract structured information from multiple public researcher sources.
* Build enriched researcher profiles.
* Generate semantic embeddings for researchers.
* Measure researcher similarity using cosine similarity.
* Calculate influence scores using academic metrics.
* Cluster researchers using unsupervised learning.
* Generate natural language insights using an LLM.
* Visualize results through an interactive Streamlit dashboard.

---

## Researchers Analyzed

1. Andrew Ng
2. Fei-Fei Li
3. Yann LeCun

---

## Data Sources

### Google Scholar

Used for extracting:

* Name
* Affiliation
* Research Interests
* Citations
* H-index
* i10-index
* Publications

### PubMed

Used for extracting:

* Research paper titles
* Abstracts
* Authors

PubMed abstracts were incorporated to enrich semantic researcher profiles with detailed research language and domain-specific context.

---

## System Architecture

Google Scholar + PubMed

↓

Structured Researcher Profiles

↓

Profile Text Generation

↓

SentenceTransformer Embeddings

↓

Cosine Similarity Analysis

↓

Influence Scoring

↓

KMeans Clustering

↓

Gemini LLM Summary Generation

↓

Streamlit Dashboard

---

## Project Structure

```text
kol-ai-project/
│
├── data/
│   ├── raw/
│   │   ├── scholar/
│   │   └── pubmed/
│
├── outputs/
│   ├── kol_profiles.json
│   ├── similarity_matrix.csv
│   ├── influence_scores.csv
│   ├── similarity_heatmap.png
│   └── llm_summary.txt
│
├── src/
│   ├── extract_scholar.py
│   ├── extract_pubmed.py
│   ├── preprocess.py
│   ├── embeddings.py
│   ├── similarity.py
│   ├── scoring.py
│   ├── clustering.py
│   └── summarizer.py
│
├── app.py
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Multi-Source Data Extraction

Researcher information was extracted from:

* Google Scholar
* PubMed

The extracted information was merged into a unified researcher profile.

---

### 2. Semantic Profile Construction

A textual profile was generated using:

* Research interests
* Publication information
* Abstract information

This profile serves as the semantic representation of each researcher.

---

### 3. Embedding Generation

Sentence embeddings were generated using SentenceTransformers.

These embeddings capture semantic meaning and allow similarity computation beyond keyword matching.

---

### 4. Similarity Analysis

Cosine similarity was used to compare researcher embeddings.

Cosine similarity measures semantic closeness between researchers in vector space.

Higher values indicate greater research similarity.

---

### 5. Influence Scoring

An influence score was computed using:

* Citation count
* H-index
* Publication count

A weighted scoring strategy was used to estimate academic influence.

---

### 6. Clustering

KMeans clustering was applied to researcher embeddings to identify naturally occurring groups of similar researchers.

This demonstrates unsupervised learning on semantic researcher representations.

---

### 7. LLM-Based Analysis

Gemini was used to generate:

* Researcher summaries
* Similarity explanations
* Key differences
* Final comparative insights

This converts quantitative outputs into human-readable business insights.

---

## Results

The system successfully generated:

* Structured researcher profiles
* Semantic similarity matrix
* Influence ranking
* Researcher clusters
* AI-generated analytical summaries

---

## Technologies Used

### Python

* Requests
* BeautifulSoup
* Pandas
* NumPy

### NLP & ML

* SentenceTransformers
* Scikit-learn
* Cosine Similarity
* KMeans Clustering

### LLM

* Google Gemini API

### Visualization

* Matplotlib
* Seaborn

### Dashboard

* Streamlit

---

## Future Improvements

* Automatic web scraping pipeline
* Additional academic data sources
* Research topic classification
* Network graph visualization
* Advanced influence scoring
* Real-time researcher discovery
* RAG-based researcher querying

---

## Conclusion

This project demonstrates an end-to-end AI pipeline for KOL analysis, combining information extraction, semantic embeddings, similarity analysis, influence scoring, clustering, and LLM-powered insight generation. The resulting system provides both quantitative and qualitative evaluation of researchers and can serve as a foundation for larger talent intelligence, expert discovery, and academic analytics platforms.
