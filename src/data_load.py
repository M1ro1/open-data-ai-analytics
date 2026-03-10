import pandas as pd
import os


def download_data():
    url = "./data/sample/sample_data.csv"
    output_path = "data/sample/vehicle_registrations.csv"
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