import streamlit as st
import pandas as pd

# Taxonomy mapping
taxonomy_map = {
    "Salary": "Fees Earned or Paid in Cash",
    "Bonus": "Non-Equity Incentive Plan Compensation",
    "Stock Awards": "Stock Awards",
    "Other Compensation": "All Other Compensation",
    "Total": "Total Compensation"
}

st.title("Compensation Entry Generator")

# Sidebar or main controls
with st.form("comp_form"):
    col1, col2 = st.columns(2)
    with col1:
        selected_params = st.multiselect(
            "Parameters", list(taxonomy_map.keys())
        )
    with col2:
        selected_years = st.multiselect(
            "Years", ["2022", "2023", "2024"]
        )
    
    repeat = st.number_input("Repeat", min_value=1, value=1, step=1)
    submitted = st.form_submit_button("Generate")

# Table generation
if submitted:
    records = []
    selected_years.sort()
    for r in range(repeat):
        for year in selected_years:
            for param in selected_params:
                taxonomy = taxonomy_map.get(param, "Unknown")
                records.append({
                    "Executive": "",
                    "Parameter": param,
                    "Year": year,
                    "Taxonomy": taxonomy
                })
    
    df = pd.DataFrame(records)
    st.write("### Generated Table")
    st.dataframe(df, use_container_width=True)
