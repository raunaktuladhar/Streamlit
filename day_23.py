import streamlit as st

st.title('st.query_params')

with st.expander('About this app'):
    st.write("`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown(''' 
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')

# 2. Contents of st.query_params
st.header('2. Contents of st.query_params')
params = st.query_params  # Use the recommended method to access query params
st.write(params)

# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

# Safely access query parameters using .get()
firstname = params.get('firstname', [''])[0]  # Default to an empty string if 'firstname' is missing
surname = params.get('surname', [''])[0]      # Default to an empty string if 'surname' is missing

st.write(f'Hello **{firstname} {surname}**, how are you?')
