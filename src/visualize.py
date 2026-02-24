import pandas as pd
import matplotlib.pyplot as plt

def create_viz():
    df = pd.read_csv("data/raw/vehicle_registrations.csv")
    df['FUEL'].value_counts().plot(kind='bar', title='Розподіл за типом палива')
    plt.tight_layout()
    plt.savefig("reports/figures/fuel_distribution.png")
    print("Графік збережено в reports/figures/")

if __name__ == "__main__":
    create_viz()