# PremierLeagueStanding_ETL
A clean, production-style ETL pipeline that extracts live Premier League standings from the football-data.org API, transforms the data into a structured format, and loads it into a CSV file ready for SQL analysis

📌 Overview

This project demonstrates a real-world Data Engineering ETL workflow using Python.
It showcases:
API data extraction
Data cleaning and transformation
CSV storage for downstream analytics
Modular pipeline architecture
Separation of concerns (Extract → Transform → Load)

🚀 Features
✓ Extract
Fetches live Premier League standings with authenticated API requests from football-data.org.

✓ Transform
Cleans and reshapes JSON data into a properly structured Pandas DataFrame including:
Position, Team, Played games, Wins, draws, losses, Goals for / against, Goal difference, Points

✓ Load
Outputs a clean, analysis-ready CSV file:
output/PLStanding.csv
Perfect for loading into:
MySQL Workbench
PostgreSQL
Excel or BI tools (Power BI, Tableau)

🔧 Installation & Setup
1. Clone the repo
   git clone https://github.com/femigab100/PremierLeagueStanding_ETL.git
   cd Football_Data_ETL

2. Install dependencies
pip install -r requirements.txt

3. Add your API key.
   Open config and replace: API_TOKEN = "YOUR_API_TOKEN"
   
5. Execute the pipeline
   python pipeline.py

Output:
Extracts live standings
Transforms JSON → DataFrame
Saves CSV to output/PLStanding.csv

🛠️ Tech Stack
Python
Pandas
Requests
Football-Data API
CSV / SQL

📚 Learning Outcomes
This project helps you practice real Data Engineering concepts:
API integration
Modular architecture
ETL Pipeline
Building a production-ready folder structure

🤝 Contributions
Feel free to fork, open issues, or submit pull requests.

⭐ Support
If this project helped you, give the repo a star ⭐
It motivates and supports ongoing improvements.
