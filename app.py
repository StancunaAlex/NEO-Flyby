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
            "### Organize:",
            ("By Distance(Most likely)", "By Distance(Closest Possible)",
              "By Year", "By Brightness", "By Diameter", "By Rarity")
        )

        if option == 'By Distance(Most likely)':
            chart = st.pyplot(self.plt.by_distance(self.kind))
        elif option == 'By Distance(Closest Possible)':
            chart = st.pyplot(self.plt.by_distance_close(self.kind))
        elif option == 'By Year':
            chart = st.pyplot(self.plt.by_year(self.kind))
        elif option == 'By Brightness':
            chart = st.pyplot(self.plt.by_magnitude(self.kind))
        elif option == 'By Diameter':
            chart = st.pyplot(self.plt.by_diameter(self.kind))
        elif option == 'By Rarity':
            chart = st.pyplot(self.plt.by_rarity(self.kind))

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

        # sb_time = st.sidebar.selectbox(
        #     'Choose the timeline:',
        #     ('Past', 'Future')
        # )

        # if sb_time == 'Past':
        #     pass
        # elif sb_time == 'Future':
        #     pass
        

start = Build()