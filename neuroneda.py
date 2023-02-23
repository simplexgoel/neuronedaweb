import streamlit as st
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="Neuron EDA, Inc.", page_icon=":brain:")

# Load neuron image
neuron_img = Image.open("neuron.png")

# Display neuron image
st.image(neuron_img, caption="Image of a neuron", use_column_width=True)

# Display company name and under construction sign
st.write("# Neuron EDA, Inc.")
st.write("## Under Construction :construction:")

