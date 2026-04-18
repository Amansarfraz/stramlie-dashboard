import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Student Dashboard", layout="wide")

st.title("📊 Student Performance Dashboard")
st.write("Simple student marks analysis dashboard")

# -------------------------------
# DATA
# -------------------------------
data = pd.DataFrame({
    "Student": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"],
    "Math": [80, 55, 90, 70, 60],
    "English": [75, 65, 88, 72, 58],
    "Science": [85, 60, 92, 68, 66]
})

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.header("Select Student")

selected_student = st.sidebar.selectbox(
    "Choose Student",
    data["Student"]
)

# Filter student row
student_data = data[data["Student"] == selected_student].iloc[0]

# -------------------------------
# CALCULATIONS (FIXED)
# -------------------------------
total = student_data["Math"] + student_data["English"] + student_data["Science"]
avg = total / 3

# -------------------------------
# METRICS
# -------------------------------
st.subheader("📌 Performance Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Marks", total)
col2.metric("Average Marks", round(avg, 2))
col3.metric("Subjects", 3)

# -------------------------------
# CHART DATA
# -------------------------------
st.subheader("📈 Subject-wise Marks")

chart_data = pd.DataFrame({
    "Subjects": ["Math", "English", "Science"],
    "Marks": [student_data["Math"], student_data["English"], student_data["Science"]]
})

st.bar_chart(chart_data.set_index("Subjects"))

# -------------------------------
# TABLE
# -------------------------------
st.subheader("📋 Student Details")

st.dataframe(pd.DataFrame([student_data]))

# -------------------------------
# RESULT MESSAGE
# -------------------------------
if avg >= 80:
    st.success("🌟 Excellent Performance")
elif avg >= 60:
    st.info("👍 Good Performance")
else:
    st.warning("⚠️ Need Improvement")