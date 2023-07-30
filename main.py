import streamlit as st
# import pandas as pd
# from io import StringIO
# import base64
from PyPDF2 import PdfReader
# from elevenlabs import set_api_key
# import os
# import requests
# from elevenlabs import generate, play

from elevenlabs import generate, set_api_key
st.title("The Voich")
def generate_voice(text):
  set_api_key('5bde68c411f0c6779da15eb8d76ca7b1')
  audio = generate(
         text=text,
         voice="Bella",
         model='eleven_multilingual_v1'
    )
  st.audio(audio)

uploaded_file = st.file_uploader("Choose a file" , type = 'pdf')
if uploaded_file is not None:
  reader = PdfReader(uploaded_file)
  page = reader.pages[5]
  text = page.extract_text()
  st.write(text)
  st.button('Read' , on_click = generate_voice(text))











  








