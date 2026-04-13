import pandas as pd
from sqlalchemy import create_engine
import os
import json

def research_data():
    engine = create_engine("sqlite:////app/db/database.db")
    df = pd.read_sql("SELECT * FROM vehicles", engine)

    stats = {"total_records": len(df)}
    if 'BRAND' in df.columns:
        stats["top_5_brands"] = df['BRAND'].value_counts().head(5).to_dict()

    os.makedirs("/app/reports", exist_ok=True)
    with open("/app/reports/research_report.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)
    print("Звіт з дослідження збережено.")

if __name__ == "__main__":
    research_data()
