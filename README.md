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
