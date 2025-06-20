import matplotlib.pyplot as plt
from Data.data import Read_data
import numpy as np

class Create_plot():
    def __init__(self):
        self.read = Read_data()
        self.df = self.read.load_data()

        self.kind = 'line'
    
    def by_distance(self):
        counts = self.df['Distance Group'].value_counts().sort_index()

        self.fig, self.ax = plt.subplots(figsize=(11, 9))
        counts.plot(kind=self.kind)
        return self.fig
    
    def by_distance_close(self):
        pass
    
    def by_year(self):
        counts = self.df['Year Group'].value_counts().sort_index()

        self.fig, self.ax = plt.subplots(figsize=(11, 9))
        counts.plot(kind=self.kind, ax=self.ax)
        return self.fig
    
    def by_magnitude(self):
        pass