import pandas as pd
from sqlalchemy import create_engine
import os

def load_data():
    input_path = "/app/data/sample/sample_data.csv"
    db_path = "sqlite:////app/db/database.db"

    print(f"Починаю завантаження даних з {input_path}...")
    try:
        df = pd.read_csv(input_path, sep=';', encoding='utf-8', low_memory=False)
        os.makedirs("/app/db", exist_ok=True)
        
        engine = create_engine(db_path)
        df.to_sql('vehicles', engine, if_exists='replace', index=False)
        
        print(f"Дані успішно збережено у БД! Завантажено рядків: {len(df)}")
    except Exception as e:
        print(f"Помилка при завантаженні: {e}")

if __name__ == "__main__":
    load_data()
