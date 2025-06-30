import streamlit as st
import time
import os
from Plots.plots import Create_plot
from Text.text import Description

class Build():
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.icon_path = os.path.join(script_dir, 'Resources', 'NEO_icon.png')

        st.set_page_config(layout='wide')

        self.plt = Create_plot()
        self.text = Description()
        self.df = self.plt.read
        self.side_panel()
        self.main_panel()

    def main_panel(self):
        st.title('NEO Flyby')
        st.markdown(self.text.app_description)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            with st.expander('Information on NEOs'):
                st.markdown(self.text.info)

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
            
            self.sort_type = option_sort[self.option]
            text, sort_description = self.text.main_text(self.sort_type)
        
            with st.spinner(self.text.random_loading):
                time.sleep(self.plt.rand)
                st.info(sort_description)
                chart = st.pyplot(self.plt.sort(self.kind, self.past, self.sort_type))

        st.caption(self.text.df_info)
        st.dataframe(self.df.dataframe(), use_container_width=True, height=100)

        st.caption("Created by Alex | [GitHub](https://github.com/StancunaAlex) | [LinkedIn](https://www.linkedin.com/in/alex-stancuna/) | Powered by NASA")

    def side_panel(self):
        st.sidebar.image(self.icon_path, width=64)

        self.option = st.sidebar.selectbox(
            "### Group or sort by:",
            ("Estimated Distance (Most Likely)", "Estimated Distance (Closest Possible)",
            "Year of Approach", "Apparent Brightness","Estimated Diameter", 'Estimated Velocity (km/s)', "Rarity Score",
            'Concern Score')
        )

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
            ('Historical Data', 'Predicted Data', 'All Data')
        )

        if 'Historical Data' in sb_time:
            self.past = True
        else:
            self.past = False
        
start = Build()