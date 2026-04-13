import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

def create_viz():
    engine = create_engine("sqlite:////app/db/database.db")
    df = pd.read_sql("SELECT * FROM vehicles", engine)

    os.makedirs('/app/reports/figures', exist_ok=True)

    if 'FUEL' in df.columns:
        df['FUEL'].value_counts().plot(kind='bar', title='Розподіл за типом палива')
        plt.tight_layout()
        plt.savefig("/app/reports/figures/fuel_distribution.png")
        plt.close()

    if 'BRAND' in df.columns:
        df['BRAND'].value_counts().head(10).plot(kind='pie', title='Топ 10 марок')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig("/app/reports/figures/top_brands.png")
        plt.close()
        
    print("Графіки збережено.")

if __name__ == "__main__":
    create_viz()
