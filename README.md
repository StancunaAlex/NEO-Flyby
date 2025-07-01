# NEO-Flyby
## Description
This project analyzes **Near-Earth Objects (NEOs)**, tracking their size, distance from Earth, velocity, and potential risk factors. It uses data from NASA's **CNEOS** (Center for Near-Earth Object Studies) to categorize and score NEOs based on various metrics, such as their **potentially hazardous** status and close approaches. The app also visualizes these metrics to provide insights into the future and past behavior of NEOs.

## Features
- **Data Parsing:** Automatically cleans and processes NEO data from CSV files.
- **Dynamic Categorization:** Classifies NEOs based on various factors like size, distance, and velocity.
- **Risk Scoring:** Calculates and visualizes risk scores based on proximity, speed, and size.
- **Visualization:** Interactive charts displaying categorized data for better understanding.
- **User Input:** Ability to load data for past or future NEOs, or both.

## Usage
You can either clone the repository and run it locally, or simply use the link provided below to check it out via Streamlit.

[Check out the NEO-Flyby App here](https://stancunaalex-neo-flyby-app-cjjcwl.streamlit.app/)

## How to Run the App Locally

If you prefer to run the app locally instead of using the online version, follow these steps:

### Prerequisites
Ensure that you have the following installed on your machine:
- [Python](https://www.python.org/downloads/) (Version 3.7 or later)
- [pip](https://pip.pypa.io/en/stable/), the Python package installer

### Steps to Run the App Locally:

1. **Clone the Repository:**
   First, clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/neo-flyby.git
   ```
   
2. **Navigate to the Project Directory:**

   ```bash
   cd neo-flyby
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. You can start the app with:
   ```bash
    python -m neo-flyby
    ```

   ## How It Works
- Upon launching the app, users can select past or future NEO data and view categorized data, including visualizations for different metrics like distance and velocity.
- Users can interact with the data by selecting different categories and observing how NEOs are classified and scored based on potential impact risk.
