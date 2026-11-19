
# Import required libraries
import streamlit as st
from pathlib import Path

# Configure the dashboard
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="📊",
    layout="wide"
)

# Get the project root and chart folder
project_root = Path(__file__).resolve().parent.parent
figures_folder = project_root / "Reports" / "figures"

# Dashboard title
st.title("Employee Attrition Analysis Dashboard")
st.write("Explore employee data through visualizations.")

# First chart: Employee count by department
st.header("1. Employee Count by Department")

department_chart = figures_folder / "employee_count_by_department.png"

if department_chart.exists():
    st.image(str(department_chart), caption="Employee count by department")
else:
    st.error("Department chart not found.")

# Second chart: Employee age distribution
st.header("2. Employee Age Distribution")

age_chart = figures_folder / "employee_age_distribution.png"

if age_chart.exists():
    st.image(str(age_chart), caption="Employee age distribution")
else:
    st.error("Age distribution chart not found.")

# Footer
st.caption("Week 1 Project | Employee Attrition Data Analysis")