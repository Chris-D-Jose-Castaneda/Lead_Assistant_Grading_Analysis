## 🛠️ Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Chris-D-Jose-Castaneda/Lead_Assistant_Grading_Analysis.git
   cd Lead_Assistant_Grading_Analysis

# Lead_Assistant_Grading_Analysis
Maintain classes

Grading App for students enrolled int the course: https://biz-comp.streamlit.app/

📄 File Details

    .devcontainer/devcontainer.json
    Container definition for a reproducible dev environment (Python 3.11 + VS Code).

    data/
    Place raw or intermediate files here (CSV, JSON, etc.) for notebooks and app.

    HADM1740_All_Major_Assignments.csv
    Original dataset with student scores and due dates for HADM 1740.

    Full_Schemas.sql
    SQL script to create class_grades database schema: tables for Fall/Spring terms, grading data, etc.

    Analysis.ipynb

        Loading & parsing CSV

        Date/time feature engineering

        Basic EDA (counts by month, day of week, section)

        Histograms & bar charts

        Advanced analyses: PCA, clustering, logistic regression

    ETL.ipynb

        Read raw CSV into pandas

        Clean & pivot data

        Write to SQL (SQLite/MySQL) via SQLAlchemy

    app.py

        Streamlit interface

        Connects to SQL backend or reads CSV

        Interactive filters, tables, charts, export options

    requirements.txt
    Pinning versions for pandas, numpy, SQLAlchemy, streamlit, scikit‑learn, matplotlib, seaborn, etc.

    🤝 Contributing

    Fork the repo

    Create a feature branch (git checkout -b feat/YourFeature)

    Commit your changes (git commit -m "Add awesome feature")

    Push to branch (git push origin feat/YourFeature)

    Open a Pull Request

📫 Contact

Chris José Castaneda — chris.jose.castaneda@gmail.com
Feel free to open an issue or drop me a line with suggestions!
