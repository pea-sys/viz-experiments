#conda activate stenv
#streamlit run streamlit_app.py

import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')