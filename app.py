import streamlit as st
from Plots.plots import Create_plot

class Build():
    def __init__(self):
        st.title('NEO Flyby')

        self.plt = Create_plot()
        self.side_panel()
        self.main_screen()

    def main_screen(self):
        description = st.write("""
        NEO Flyby is an app that allows you to visualize data and statistics about near earth objects(NEOs).
        """)

        option = st.radio(
            "### Group or sort by:",
            ("Estimated Distance (Most Likely)", "Estimated Distance (Closest Possible)",
            "Year of Approach", "Apparent Brightness","Estimated Diameter", 'Estimated Velocity (km/s)', "Rarity Score")
        )

        option_sort = {
            'Estimated Distance (Most Likely)': 'Distance Group',
            'Estimated Distance (Closest Possible)': 'Distance Group Close',
            'Year of Approach': 'Year Group',
            'Apparent Brightness': 'Magnitude',
            'Estimated Diameter': 'Diameter Group',
            'Estimated Velocity (km/s)': 'Velocity Group',
            'Rarity Score': 'Rarity Group'
        }

        self.sort_type = option_sort[option]
        chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))

    def side_panel(self):
        sb = st.sidebar.selectbox(
            'Choose the type of plot you would like:',
            ('Line', 'Bar', 'Barh', 'Area', 'Pie')
        )

        sb_sort = {
            'Line': 'line',
            'Bar': 'bar',
            'Barh': 'barh',
            'Area': 'area',
            'Pie': 'pie'
        }

        self.kind = sb_sort[sb]

        sb_time = st.sidebar.selectbox(
            'Select time range',
            ('Historical Data', 'Predicted Data')
        )

        if sb_time == 'Historical Data':
            self.past = True
        else:
            self.past = False
        

start = Build()