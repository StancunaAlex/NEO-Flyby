import pandas as pd
import os

class Read_data():
    def __init__(self):
        data_dir = os.path.dirname(os.path.abspath(__file__))
        self.csv_path = os.path.join(data_dir, 'NEO_close.csv')

    def load_data(self):
        df = pd.read_csv(self.csv_path)

        distance_bin = [0, 0.1, 1, 5, 10]
        distnace_label = ['<0.1 LD', '0-1 LD', '1-5 LD', '5-10 LD']

        df['Distance Group'] = pd.cut(df['CA DistanceNominal (LD)'], bins=distance_bin, labels=distnace_label)

        df["Year"] = pd.to_numeric(df['Close-Approach (CA) Date'].str[:4])

        year_bin = [1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030]
        year_label = ['1890-1900', '1900-1910', '1910-1920', '1920-1930', '1930-1940', '1940-1950', '1950-1960', '1960-1970',
                       '1970-1980', '1980-1990', '1990-2000', '2000-2010', '2010-2020', '2020-2030']

        df['Year Group'] = pd.cut(df['Year'], bins=year_bin, labels=year_label)

        # print(df)
        return df

# start = Read_data()

# startt = start.load_data()