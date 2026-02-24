import pandas as pd
import requests
import os


def download_data():
    url = "https://data.gov.ua/dataset/06779371-308f-42d7-895e-5a39833375f0/resource/3f13166f-090b-499e-8e23-e9851c5a5f67/download/tz_opendata_z01012024_01022024.csv"

    output_path = "data/raw/vehicle_registrations.csv"

    print(f"Починаю завантаження даних з {url}...")

    try:
        df = pd.read_csv(url, sep=';', encoding='utf-8', low_memory=False)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        df.to_csv(output_path, index=False)
        print(f"Дані успішно збережено у {output_path}")
        print(f"Завантажено рядків: {len(df)}")

        print("\nПерші 5 рядків даних:")
        print(df.head())

    except Exception as e:
        print(f"Помилка при завантаженні: {e}")


if __name__ == "__main__":
    download_data()
