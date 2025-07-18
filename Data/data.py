import pandas as pd
import numpy as np
import os

class Read_data():
    def __init__(self):
        data_dir = os.path.dirname(os.path.abspath(__file__))
        self.past_csv_path = os.path.join(data_dir, 'NEO_close.csv')
        self.future_csv_path = os.path.join(data_dir, 'NEO_close_future.csv')

        self.load_data(past = True, all_data = False)

    def load_data(self, past, all_data):
        if past == True and all_data == False:
            self.df = pd.read_csv(self.past_csv_path)

            year_bin = np.arange(1890, 2031, 10)
        elif past == False and all_data == False:
            self.df = pd.read_csv(self.future_csv_path)

            year_bin = np.arange(2020, 2201, 10)
        elif past == False and all_data == True:
            df1 = pd.read_csv(self.past_csv_path)
            df2 = pd.read_csv(self.future_csv_path)

            self.df = pd.concat([df1, df2], ignore_index=True)

            year_bin = np.arange(1890, 2201, 10)
        
        self.year_label = [f"{start}-{start+10}" for start in year_bin[:-1]]

        self.df.pop('V infinity(km/s)')

        distance_bin = np.array([0, 0.01, 0.05, 0.3, 1.0, 5.0, 10.0])
        self.distnace_label = [
    "Extremely Close (<0.01 LD)",
    "Very Close (0.01–0.05 LD)",
    "Close (0.05–0.3 LD)",
    "Near Moon (0.3–1.0 LD)",
    "Medium Range (1–5 LD)",
    "Distant (5–10 LD)"
]

        self.df['Distance Group'] = pd.cut(self.df['CA DistanceNominal (LD)'], bins=distance_bin, labels=self.distnace_label, right=False)

        self.df['Distance Group Close'] = pd.cut(self.df['CA DistanceMinimum (LD)'], bins=distance_bin, labels=self.distnace_label, right=False)

        self.df["Year"] = pd.to_numeric(self.df['Close-Approach (CA) Date'].str[:4])

        self.df['Year Group'] = pd.cut(self.df['Year'], bins=year_bin, labels=self.year_label, right=True)

        magnitude_bin = np.array([0, 14, 17, 22, 25, 30, float('inf')])
        self.magnitude_label = [
    "Extremely Bright (<14)",
    "Very Bright (14–17)",
    "Moderately Bright (17–22)",
    "Faint (22–25)",
    "Very Faint (25–30)",
    "Nearly Invisible (>30)"
]
        
        self.df['Magnitude'] = pd.cut(self.df['H(mag)'], bins=magnitude_bin, labels=self.magnitude_label, right=False)

        diameter_bin = np.array([0, 10, 25, 140, 300, 1000, 10000, float('inf')])
        self.diameter_labels = [
    "Tiny (<10 m)",
    "Very Small (10–25 m)",
    "Small (25–140 m)",
    "Medium (140–300 m)",
    "Large (300–1000 m)",
    "Massive (1-10 km)",
    'Extinction Level Size (>10 km)'
]

        # Look into fixing the parsing. Current version doesn't handle decimals well
        def parse_diameter(diam_str):
            if pd.isna(diam_str):
                return np.nan
            
            diam_str = diam_str.replace(" ", "")
            
            if "±" in diam_str:
                diam_str = diam_str.split("±")[0]
            
            if "–" in diam_str:
                parts = diam_str.split("–")
            elif "-" in diam_str:
                parts = diam_str.split("-")
            else:
                parts = [diam_str]
            
            numbers = []
            for part in parts:
                part = part.replace("km", "").replace("m", "")
                try:
                    numbers.append(float(part))
                except:
                    continue
            
            if not numbers:
                return np.nan
            
            avg_val = np.mean(numbers)
            
            if 'km' in diam_str:
                avg_val *= 1000
            
            return avg_val
        
        self.df['Average Diameter'] = self.df['Diameter'].apply(parse_diameter)

        self.df['Diameter Group'] = pd.cut(self.df['Average Diameter'], bins=diameter_bin, labels=self.diameter_labels, right=False)

        rarity_bin = np.array([0, 1, 2, 3, 4, 5, float('inf')])
        self.rarity_label = ["Very Common", "Common", "Uncommon", "Rare", "Very Rare", "Extremely Rare"]
        
        self.df["Rarity Group"] = pd.cut(self.df["Rarity"], bins=rarity_bin, labels=self.rarity_label, right=False)

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

        self.df['Velocity Group'] = pd.cut(self.df['V relative(km/s)'], bins=velocity_bin, labels=self.velocity_labels, right=False)

        scoring = {
            "Extremely Close (<0.01 LD)": 5,
            "Very Close (0.01–0.05 LD)": 4,
            "Close (0.05–0.3 LD)": 3,
            "Near Moon (0.3–1.0 LD)": 2,
            "Medium Range (1–5 LD)": 1,
            "Distant (5–10 LD)": 0,
            "Extremely Bright (<14)": 5,
            "Very Bright (14–17)": 4,
            "Moderately Bright (17–22)": 3,
            "Faint (22–25)": 2,
            "Very Faint (25–30)": 1,
            "Nearly Invisible (>30)": 0,
            "Tiny (<10 m)": 0,
            "Very Small (10–25 m)": 1,
            "Small (25–140 m)": 2,
            "Medium (140–300 m)": 3,
            "Large (300–1000 m)": 4,
            "Massive (1-10 km)": 5,
            'Extinction Event (>10 km)': 6,
            'Crawling (0-5 km/s)': 0,
            'Slow Approach (5-10 km/s)': 1,
            'Moderate Speed (10-15 km/s)': 2,
            'Typical NEO Speed (15-20 km/s)': 3,
            'Fast Mover (20-30 km/s)': 4,
            'Hypervelocity (30-40 km/s)': 5,
            'Extreme Velocity (>40 km/s)': 6
            
        }
        
        score_columns = ["Distance Group", "Velocity Group", "Magnitude", "Diameter Group"]

        for column in score_columns:
            self.df[column + 'points'] = self.df[column].map(scoring)

        self.df['Total Score'] = self.df[[column + 'points' for column in score_columns]].sum(axis=1)

        score_bin = np.array([0, 5, 10, 15, 20, 22])
        self.score_label = [
            'No Concern',
            'Scientific Interest',
            'Moderate Concern',
            'Serious Concern',
            'Extinction Event'
            ]

        self.df['Score Group'] = pd.cut(self.df['Total Score'], bins=score_bin, labels=self.score_label, right=False)

        self.dataframe()
        self.count()
        return self.df
    
    def count(self):
        self.group_type = ['CA DistanceNominal (LD)', 'CA DistanceMinimum (LD)', 'Year',
                           'H(mag)', 'Average Diameter', 'V relative(km/s)',
                           'Rarity', 'Total Score']
        
        self.label_count = {}

        self.summary_stats()
        return self.summary_df

    def summary_stats(self):
        for label in self.group_type:
            self.label_count[label] = self.df[label].sum()

        self.min_val = {label: np.min(self.df[label]) for label in self.group_type}
        self.max_val = {label: np.max(self.df[label]) for label in self.group_type}
        self.averg_val = {label: np.nanmean(pd.to_numeric(self.df[label])) for label in self.group_type}
        self.median_val = {label: np.median(pd.to_numeric(self.df[label]).dropna()) for label in self.group_type}

        d = {
            'Minimum Value': [self.min_val[label] for label in self.group_type],
            'Mean Value': [self.averg_val[label] for label in self.group_type],
            'Max Value': [self.max_val[label] for label in self.group_type],
            'Median Value': [self.median_val[label] for label in self.group_type]
            }

        self.summary_df = pd.DataFrame(data=d, index=['Distance (LD)', 'Closest Distance (LD)', 'Year', 'Magnitude (H)', 'Diameter (m)',
                                                      'Velocity (km/s)', 'Rarity', 'Concern Score'])

        return self.summary_df
    
    def dataframe(self):
        return self.df
    
# start = Read_data()
# startt = start.load_data(past=False, all_data=False)