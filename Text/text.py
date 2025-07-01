import random

class Description:
    def __init__(self):
        self.app_description = "### Visualize historical and predicted near-Earth object flybys."

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

- Most NEOs and PHOs (Potentially hazardous objects) are **asteroids**.
- A very small number (about **0.3%**) are **comets**.
"""

        loading_text = ('Crunching space rocks...', 'Calculating asteroid trajectory...', 'Gathering satellite data...',
                        'Observing the sky...', 'Verifying planet positions...', 'Scanning for potential threats...',
                        'Negotiating with aliens...')
        
        self.df_info = """**This is the full formatted dataframe used for the plotting. To see or download the unformatted dataframe, visit NASA's official website.
          Note that the file format is csv.**"""

        self.random_loading = random.choice(loading_text)

        self.summary_info = 'Note that the data used to create the table is based on the time range selected.'

        self.summary_description = """
### Distance
- This metric shows how far the object is from Earth at its **estimated approach**, typically measured in kilometers or astronomical units (AU).
- Closest Distance refers specifically to the object's **minimum distance** from Earth during its closest estimated approach.
- In my data I've decided to use **lunar distance (LD)** to measure how far away certain NEOs are.

### Year
- This field represents the year in which each object made or is **expected** to make its closest approach to Earth.
- For clarity, the data is grouped into **10-year intervals**, making trends easier to interpret.
- Most Near-Earth Objects (NEOs) appear within a 10–20 year timeframe, as **shorter time horizons allow for more accurate trajectory calculations** and easier tracking.

### Magnitude
- Refers to the object’s **apparent brightness** as observed from Earth.
- **Lower** magnitude means a brighter and potentially larger object.

### Diameter
- This reflects the **estimated size** of the object, in meters.
- Larger diameters indicate more massive objects that can cause **greater impact damage** if they enter Earth’s atmosphere.

### Velocity
- Indicates the object’s speed **relative to Earth**, measured in kilometers per second (km/s).
- Higher velocities increase the energy of potential impacts and reduce reaction time for mitigation.

### Rarity
- Rarity scores represent how unusual or infrequent a particular object or event is.
- High rarity can mean either **extreme size, speed, proximity, or a combination**.

### Concern Score
- This is a calculated value based on factors like **distance, size, speed, and magnitude**.
- It serves as a composite risk indicator—higher scores **suggest** greater potential threat.
- Notably, a smaller NEO with a high certainty of impact may receive a **higher score** than a large NEO with virtually no chance of collision, emphasizing **likelihood** over size or speed alone.

"""

        self.top_neos = """
## Here is a list of 3 interesting NEOs that have passed by Earth or will pass by in the near future.

### 1. P/1999 J6 (SOHO)
- P/1999 J6 (SOHO) is the first periodic sungrazing comet discovered by SOHO scrutiny. This comet has passed Earth on the 12th of June 1999, 
at an astonishing speed of 43 km/s relative to our planet. It is considered one of, if not the fastest NEOs to come closer than 10 lunar distances (LD), having passed us by at a distance of 
~4.7 LD. 
- This distance also makes it one of the closest cometary flybys in recent history. Given its incredible speed, the comet is surprisingly small, having an estimated diameter of ~23-46 m. 
- This comet passes Earth periodically, its next pass happening in 2004, then 2010 and the next being on the 18th of June 2026.

### 2. 144898 (2004 VD17)
- 144898 (2004 VD17) is an Apollo-class Asteroid and one of the largest NEOs that is set to pass Earth in the future. The size also gives it 
its Potentially Hazardous Asteroid (PHA) classification.
- The closest flyby is predicted to take place on the 5th of May 2196 at ~2.5 LD. A more recent, although more distant, flyby will take place on 
the 7th of November 2041 at ~5 LD.
- The interesting aspect of this asteroid is its size, having a diameter between 440-990 m, and its 'rubbile pile' status, meaning that the asteroid is a loose 
colection of rocks that is only held together by gravity

### 3. 99942 Apophis (2004 MN4)
- 99942 Apophis (2004 MN4) is an Aten-class Asteroid and one of the rarest ones. What gives it its rarity factor is its estimated diameter, 
being ~340 m, and the distance at which it will pass as by, being ~0.09 LD.
- The asteroid will have its closest flyby on the 13th of April 2029. The size of this NEO puts it in the Potentially Hazardous Asteroid (PHA) category.
- Due to the distance of its flyby, it has been closely observed over the years and it was determined that the asteroid's impact risk is virtually zero, 
although its proximity will give scientists a unique opportunity to study its size, shape and orbit with high precision. During the flyby, its orbit will be 
affected by Earth's gravitational pull and thus change its trajectory for future flybys.

"""
        
    def main_text(self, sort_type):
        self.text_sort = {
            'Distance Group':{
                'text': """""",
                'sort description': (
        "Groups NEOs based on their most probable distance from Earth during close approach. "
    )
            },
            'Distance Group Close': {
                'text': """""",
                'sort description': (
        "Groups NEOs according to the closest possible distance they could approach Earth. "

    )
            },
            'Year Group': {
                'text': """""",
                'sort description': (
        "Groups NEOs by the year in which they make their close approach to Earth. "
    )
            },
            'Magnitude': {
                'text': """""",
                'sort description': (
        "Groups NEOs based on their apparent brightness (magnitude) as seen from Earth. "
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
    )
            }
        }

        return self.text_sort[sort_type]['text'], self.text_sort[sort_type]['sort description']