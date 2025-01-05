# How to layout your Streamlit app
'''In this tutorial, we're going to use the following commands to layout our Streamlit app:
st.set_page_config(layout="wide") - Displays the contents of the app in wide mode 
(otherwise by default, the contents are encapsulated in a fixed width box.
st.sidebar - Places the widgets or text/image displays in the sidebar.
st.expander - Places text/image displays inside a collapsible container box.
st.columns - Creates a tabular space (or column) within which contents can be placed inside.'''

import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')


# Explaination of 'with'
'''
the with statement is used to create context blocks that manage the scope of certain elements or actions. 
When used with Streamlit components like st.expander(), st.sidebar(), or st.container(), 
it allows you to group multiple Streamlit calls together and organize your app's layout in a more structured way.
'''

