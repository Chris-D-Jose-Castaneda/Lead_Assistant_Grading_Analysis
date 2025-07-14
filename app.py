import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.graph_objects import Indicator, Figure

# ------------------------
# Configuration
# ------------------------
st.set_page_config(
    page_title="Grading Calculator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------
# Sidebar: Theme & Tips
# ------------------------
with st.sidebar:
    st.title("Settings & Tips")
    # Default to Light theme
    theme = st.radio("Theme", ["Light", "Dark"], index=0)
    st.markdown("---")
    # Success Tips styled in black for readability
    st.markdown(
        """
        <div style='color:black; font-weight:bold;'>Success Tips:</div>
        <ul style='color:black;'>
          <li>Attend lectures regularly</li>
          <li>Visit office hours for help 7pm–9pm</li>
          <li>Email TAs early with questions</li>
        </ul>
        """, unsafe_allow_html=True
    )

# ------------------------
# Apply Dark Mode CSS (only if selected)
# ------------------------
if theme == "Dark":
    st.markdown(
        """
        <style>
        /* Main background and text */
        .stApp, .css-18e3th9 { background-color: #1e1e2e; color: #e0e0e0; }
        /* Sidebar */
        .css-1d391kg { background-color: #2d2d44; }
        /* Number inputs */
        .stNumberInput>div>input { background-color: #2d2d44; color: #e0e0e0; border: none; }
        /* Metric values */
        .stMetric-value { color: #80ffdb; }
        /* Slider styling */
        input[type=range]::-webkit-slider-thumb { background: #4ecdc4; }
        input[type=range]::-webkit-slider-runnable-track { background: #44475a; height: 4px; }
        </style>
        """, unsafe_allow_html=True
    )

# ------------------------
# Title
# ------------------------
st.title("📊 Grading Calculator")

# ------------------------
# User Inputs
# ------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Prelims & Final (50%)")
    p1 = st.number_input("Prelim I (%)", min_value=0.0, max_value=100.0, step=0.1)
    p2 = st.number_input("Prelim II (%)", min_value=0.0, max_value=100.0, step=0.1)
    p3 = st.number_input("Final (%)", min_value=0.0, max_value=100.0, step=0.1)
with col2:
    st.subheader("Templates (30%) — 5% each")
    word = st.number_input("Word Template (%)", min_value=0.0, max_value=100.0, step=0.1)
    letter = st.number_input("Letterhead Template (%)", min_value=0.0, max_value=100.0, step=0.1)
    report = st.number_input("Report Template (%)", min_value=0.0, max_value=100.0, step=0.1)
with col3:
    st.subheader("Templates cont.")
    ppt = st.number_input("PowerPoint Template (%)", min_value=0.0, max_value=100.0, step=0.1)
    xanalysis = st.number_input("Excel Analysis (%)", min_value=0.0, max_value=100.0, step=0.1)
    xmodel = st.number_input("Excel Model (%)", min_value=0.0, max_value=100.0, step=0.1)

st.subheader("Daily Assignments (20%)")
# Use a red accent for light theme slider
slider_style = "style='background: #ff4b4b'" if theme == "Light" else ""
daily = st.slider("Daily Avg (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

# ------------------------
# Calculations
# ------------------------
w_pre = 0.50 / 3
w_tpl = 0.30 / 6
w_daily = 0.20
c_p1 = p1 * w_pre
c_p2 = p2 * w_pre
c_p3 = p3 * w_pre
c_templates = (word + letter + report + ppt + xanalysis + xmodel) / 6 * 0.30
c_daily = daily * w_daily
total_pct = round(c_p1 + c_p2 + c_p3 + c_templates + c_daily, 2)

# Letter grade logic
def get_letter(p):
    if p >= 97: return "A+"
    if p >= 94: return "A"
    if p >= 90: return "A-"
    if p >= 87: return "B+"
    if p >= 84: return "B"
    if p >= 80: return "B-"
    if p >= 77: return "C+"
    if p >= 74: return "C"
    if p >= 70: return "C-"
    if p >= 67: return "D+"
    if p >= 64: return "D"
    if p >= 60: return "D-"
    return "F"
letter = get_letter(total_pct)

# ------------------------
# Display Results
# ------------------------
st.subheader("🎯 Results")
col4, col5 = st.columns(2)
col4.metric("Final %", f"{total_pct:.2f}%")
col5.metric("Letter Grade", letter)

# Component bar chart
contribs = pd.DataFrame({
    'Category': ['Prelim1','Prelim2','Final','Templates','Daily'],
    'Points': [c_p1, c_p2, c_p3, c_templates, c_daily]
})
fig_bar = px.bar(
    contribs, x='Category', y='Points', text='Points',
    title="Contribution to Final Grade (in % points)",
    template=('plotly_white' if theme=='Light' else 'plotly_dark')
)
fig_bar.update_traces(textposition='outside')
st.plotly_chart(fig_bar, use_container_width=True)

# Overall gauge
fig_gauge = Figure(Indicator(
    mode="gauge+number", value=total_pct,
    gauge={ 'axis': {'range': [0,100]}, 'bar': {'color': '#ff4b4b' if theme=='Light' else '#80ffdb'},
            'steps': [{'range': [0,60],'color':'#ff6b6b'},
                      {'range': [60,80],'color':'#ffd93d'},
                      {'range': [80,100],'color':'#4ecdc4'}]
    }
))
fig_gauge.update_layout(title="Overall Grade Gauge", margin={'t':50,'b':0,'l':0,'r':0})
st.plotly_chart(fig_gauge, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='color:black'>******************************************************************************** Built by cdj48. Ensure lecture attendance and TA engagement for success. ********************************************************************************</p>", unsafe_allow_html=True)
