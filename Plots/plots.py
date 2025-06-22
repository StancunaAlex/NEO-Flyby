import matplotlib.pyplot as plt
from Data.data import Read_data
import numpy as np

class Create_plot():
    def __init__(self):
        self.read = Read_data()
        self.size = (16, 12)
        self.title_size = 30
        self.fontsize = 18
    
    def create_chart(self, kind, name_x, title, labels):
        fig, ax = plt.subplots(figsize=self.size)
        self.counts.plot(kind=kind, ax=ax)

        if kind == 'barh':
            ax.set_xlabel('Number of NEOs', fontsize=self.fontsize)
            ax.set_ylabel(name_x, fontsize=self.fontsize)
        elif kind == 'pie':
            ax.set_xlabel('')
            ax.set_ylabel('')
            plt.legend(labels)
        else:
            ax.set_xlabel(name_x, fontsize=self.fontsize)
            ax.set_ylabel('Number of NEOs', fontsize=self.fontsize)

        fig.suptitle(title, fontsize=self.title_size)
        fig.tight_layout()
        return fig
    
    def sort(self, kind, past, sort_type):
        self.df = self.read.load_data(past)

        if sort_type == 'Distance Group':

            self.counts = self.df[sort_type].value_counts().reindex(self.read.distnace_label[::-1])
            labels = self.read.distnace_label[::-1]

            name_x = 'Distance'
            title = "Estimated Flyby Distance of the NEO"

        elif sort_type == 'Distance Group Close':

            self.counts = self.df[sort_type].value_counts().reindex(self.read.distnace_label[::-1])
            labels = self.read.distnace_label[::-1]

            name_x = 'Distance'
            title = "Minimum Possible Flyby Distance of the NEO"

        elif sort_type == 'Year Group':

            self.counts = self.df[sort_type].value_counts().reindex(self.read.year_label)
            labels = self.read.year_label

            name_x = 'Year Group'
            title = "Year of NEO Flyby"

        elif sort_type == 'Magnitude':

            self.counts = self.df[sort_type].value_counts().reindex(self.read.magnitude_label[::-1])
            labels = self.read.magnitude_label[::-1]

            name_x = 'Brightness'
            title = "Estimated Brightness (H Magnitude) of the NEO"

        elif sort_type == 'Diameter Group':

            self.counts = self.df[sort_type].value_counts().sort_index()
            labels = self.read.diameter_labels

            name_x = 'Diameter'
            title = "Estimated Diameter of the NEO"

        elif sort_type == 'Rarity Group':

            self.counts = self.df[sort_type].value_counts().sort_index()
            labels = self.read.rarity_label

            name_x = 'Rarity'
            title = "Rarity Score of the NEO"

        return self.create_chart(kind, name_x, title, labels)