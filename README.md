📄 File Overview

    .devcontainer/devcontainer.json
    Container spec (Python 3.11 + VS Code extensions)

    data/
    Folder for raw/intermediate datasets

    HADM1740_All_Major_Assignments.csv
    Master assignments & scores CSV

    Full_Schemas.sql
    DDL to create all grading tables

    Analysis.ipynb
    • Load & parse raw data
    • Feature engineering (dates, sections)
    • EDA: counts, charts, clustering, PCA

    ETL.ipynb
    • Read/clean CSV in pandas
    • Pivot, transform, load into SQL via SQLAlchemy

    app.py
    • Streamlit UI
    • Connects to SQL or CSV
    • Interactive filters, tables & charts

    requirements.txt
    Lists versions for pandas, numpy, SQLAlchemy, scikit‑learn, streamlit, matplotlib, etc.

🤝 Contributing

    Fork & branch (git checkout -b feat/YourFeature)

    Commit (git commit -m "Add awesome feature").

    Push & open PR. 🎉

✉️ Contact

Chris José Castaneda
chris.jose.castaneda@gmail.com
Feel free to open issues or suggestions!
