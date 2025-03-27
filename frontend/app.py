import streamlit as st
import requests

API_URL = "http://backend:5000/analyze_task"

st.title("Developer Task Analyzer")

task_description = st.text_area("Enter Task Description:", "")

if st.button("Analyze Task"):
    if task_description.strip():
        with st.spinner("Analyzing task..."):
            response = requests.post(API_URL, json={"task_description": task_description})
            if response.status_code == 200:
                result = response.json()
                
                # Display task breakdown
                st.subheader("Task Breakdown")
                st.json(result["sub_tasks"])

                # Generate and display flowchart
                st.subheader("Flowchart")
                st.graphviz_chart(result["flowchart"])
            else:
                st.error("Error: Unable to analyze task.")
    else:
        st.warning("Please enter a task description.")
