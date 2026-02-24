import pandas as pd

def check_quality():
    df = pd.read_csv("data/raw/vehicle_registrations.csv")
    print("--- ПЕРЕВІРКА ЯКОСТІ ДАНИХ ---")
    print(f"Порожні значення:\n{df.isnull().sum()}")
    print(f"Дублікати: {df.duplicated().sum()}")
    print(f"Типи колонок:\n{df.dtypes}")

if __name__ == "__main__":
    check_quality()