# day 10

# st.selectbox
'''st.selectbox allows the display of a select widget.'''

import streamlit as st
st.header("st.selectbox")

option = st.selectbox(
    "What is your favourite colour?",
    ('Blue', 'Red', 'Green')
)

st.write("Your favourite color is ", option)

# day 11

# st.multiselect
# st.multiselect displays a multiselect widget.

st.header("st.multiselect")

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red']
)

st.write("You selected: ", options)