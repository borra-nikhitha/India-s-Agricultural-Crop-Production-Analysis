Agricultural Crop Production Dashboard

An interactive analytics project that explores Agricultural Crop Production in India (1997–2021) using Tableau. The project analyzes crop production trends across different states, districts, seasons, and crops to provide meaningful agricultural insights. It combines a Flask web application, an embedded Tableau Dashboard, and a Tableau Story to present data-driven visualizations in a single, interactive platform.

Live Dataset Stats: Agricultural Crop Production Dataset (1997–2021) · State-wise, District-wise, Crop-wise and Season-wise analysis · Cleaned dataset with preprocessing completed.

Project Structure
project/
│
├── app.py                 # Flask application and routes
├── requirements.txt       # Python dependencies
│
├── templates/
│   ├── index.html         # Home page
│   ├── dashboard.html     # Embedded Tableau Dashboard
│   ├── story.html         # Embedded Tableau Story
│   ├── about.html         # Project documentation
│   └── dataset.html       # Dataset preview and download
│
└── assets/
    ├── css/
    │   └── style.css      # Website styling
    ├── js/
    │   └── app.js         # JavaScript functionality
    ├── images/
    └── icons/
 
 Tech Stack
Layer	Technology
Backend	Python, Flask
Frontend	HTML5, CSS3, JavaScript
Visualization	Tableau Public (Dashboard & Story)
Data	Microsoft Excel (.xlsx)
Version Control	GitHub

 Getting Started
Prerequisites
Python 3.10 or later
pip
Installation
# Clone the repository
git clone https://github.com/yourusername/Agricultural-Crop-Production-Dashboard.git

cd Agricultural-Crop-Production-Dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

 Pages
Route	Description
/	Home page with project overview, objectives and technology stack
/dashboard	Interactive Tableau Dashboard
/story	Tableau Story presenting agricultural insights
/about	Project documentation and business insights
/dataset	Dataset preview and download
 Dataset Overview

The dataset contains agricultural crop production information collected across different regions of India from 1997–2021.

It includes:

State
District
Crop
Year
Season
Area (Hectares)
Production (Tonnes)
Yield
 Tableau Resources

Tableau Story:
(Add your Tableau Story link if available)

Key Insights
The dashboard provides:
State-wise Crop Production Analysis
District-wise Production Comparison
Crop-wise Production Trends
Season-wise Agricultural Analysis
Year-wise Production Trends
Yield Analysis
Interactive Dashboard Filters
Business Insights for Agricultural Planning

Project Objectives
Analyze agricultural crop production trends.
Compare production across states and districts.
Study seasonal variations in agriculture.
Visualize crop production using Tableau.
Support data-driven agricultural decision-making.

License
This project was developed for academic and internship demonstration purposes using Tableau Public, Flask, HTML, CSS, JavaScript, and Microsoft Excel.
