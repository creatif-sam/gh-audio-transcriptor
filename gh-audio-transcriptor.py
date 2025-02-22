import streamlit as st
import whisper
import os
import tempfile

# Title of the Streamlit app
st.title("🎙️ Whisper Transcription App - Ghanaian English")

# Upload audio file
audio_file = st.file_uploader("📤 Upload an audio file (MP3, WAV, etc.)", type=["mp3", "wav", "m4a"])

# Load Whisper model
@st.cache_resource  # Caches the model to avoid reloading
def load_model():
    return whisper.load_model("medium")  # Options: tiny, base, small, medium, large

model = load_model()

if audio_file is not None:
    # Save the uploaded file to a temporary location
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, audio_file.name)

    with open(file_path, "wb") as f:
        f.write(audio_file.read())

    # Display the uploaded file
    st.audio(file_path, format="audio/mp3")

    # Transcribe the audio
    st.write("⏳ Transcribing audio... Please wait...")
    result = model.transcribe(file_path)

    # Show the transcription result
    st.success("✅ Transcription Completed!")
    st.text_area("📝 Transcription:", result["text"], height=300)

    # Option to download transcription
    st.download_button("⬇️ Download Transcription", result["text"], file_name="transcription.txt")

