import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_audio(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")

# Streamlit app
st.title("Transcript to Audio Converter")

# Text input
transcript = st.text_area("Enter your transcript:")

# Language selection
lang = st.selectbox("Select language:", ('en', 'es', 'fr', 'de', 'it'))

# Convert button
if st.button("Convert to Audio"):
    if transcript:
        text_to_audio(transcript, lang)
        # Provide a download link
        with open("output.mp3", "rb") as file:
            st.download_button(
                label="Download Audio",
                data=file,
                file_name="output.mp3",
                mime="audio/mpeg"
            )
    else:
        st.warning("Please enter a transcript to convert.")

# Remove the audio file after download
if os.path.exists("output.mp3"):
    os.remove("output.mp3")
