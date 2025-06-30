import random

class Description:
    def __init__(self):
        self.app_description = "### Analyze and visualize historical and predicted near-Earth object flybys."

        self.info = """
        ### What is a Near-Earth Object (NEO)?

- A **Near-Earth Object (NEO)** is a small object in space that orbits the Sun.
- It gets **close to Earth’s orbit**, specifically coming within **1.3 times the distance between Earth and the Sun**.  
  (This distance is called an **astronomical unit (AU)**.)

### Important Details About NEOs

- The definition depends on the object’s **orbit around the Sun**, not where it is right now.
- This means an NEO might be far from Earth at the moment but still considered an NEO because its orbit brings it close to Earth at some point.

  ### What Makes an NEO Potentially Hazardous?

- If an NEO’s orbit **crosses Earth’s orbit** and it is **larger than 140 meters (about 460 feet)** across, it is called a **Potentially Hazardous Object (PHO)**.
- These objects are monitored closely because they could pose a risk to Earth.

### Types of NEOs

- Most NEOs and PHOs are **asteroids**.
- A very small number (about **0.3%**) are **comets**.
"""

        loading_text = ('Crunching space rocks...', 'Calculating asteroid trajectory...', 'Gathering satellite data...',
                        'Observing the sky...', 'Verifying planet positions...', 'Scanning for potential threats...',
                        'Negotiating with aliens...')
        
        self.df_info = """**This is the full formatted dataframe used for the plotting. To see or download the unformatted dataframe, visit NASA's official website.
          Note that the file format is csv.**"""

        self.random_loading = random.choice(loading_text)
        
    def main_text(self, sort_type):
        self.text_sort = {
            'Distance Group':{
                'text': """""",
                'sort description': (
        "Groups NEOs based on their most probable distance from Earth during close approach."
        "This reflects the best estimate of how near each object will come."
    )
            },
            'Distance Group Close': {
                'text': """""",
                'sort description': (
        "Groups NEOs according to the closest possible distance they could approach Earth, "
        "accounting for uncertainties in their orbits. Represents the minimum potential distance."
    )
            },
            'Year Group': {
                'text': """""",
                'sort description': (
        "Groups NEOs by the year in which they make their close approach to Earth, "
        "allowing visualization of flybys over time. For simplicity, the years are grouped into 10-year intervals."
    )
            },
            'Magnitude': {
                'text': """""",
                'sort description': (
        "Groups NEOs based on their apparent brightness (magnitude) as seen from Earth. "
        "Lower magnitudes mean brighter objects."
    )
            },
            'Diameter Group': {
                'text': """""",
                'sort description': (
        "Groups NEOs by their estimated physical size (diameter), giving insight into the scale of the object."
    )
            },
            'Velocity Group': {
                'text': """""",
                'sort description': (
        "Groups NEOs by their estimated speed relative to Earth at close approach, measured in kilometers per second."
    )
            },
            'Rarity Group': {
                'text': """""",
                'sort description': (
        "Groups NEOs according to NASA's rarity metric indicating how unusual or infrequent their flyby characteristics are."
    )
            },
            'Score Group': {
                'text': """""",
                'sort description': (
        "Groups NEOs by a risk assessment score representing the potential hazard level they pose to Earth."
        " Note that a NEO with a 100% chance of impacting Earth will always score higher than a much larger NEO with virtually no chance of collision."
    )
            }
        }

        return self.text_sort[sort_type]['text'], self.text_sort[sort_type]['sort description']