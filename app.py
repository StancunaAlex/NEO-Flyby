import streamlit as st
from Plots.plots import Create_plot

class Build():
    def __init__(self):
        st.title('NEO Flyby')

        plt = Create_plot()
        distance_plot = plt.by_distance()
        year_plot = plt.by_year()

        st.write("""
        NEO Flyby is an app that allows you to visualize data and statistics about near earth objects(NEO's).
        """)

        option = st.radio(
            "### Organize:",
            ("By Distance(Most likely)", "By Distance(Closest Possible)", "By Year", "By Magnitude")
        )

        if option == 'By Distance(Most likely)':
            chart = st.pyplot(distance_plot)
        elif option == 'By Distance(Closest Possible)':
            chart = st.pyplot()
        elif option == 'By Year':
            chart = st.pyplot(year_plot)
        else:
            chart = st.pyplot()


start = Build()