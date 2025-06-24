import matplotlib.pyplot as plt
from Data.data import Read_data
import numpy as np

class Create_plot():
    def __init__(self):
        self.read = Read_data()
        self.size = (16, 12)
        self.title_size = 34
        self.fontsize = 22
    
    def create_chart(self, kind, name_x, title, labels):

        fig, ax = plt.subplots(figsize=self.size)
        data_ax1 = self.counts
        data_ax2 = labels

        ax.set_xlabel(name_x, fontsize=self.fontsize)
        ax.set_ylabel('Number of NEOs', fontsize=self.fontsize)

        legend = [f'{label} - {count}'
            for label, count in zip(labels, self.counts)
            ]
        ax.legend(legend, title='Number of NEOs', fontsize=14, loc='upper right')

        fig.suptitle(title, fontsize=self.title_size)
        fig.tight_layout()
        
        if kind == 'pie':
            fig, ax = plt.subplots(figsize=self.size)
            ax.set_xlabel('')
            ax.set_ylabel('')

            total_pie = self.counts.sum()
            percentage = [f'{label} - {count / total_pie:.1%}'
                          for label, count in zip(labels, self.counts)
                          ]
            
            ax.pie(self.counts, startangle=90, counterclock=False, normalize=True)
            ax.legend(percentage, fontsize=14, loc='upper left')
            fig.suptitle(title, fontsize=self.title_size)
        elif kind == 'barh':
            barh = ax.barh(data_ax2, data_ax1)
            ax.bar_label(barh, fmt='%.0f')
        elif kind == 'bar':
            barh = ax.bar(data_ax2, data_ax1)
            ax.bar_label(barh, fmt='%.0f')

        return fig
    
    def sort(self, kind, past, sort_type):
        self.df = self.read.load_data(past)

        sort_dict = {
            'Distance Group': {
                'count': self.df[sort_type].value_counts().reindex(self.read.distnace_label[::-1]),
                'label': self.read.distnace_label[::-1],
                'name': 'Distance',
                'title': 'Estimated Flyby Distance of the NEO'
            },
            'Distance Group Close': {
                'count': self.df[sort_type].value_counts().reindex(self.read.distnace_label[::-1]),
                'label': self.read.distnace_label[::-1],
                'name': 'Distance',
                'title': 'Minimum Possible Flyby Distance of the NEO'
            },
            'Year Group': {
                'count': self.df[sort_type].value_counts().reindex(self.read.year_label),
                'label': self.read.year_label,
                'name': 'Year Group',
                'title': 'Year of NEO Flyby'
            },
            'Magnitude': {
                'count': self.df[sort_type].value_counts().reindex(self.read.magnitude_label[::-1]),
                'label': self.read.magnitude_label[::-1],
                'name': 'Brightness',
                'title': 'Estimated Brightness (H Magnitude) of the NEO'
            },
            'Diameter Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.diameter_labels,
                'name': 'Diameter',
                'title': 'Estimated Diameter of the NEO'
            },
            'Velocity Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.velocity_labels,
                'name': 'Velocity',
                'title': 'Relative Velocity of the NEO'
            },
            'Rarity Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.rarity_label,
                'name': 'Rarity',
                'title': 'Rarity Score of the NEO'
            },
            'Score Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.score_label,
                'name': 'Concern',
                'title': 'Concern Score of the NEO'
            }
        }

        self.counts = sort_dict[sort_type]['count']
        labels = sort_dict[sort_type]['label']

        name_x = sort_dict[sort_type]['name']
        title = sort_dict[sort_type]['title']

        return self.create_chart(kind, name_x, title, labels)