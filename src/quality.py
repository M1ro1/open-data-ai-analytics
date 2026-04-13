import pandas as pd
from sqlalchemy import create_engine
import os

def check_quality():
    engine = create_engine("sqlite:////app/db/database.db")
    df = pd.read_sql("SELECT * FROM vehicles", engine)

    report = "--- ПЕРЕВІРКА ЯКОСТІ ДАНИХ ---\n\n"
    report += f"Порожні значення:\n{df.isnull().sum()}\n\n"
    report += f"Дублікати: {df.duplicated().sum()}\n\n"
    report += f"Типи колонок:\n{df.dtypes}\n"

    os.makedirs("/app/reports", exist_ok=True)
    with open("/app/reports/quality_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("Звіт з якості збережено.")

if __name__ == "__main__":
    check_quality()
