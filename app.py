import streamlit as st
from Plots.plots import Create_plot
from Text.text import Description

class Build():
    def __init__(self):
        st.title('NEO Flyby')

        self.plt = Create_plot()
        self.text = Description()
        self.side_panel()
        self.main_panel()

    def main_panel(self):
        st.info(self.text.right_description)
        
        st.info(self.text.left_description)

        option = st.radio(
            "### Group or sort by:",
            ("Estimated Distance (Most Likely)", "Estimated Distance (Closest Possible)",
            "Year of Approach", "Apparent Brightness","Estimated Diameter", 'Estimated Velocity (km/s)', "Rarity Score",
            'Concern Score')
        )


        option_sort = {
            'Estimated Distance (Most Likely)': 'Distance Group',
            'Estimated Distance (Closest Possible)': 'Distance Group Close',
            'Year of Approach': 'Year Group',
            'Apparent Brightness': 'Magnitude',
            'Estimated Diameter': 'Diameter Group',
            'Estimated Velocity (km/s)': 'Velocity Group',
            'Rarity Score': 'Rarity Group',
            'Concern Score': 'Score Group'
        }

        self.sort_type = option_sort[option]
        text, sort_description = self.text.main_text(self.sort_type)

        st.info(sort_description)
        
        chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))


        st.write()

    def side_panel(self):
        sb = st.sidebar.selectbox(
            'Choose the type of plot you would like:',
            ('Bar', 'BarH', 'Pie')
        )

        sb_sort = {
            'Bar': 'bar',
            'BarH': 'barh',
            'Pie': 'pie'
        }

        self.kind = sb_sort[sb]

        sb_time = st.sidebar.selectbox(
            'Select time range:',
            ('Historical Data', 'Predicted Data')
        )

        if sb_time == 'Historical Data':
            self.past = True
        else:
            self.past = False
        

start = Build()