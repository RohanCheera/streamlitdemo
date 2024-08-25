import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Interactive Streamlit App")

# Add a slider
slider_value = st.slider("Pick a number", 0, 100, 50)

# Add a selectbox
selectbox_value = st.selectbox("Pick a color", ["Red", "Green", "Blue"])

# Add a button
if st.button("Click Me"):
    st.write(f"You picked number {slider_value} and color {selectbox_value}.")

# Display a chart
st.write("Here's a random chart:")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
