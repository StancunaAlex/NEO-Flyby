import matplotlib.pyplot as plt
from Data.data import Read_data
import numpy as np

class Create_plot():
    def __init__(self):
        self.read = Read_data()
        self.df = self.read.load_data()
        self.size = (16, 12)
        self.title_size = 30
        self.fontsize = 18
    
    def create_chart(self, kind, name_x, title):
        fig, ax = plt.subplots(figsize=self.size)
        self.counts.plot(kind=kind, ax=ax)

        if kind == 'barh':
            ax.set_xlabel('Number of NEOs', fontsize=self.fontsize)
            ax.set_ylabel(name_x, fontsize=self.fontsize)
        elif kind == 'pie':
            ax.set_xlabel('')
            ax.set_ylabel('')
            
        else:
            ax.set_xlabel(name_x, fontsize=self.fontsize)
            ax.set_ylabel('Number of NEOs', fontsize=self.fontsize)

        fig.suptitle(title, fontsize=self.title_size)
        fig.tight_layout()
        return fig

    def by_distance(self, kind):
        self.counts = self.df['Distance Group'].value_counts().sort_index()

        name_x = 'Distance'
        title = 'Estimated distance of the NEO relative to Earth'

        return self.create_chart(kind, name_x, title)
    
    def by_distance_close(self, kind):
        self.counts = self.df['Distance Group Close'].value_counts().sort_index()

        name_x = 'Distance'
        title = 'Estimated closest possible distance of the NEO relative to Earth'

        return self.create_chart(kind, name_x, title)
    
    def by_year(self, kind):
        self.counts = self.df['Year Group'].value_counts().sort_index()

        name_x = 'Year Group'
        title = 'Year in which NEO passed by Earth'
        
        return self.create_chart(kind, name_x, title)
    
    def by_magnitude(self, kind):
        self.counts = self.df['Magnitude'].value_counts().sort_index()

        name_x = 'Brightness'
        title = 'Brightness of the NEO'

        return self.create_chart(kind, name_x, title)

    def by_diameter(self, kind):
        self.counts = self.df['Diameter Group'].value_counts().sort_index()

        name_x = 'Diameter'
        title = 'Diameter of the NEO'

        return self.create_chart(kind, name_x, title)

    def by_rarity(self, kind):
        self.counts = self.df['Rarity Group'].value_counts().sort_index()

        name_x = 'Rarity'
        title = 'Rarity of the NEO'

        return self.create_chart(kind, name_x, title)