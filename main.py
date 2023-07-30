import streamlit as st
from PyPDF2 import PdfReader
from elevenlabs import generate, set_api_key
st.title("The Voich")

# funtion to generate text to speech
def generate_voice(text):
  set_api_key('5bde68c411f0c6779da15eb8d76ca7b1')
  audio = generate(
         text=text,
         voice="Bella",
         model='eleven_multilingual_v1'
    )
  st.audio(audio)
# uploading of file
uploaded_file = st.file_uploader("Choose a file" , type = 'pdf')
# if the file object is not none , then extract text from it
if uploaded_file is not None:
  reader = PdfReader(uploaded_file)
  page = reader.pages[5]
  text = page.extract_text()
  st.write(text)
  # pass the text to elevenlabs to show its magic
  st.button('Read' , on_click = generate_voice(text))













  








