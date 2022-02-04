import streamlit as st
import pandas as pd
from multi_app import *
from apps import home, process,demo,limit

st.set_page_config(layout="wide")

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Process", process.app)
app.add_app("Demo", demo.app)
app.add_app("Limitation & Future Direction", limit.app)
app.run()









