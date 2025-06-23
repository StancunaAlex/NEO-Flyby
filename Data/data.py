import pandas as pd
import numpy as np
import os

class Read_data():
    def __init__(self):
        data_dir = os.path.dirname(os.path.abspath(__file__))
        self.past_csv_path = os.path.join(data_dir, 'NEO_close.csv')
        self.future_csv_path = os.path.join(data_dir, 'NEO_close_future.csv')

    def load_data(self, past):
        if past == True:
            df = pd.read_csv(self.past_csv_path)

            year_bin = np.arange(1890, 2031, 10)
            self.year_label = [f"{start}-{start+10}" for start in year_bin[:-1]]
        else:
            df = pd.read_csv(self.future_csv_path)

            year_bin = np.arange(2020, 2200, 10)
            self.year_label = [f"{start}-{start+10}" for start in year_bin[:-1]]

        df.pop('V infinity(km/s)')

        distance_bin = np.array([0, 0.01, 0.05, 0.3, 1.0, 5.0, 10.0])
        self.distnace_label = [
    "Extremely Close (<0.01 LD)",
    "Very Close (0.01–0.05 LD)",
    "Close (0.05–0.3 LD)",
    "Near Moon (0.3–1.0 LD)",
    "Medium Range (1–5 LD)",
    "Distant (5–10 LD)"
]

        df['Distance Group'] = pd.cut(df['CA DistanceNominal (LD)'], bins=distance_bin, labels=self.distnace_label, right=False)

        df['Distance Group Close'] = pd.cut(df['CA DistanceMinimum (LD)'], bins=distance_bin, labels=self.distnace_label, right=False)

        df["Year"] = pd.to_numeric(df['Close-Approach (CA) Date'].str[:4])

        df['Year Group'] = pd.cut(df['Year'], bins=year_bin, labels=self.year_label, right=False)

        magnitude_bin = np.array([0, 14, 17, 22, 25, 30, float('inf')])
        self.magnitude_label = [
    "Extremely Bright (<14)",
    "Very Bright (14–17)",
    "Moderately Bright (17–22)",
    "Faint (22–25)",
    "Very Faint (25–30)",
    "Nearly Invisible (>30)"
]
        
        df['Magnitude'] = pd.cut(df['H(mag)'], bins=magnitude_bin, labels=self.magnitude_label, right=False)

        diameter_bin = np.array([0, 10, 25, 140, 300, 1000, 10000, float('inf')])
        self.diameter_labels = [
    "Tiny (<10 m)",
    "Very Small (10–25 m)",
    "Small (25–140 m)",
    "Medium (140–300 m)",
    "Large (300–1000 m)",
    "Massive (1-10 km)",
    'Extinction Event (>10 km)'
]

        df['Diameter'] = (
            df['Diameter']
            .str.replace('km', '000 m', regex=False)
            .str.extractall(r'(\d+\.?\d*)')
            .unstack()
            .astype(float)
            .mean(axis=1)
        )

        df['Diameter Group'] = pd.cut(df['Diameter'], bins=diameter_bin, labels=self.diameter_labels, right=False)

        rarity_bin = np.array([0, 1, 2, 3, 4, 5, float('inf')])
        self.rarity_label = ["Very Common", "Common", "Uncommon", "Rare", "Very Rare", "Extremely Rare"]
        
        df["Rarity Group"] = pd.cut(df["Rarity"], bins=rarity_bin, labels=self.rarity_label, right=False)

        velocity_bin = np.array([0, 5, 10, 15, 20, 30, 40, float('inf')])
        self.velocity_labels = [
            'Crawling (0-5 km/s)',
            'Slow Approach (5-10 km/s)',
            'Moderate Speed (10-15 km/s)',
            'Typical NEO Speed (15-20 km/s)',
            'Fast Mover (20-30 km/s)',
            'Hypervelocity (30-40 km/s)',
            'Extreme Velocity (>40 km/s)'
        ]

        df['Velocity Group'] = pd.cut(df['V relative(km/s)'], bins=velocity_bin, labels=self.velocity_labels, right=False)

        return df