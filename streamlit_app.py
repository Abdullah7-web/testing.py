import pandas as pd
import numpy as np
#import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st



df = sns.load_dataset("Titanic")

df.info()

st.title("TESTING")
st.write("This app is solely based on testing, I'm facing an issue with deployment, Creating other app to re-check the concern.")


st.bar_chart(df, x="embark_town", y="alive")

df.info()

fig = px.treemap(df, path=["who", "survived"])
st.plotly_chart(fig)

