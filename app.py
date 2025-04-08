import streamlit as st
import pandas as pd
import numpy as np

## Title of the application 
st.title("Hello streamlit!")
st.subheader("This is a subheader")

## display a text
st.write("this is a simple text")

## create a simple dataframe
df = pd.DataFrame(
    {
        "a": [1, 2, 3, 4],
        "b": [5, 6, 7, 8],
        "c": [9, 10, 11, 12],
    }
)
## display a dataframe 
st.write("Here is the dataframe")
st.write(df)

## create a line chart 

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["a", "b", "c"]
)
st.write("Here is a line chart")
st.line_chart(chart_data) 
