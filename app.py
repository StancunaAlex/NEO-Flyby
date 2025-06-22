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
            "Year of Approach", "Apparent Brightness","Estimated Diameter", "Rarity Score")
        )

        if option == 'Estimated Distance (Most Likely)':
            self.sort_type = 'Distance Group'
            chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))
        elif option == 'Estimated Distance (Closest Possible)':
            self.sort_type = 'Distance Group Close'
            chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))
        elif option == 'Year of Approach':
            self.sort_type = 'Year Group'
            chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))
        elif option == 'Apparent Brightness':
            self.sort_type = 'Magnitude'
            chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))
        elif option == 'Estimated Diameter':
            self.sort_type = 'Diameter Group'
            chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))
        elif option == 'Rarity Score':
            self.sort_type = 'Rarity Group'
            chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))

    def side_panel(self):
        sb = st.sidebar.selectbox(
            'Choose the type of plot you would like:',
            ('Line', 'Bar', 'Barh', 'Area', 'Pie')
        )

        if sb == 'Line':
            self.kind = 'line'
        elif sb == 'Bar':
            self.kind = 'bar'
        elif sb == 'Barh':
            self.kind = 'barh'
        elif sb == 'Area':
            self.kind = 'area'
        elif sb == 'Pie':
            self.kind = 'pie'

        sb_time = st.sidebar.selectbox(
            'Select time range',
            ('Historical Data', 'Predicted Data')
        )

        if sb_time == 'Historical Data':
            self.past = True
        else:
            self.past = False
        

start = Build()