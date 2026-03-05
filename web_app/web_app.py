import streamlit as st
import requests

API_URL = "https://ba47bd8d2de3.ngrok-free.app/predict"

st.title("Audio Emotion Classification ")

audio_file = st.file_uploader("Upload an audio file", type=["wav","mp3"])

if audio_file is not None:
    st.audio(audio_file, format='audio/wav')

    if st.button("Predict Emotion"):
        files = {"file": (audio_file.name, audio_file, "audio/wav")}
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            result = response.json()
            pred_class = result.get("predicted_class", "Error")
            confidence = result.get("confidence", None)

            if confidence is not None:
                confidence_percent = round(confidence * 100, 2)
                st.success(f"Predicted Emotion: **{pred_class}** ({confidence_percent}% confident)")
            else:
                st.success(f"Predicted Emotion: **{pred_class}**")
        else:
            st.error("Prediction failed. Try again!")
