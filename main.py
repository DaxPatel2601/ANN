import pandas as pd
import numpy as np
import streamlit as st


with st.form("form1"):
    user_input=st.text_input("Name")
    submit=st.form_submit_button("Submit")
    
    if submit:
        st.write(user_input)
        
        