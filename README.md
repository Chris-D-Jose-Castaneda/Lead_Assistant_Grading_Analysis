# 🎓 Lead Assistant Grading Analysis 📊

> End‑to‑end grading analysis & ETL pipeline with an interactive Streamlit dashboard for HADM 1740.

---

## 🚀 Live Demo
Try the interactive grading app here:  
👉 https://biz-comp.streamlit.app/

---

## 📂 Repository Structure

```text
Lead_Assistant_Grading_Analysis/
├── .devcontainer/                         
│   └── devcontainer.json                  🐳 VS Code & Codespaces container config  
├── data/                                  
│   └── …                                   📁 Place raw or additional CSV/JSON files  
├── HADM1740_All_Major_Assignments.csv     📊 Raw assignments & scores dataset  
├── Full_Schemas.sql                       🗄️ SQL DDL for `class_grades` database  
├── Analysis.ipynb                         📈 Jupyter notebook: EDA, cleaning, feature engineering  
├── ETL.ipynb                              🔄 Jupyter notebook: extract‑transform‑load pipeline  
├── app.py                                 🌐 Streamlit app entrypoint  
├── requirements.txt                       📦 Python dependencies  
└── README.md                              📝 This file  

---

##📄 File Details

    .devcontainer/devcontainer.json
    Container config (Python 3.11 + VS Code extensions).

    data/
    Folder for raw or intermediate datasets used by notebooks and the app.

    HADM1740_All_Major_Assignments.csv
    Master CSV of student submissions, due dates, and scores for HADM 1740.

    Full_Schemas.sql
    SQL script defining the class_grades database schema (tables, columns, indexes).

    ETL.ipynb
    • Reads raw CSV into pandas
    • Cleans, pivots, and transforms data
    • Loads processed data into SQL via SQLAlchemy

    Analysis.ipynb
    • Exploratory data analysis (month/day distributions, section comparisons)
    • Feature engineering (date parts, score metrics)
    • Visualizations: histograms, bar charts, clustering, PCA

    app.py
    • Streamlit application
    • Connects to SQL backend or CSV
    • Interactive filters, tables, and charts for grading insights

    requirements.txt
    Lists pinned versions for pandas, numpy, SQLAlchemy, streamlit, scikit‑learn, matplotlib, etc.\

---
## 🤝 Contributing

    Fork the repo & checkout a feature branch:

git checkout -b feat/YourFeature

Commit your changes:

git commit -m "Add awesome feature"

Push & open a Pull Request 🎉
