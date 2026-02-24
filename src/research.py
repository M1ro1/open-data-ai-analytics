import pandas as pd

def research_data():
    df = pd.read_csv("data/raw/vehicle_registrations.csv")
    print("--- ДОСЛІДЖЕННЯ ДАНИХ ---")
    top_brands = df['BRAND'].value_counts().head(5)
    print(f"Топ марок:\n{top_brands}")

if __name__ == "__main__":
    research_data()