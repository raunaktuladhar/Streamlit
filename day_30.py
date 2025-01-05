# The Art of Creating Streamlit Apps
'''Today's Day 30 of the #30DaysOfStreamlit challenge. Congratulations on making this far in the challenge.

In this tutorial, we're going to put our newfound knowledge from this learning challenge to create Streamlit apps 
to solve real-world problem.

Real-world problem
As a content creator, having access to thumbnail images from YouTube videos are useful resources for social 
promotion and content creation.

Let's figure out how we're going to tackle this problem and build a Streamlit app.

Solution
Today, we're going to build yt-img-app, which is a Streamlit app that can extract thumbnail images from 
YouTube videos.

In a nutshell, here's the 3 simple steps that we want the Streamlit app to do:

Accept a YouTube URL as input from users
Perform text processing of the URL to extract the unique YouTube video ID
Use the YouTube video ID as an input to a custom function that retrieves and displays the thumbnail 
image from YouTube videos

Instructions
To get started in using the Streamlit app, copy and paste a YouTube URL into the input text box.'''

import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')