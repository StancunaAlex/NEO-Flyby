import matplotlib.pyplot as plt
from Data.data import Read_data
import numpy as np

class Create_plot():
    def __init__(self):
        self.read = Read_data()
        self.size = (16, 12)
        self.title_size = 30
        self.fontsize = 22

        self.rand = np.random.uniform(0.3, 0.8)

    def percent_filter(pct):
        return f'{pct:.0f}%' if pct >= 1 else ''
    
    def create_chart(self, kind, name_x, title, labels, explode):

        fig, ax = plt.subplots(figsize=self.size)
        data_ax1 = self.counts
        data_ax2 = labels

        colors = [
        '#0288D1', '#FF7043', '#388E3C', '#7B1FA2',
        '#FFA000', '#00796B', '#D32F2F', '#303F9F',
        '#F4511E', '#2E7D32', '#1976D2', '#8E24AA',
        '#F9A825', '#455A64'
    ]

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
            
            ax.pie(self.counts, startangle=90, counterclock=False, normalize=True,
                    autopct=percent_filter, pctdistance=1.08, colors=colors,
                    explode=explode, shadow=True)
            ax.legend(percentage, fontsize=9, loc='upper left')
            fig.suptitle(title, fontsize=self.title_size)
        elif kind == 'barh':
            barh = ax.barh(data_ax2, data_ax1)
            ax.bar_label(barh, fmt='%.0f')

            ax.set_ylabel(name_x, fontsize=self.fontsize)
            ax.set_xlabel('Number of NEOs', fontsize=self.fontsize)
        else:
            barh = ax.bar(data_ax2, data_ax1)
            ax.bar_label(barh, fmt='%.0f')

            ax.set_xlabel(name_x, fontsize=self.fontsize)
            ax.set_ylabel('Number of NEOs', fontsize=self.fontsize)

        return fig
    
    def sort(self, kind, past, sort_type):
        self.df = self.read.load_data(past)


        sort_dict = {
            'Distance Group': {
                'count': self.df[sort_type].value_counts().reindex(self.read.distnace_label[::-1]),
                'label': self.read.distnace_label[::-1],
                'name': 'Distance',
                'title': 'Estimated Flyby Distance of the NEO',
                'explode': (0, 0.1, 0, 0, 0, 0)
            },
            'Distance Group Close': {
                'count': self.df[sort_type].value_counts().reindex(self.read.distnace_label[::-1]),
                'label': self.read.distnace_label[::-1],
                'name': 'Distance',
                'title': 'Minimum Possible Flyby Distance of the NEO',
                'explode': (0, 0.1, 0, 0, 0, 0)
            },
            'Year Group': {
                'count': self.df[sort_type].value_counts().reindex(self.read.year_label),
                'label': self.read.year_label,
                'name': 'Year Group',
                'title': 'Year of NEO Flyby',
                'explode': (0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            },
            'Magnitude': {
                'count': self.df[sort_type].value_counts().reindex(self.read.magnitude_label[::-1]),
                'label': self.read.magnitude_label[::-1],
                'name': 'Brightness',
                'title': 'Estimated Brightness (H Magnitude) of the NEO',
                'explode': (0, 0, 0.1, 0, 0, 0)
            },
            'Diameter Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.diameter_labels,
                'name': 'Diameter',
                'title': 'Estimated Diameter of the NEO',
                'explode': (0, 0.1, 0, 0, 0, 0, 0)
            },
            'Velocity Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.velocity_labels,
                'name': 'Velocity',
                'title': 'Relative Velocity of the NEO',
                'explode': (0, 0.1, 0, 0, 0, 0, 0)
            },
            'Rarity Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.rarity_label,
                'name': 'Rarity',
                'title': 'Rarity Score of the NEO',
                'explode': (0, 0.1, 0, 0, 0, 0)
            },
            'Score Group': {
                'count': self.df[sort_type].value_counts().sort_index(),
                'label': self.read.score_label,
                'name': 'Concern',
                'title': 'Concern Score of the NEO',
                'explode': (0, 0.1, 0, 0, 0)
            }
        }
        
        if past == True:
            sort_dict['Year Group']['explode'] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0)

        self.counts = sort_dict[sort_type]['count']
        labels = sort_dict[sort_type]['label']
        explode_count = sort_dict[sort_type]['explode']
        name_x = sort_dict[sort_type]['name']
        title = sort_dict[sort_type]['title']

        return self.create_chart(kind, name_x, title, labels, explode_count)
    
def percent_filter(pct):
    return f'{pct:.1f}%' if pct >= 1 else ''
