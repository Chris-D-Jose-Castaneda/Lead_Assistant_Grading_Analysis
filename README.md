# 🏡 SWFL Real Estate Home Buying Advisor (SWFL) 🏖️

> A comprehensive analytics suite to help prospective buyers navigate Southwest Florida’s housing markets.  
> Combines automated data collection, rigorous modeling, and an interactive R Shiny dashboard for actionable insights.

---

### 🎯 Project Scope

This repository implements the full workflow—from scraping detailed property listings on Realtor.com, geocoding addresses, and building an ETL pipeline, to integrating macroeconomic indicators (county HPIs, mortgage rates) and applying advanced statistical & machine learning models. Finally, an R Shiny app delivers interactive maps, trend visualizations, forecast scenarios, and affordability calculators to guide homebuyers in a dynamic market.

---

### 📁 File Descriptions

1. **`updated_mls_scraper.py`**  
   Selenium‑based scraper that collects listing details (price, beds, baths, sqft, etc.) from Realtor.com.  
   Outputs raw data to `Raw_SWFL_Data.csv`.

2. **`Zipcode.py`**  
   Normalizes & geocodes addresses via Geopy’s Nominatim with U.S. Census API fallback.  
   Writes results to `Final_SWFL_With_Fallback_Coords.csv`.

3. **`Data Cleaning.ipynb`**  
   ETL pipeline: ingests raw CSVs, sanitizes fields, engineers features (ppsf, age, etc.), handles outliers, and merges economic series.  
   Exports cleaned dataset as `SWFL_Data_Cleaned_Final_Version.csv`.

4. **`Economic_Parameters.ipynb`**  
   Fetches & processes macro time series—30‑year fixed mortgage rates (`MORTGAGE30US.csv`), SPY/DJIA, and county HPIs (`Collier_County_Price_Index.csv`, `Lee_County_Price_Index.csv`)—and visualizes historical trends.

5. **`Modeling.ipynb`**  
   Explores predictive approaches: OLS with interactions, Ridge/Lasso, ARIMA forecasts, Random Forest, XGBoost.  
   Benchmarks models (R², RMSE) and produces diagnostic plots.

6. **`app.R`**  
   R Shiny dashboard: interactive map of listings, market trend charts, short‑term forecasts, and an affordability simulator.

7. **`Raw_SWFL_Data.csv`**  
   Raw, unprocessed output from the MLS scraper—full original fields for transparency & debugging.

8. **`Final_SWFL_With_Fallback_Coords.csv`**  
   Intermediate dataset after geocoding, including latitude & longitude for each listing.

9. **`SWFL_Data_Cleaned_Final_Version.csv`**  
   Final feature‑engineered dataset used by analysis notebooks and the Shiny app—outliers handled, economic data merged.

---

### 📄 Report

See the full write‑up in  
**`SouthWest Florida Quantitative Analysis of Urban Housing Markets.pdf`**  
for methodology, challenges, and detailed results.

---

### 🌐 Live Dashboard

Explore the published R Shiny app here:  
👉 https://chris-jose-castaneda.shinyapps.io/SWFL_Quant_Analysis/

---

### ⭐ Contribute & Star

Feel free to fork, adapt, or build upon this repository for your own data science projects.  
If you find it useful, don’t forget to ⭐ it!

Best,  
**Chris José Castaneda**  
