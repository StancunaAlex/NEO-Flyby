import pandas as pd
import numpy as np
import os

class Read_data():
    def __init__(self):
        data_dir = os.path.dirname(os.path.abspath(__file__))
        self.csv_path = os.path.join(data_dir, 'NEO_close.csv')

    def load_data(self):
        df = pd.read_csv(self.csv_path)

        df.pop('V infinity(km/s)')

        distance_bin = np.array([0, 0.01, 0.05, 0.3, 1.0, 5.0, 10.0])
        distnace_label = [
    "Extremely Close (<0.01 LD)",
    "Very Close (0.01–0.05 LD)",
    "Close (0.05–0.3 LD)",
    "Near Moon (0.3–1.0 LD)",
    "Medium Range (1–5 LD)",
    "Distant (5–10 LD)"
]

        df['Distance Group'] = pd.cut(df['CA DistanceNominal (LD)'], bins=distance_bin, labels=distnace_label, right=False)

        df['Distance Group Close'] = pd.cut(df['CA DistanceMinimum (LD)'], bins=distance_bin, labels=distnace_label, right=False)

        df["Year"] = pd.to_numeric(df['Close-Approach (CA) Date'].str[:4])

        year_bin = np.array([1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030])
        year_label = ['1890-1900', '1900-1910', '1910-1920', '1920-1930', '1930-1940', '1940-1950', '1950-1960', '1960-1970',
                       '1970-1980', '1980-1990', '1990-2000', '2000-2010', '2010-2020', '2020-2030']

        df['Year Group'] = pd.cut(df['Year'], bins=year_bin, labels=year_label, right=False)

        magnitude_bin = np.array([0, 14, 17, 22, 25, 30, float('inf')])
        magnitude_label = [
    "Extremely Bright (<14)",
    "Very Bright (14–17)",
    "Moderately Bright (17–22)",
    "Faint (22–25)",
    "Very Faint (25–30)",
    "Nearly Invisible (>30)"
]
        
        df['Magnitude'] = pd.cut(df['H(mag)'], bins=magnitude_bin, labels=magnitude_label, right=False)

        diameter_bin = np.array([0, 10, 25, 140, 300, 1000, float('inf')])
        diameter_labels = [
    "Tiny (<10 m)",
    "Very Small (10–25 m)",
    "Small (25–140 m)",
    "Medium (140–300 m)",
    "Large (300–1000 m)",
    "Massive (>1 km)"
]

        df['Diameter'] = (
            df['Diameter']
            .str.replace('km', '000 m', regex=False)
            .str.extractall(r'(\d+\.?\d*)')
            .unstack()
            .astype(float)
            .mean(axis=1)
        )

        df['Diameter Group'] = pd.cut(df['Diameter'], bins=diameter_bin, labels=diameter_labels, right=False)

        rarity_bin = np.array([0, 1, 2, 3, 4, 5, float('inf')])
        rarity_label = ["Very Common", "Common", "Uncommon", "Rare", "Very Rare", "Extremely Rare"]
        
        df["Rarity Group"] = pd.cut(df["Rarity"], bins=rarity_bin, labels=rarity_label, right=False)

        return df