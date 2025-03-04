#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 19:30:30 2025

@author: pnl17v28
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 19:30:30 2025
@author: pnl17v28
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit UI
st.title("📊 The Impact of Meat Consumption: A Data Story")
st.write("This interactive dashboard explores trends, health effects, and environmental impact of meat consumption.")

# File Uploaders for Local Testing
st.sidebar.header("📂 Upload Data Files")
meat_file = st.sidebar.file_uploader("Upload Meat Consumption Data (Excel)", type=["xlsx"])
production_file = st.sidebar.file_uploader("Upload Global Meat Production Data (Excel)", type=["xlsx"])
health_file = st.sidebar.file_uploader("Upload Health Impact Data (Excel)", type=["xlsx"])
ghg_file = st.sidebar.file_uploader("Upload GHG Emissions Data (Excel)", type=["xlsx"])

# Load data only if files are provided
if meat_file and production_file and health_file and ghg_file:
    meat_consumption = pd.read_excel(meat_file, sheet_name=0)
    global_meat_production = pd.read_excel(production_file, sheet_name=0)
    health_impact = pd.read_excel(health_file, sheet_name=0)
    ghg_emissions = pd.read_excel(ghg_file, sheet_name=0)

    # Section 1: Meat Consumption Trends
    st.header("🥩 Meat Consumption Trends in Europe")
    st.write("How has meat consumption evolved in different European countries?")

    # Ensure "Year" exists in the dataset
    if "Year" in meat_consumption.columns:
        fig, ax = plt.subplots(figsize=(10,5))
        for country in meat_consumption.columns[1:]:
            ax.plot(meat_consumption["Year"], meat_consumption[country], label=country)
        ax.set_xlabel("Year")
        ax.set_ylabel("Kg per capita")
        ax.legend()
        st.pyplot(fig)
    else:
        st.error("⚠️ 'Year' column not found in Meat Consumption data. Please check the file format.")

    # Section 2: Global Meat Production
    st.header("🌍 Global Meat Production Over Time")
    st.write("A look at the rise in global meat production.")
    
    if "Year" in global_meat_production.columns and "Production (Million Tons)" in global_meat_production.columns:
        fig2, ax2 = plt.subplots()
        ax2.plot(global_meat_production["Year"], global_meat_production["Production (Million Tons)"], marker='o')
        ax2.set_xlabel("Year")
        ax2.set_ylabel("Million Tons")
        st.pyplot(fig2)
    else:
        st.error("⚠️ Expected columns not found in Global Meat Production data.")

    # Section 3: Health Impact
    st.header("🩺 Health Risks of High Meat Consumption")
    st.write("How does meat consumption correlate with health risks?")
    st.dataframe(health_impact.head())

    # Section 4: Environmental Impact
    st.header("🌱 Environmental Impact of Meat Production")
    st.write("Greenhouse gas emissions per kilogram of different food products.")

    if "Food Product" in ghg_emissions.columns:
        st.bar_chart(ghg_emissions.set_index("Food Product"))
    else:
        st.error("⚠️ 'Food Product' column not found in GHG Emissions data.")

    # Conclusion
    st.subheader("🔎 Key Takeaways")
    st.write("- Meat consumption is rising globally, with health and environmental consequences.")
    st.write("- Processed meats have the most negative health impact.")
    st.write("- Meat production contributes significantly to greenhouse gas emissions.")
    st.write("- Sustainable alternatives are gaining attention for health and environmental reasons.")

    st.write("🚀 What actions can we take? Reducing meat consumption can lead to a healthier planet and population")
