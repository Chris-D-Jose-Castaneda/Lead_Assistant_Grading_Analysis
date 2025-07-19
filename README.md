# 🎓 Lead Assistant Grading Analysis 📊

> End‑to‑end grading analysis & ETL pipeline with an interactive Streamlit dashboard for course code 1740. This was useful for my other assistants in changing student learning.

---

## 🚀 Live Demo  
Try the interactive grading app here:  
👉 https://biz-comp.streamlit.app/

---

## 🔖 Table of Contents
- [✨ Features](#-features)  
- [🛠️ Tech Stack](#️-tech-stack)  
- [📂 Repository Structure](#-repository-structure)  
- [⚙️ Getting Started](#️-getting-started)  
- [🔧 Configuration](#-configuration)  
- [📊 Usage](#-usage)  
- [🗄️ Database Schema](#️-database-schema)  
- [🤝 Contributing](#-contributing)  
- [📄 License](#-license)  
- [✉️ Contact](#️-contact)  

---

## ✨ Features
- **Automated ETL Pipeline**  
  – Ingest raw assignment CSV, clean & transform, load into SQL  
- **Exploratory Data Analysis**  
  – Jupyter notebooks for EDA, feature engineering, visualizations  
- **Interactive Dashboard**  
  – Streamlit app with filters, tables, and charts to explore grades  
- **Extensible Architecture**  
  – Easily swap CSV for database, add new metrics or visualizations  

---

## 🛠️ Tech Stack
- **Language & Notebooks:** Python 3.11, Jupyter  
- **Data & Modeling:** pandas, NumPy, scikit‑learn  
- **Database:** SQLAlchemy (SQLite/MySQL)  
- **Visualization:** matplotlib, seaborn, Streamlit  
- **Dev Environment:** VS Code DevContainer (Docker)  

---

## 📂 Repository Structure

```text
Lead_Assistant_Grading_Analysis/
├── .devcontainer/                         
│   └── devcontainer.json                  🐳 DevContainer config (Python, VS Code)  
├── data/                                  
│   └── …                                   📁 Raw or additional CSV/JSON files  
├── HADM1740_All_Major_Assignments.csv     📊 Raw assignments & scores dataset  
├── Full_Schemas.sql                       🗄️ SQL DDL for `class_grades` database  
├── ETL.ipynb                              🔄 ETL pipeline: ingest → clean → load  
├── Analysis.ipynb                         📈 EDA & feature engineering notebooks  
├── app.py                                 🌐 Streamlit app entrypoint  
├── requirements.txt                       📦 Python dependencies  
└── README.md                              📝 This document  
