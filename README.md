# 🎵 Audio Emotion Classification

A deep learning project for **audio emotion recognition** using Mel spectrograms and CNN (VGG16). Upload an audio file to predict the speaker's emotion in real-time via a Streamlit interface.

---

## 🛠️ Features

- Converts audio files into **Mel spectrograms** for model input.
- Trains a **CNN (VGG16)** on emotional speech data (TESS dataset).
- Serves a **Flask API** to make predictions.
- Interactive **Streamlit frontend** to upload audio and see predictions.
- Provides **confidence score** along with predicted emotion.

---

## 🎯 Technologies Used

- Python, NumPy, OpenCV
- Librosa for audio processing
- TensorFlow / Keras (VGG16 CNN)
- Flask for API backend
- Streamlit for web interface
- Ngrok for public API tunneling
- Mel Spectrograms for feature extraction


```
## 🗂️ Project Structure


audio-emotion-classification/
│
├─ Colab_Notebooks/
│ └─ VGG16_transfer_learning.ipynb 
│
├─ Model/
│ └─ CNN-Mel-Spectrogram.h5 
│
├─ api/
│ └─ Prediction_Backend.ipynb # Flask API for prediction
│
├─ web_app/
│ └─ app.py # Streamlit frontend
│
└─ README.md
```

---

## 🏗️ How to Run

### 1. Clone the repo

git clone https://github.com/hamza-amjad10/audio-emotion-classification.git


2. Run Flask API

cd api

Prediction_Backend.ipynb

Your API will run locally at http://127.0.0.1:5000/predict

Use Ngrok if you want a public URL.

3. Run Streamlit App
cd web_app
streamlit run web_app.py

Upload an audio file (.wav or .mp3) and click Predict Emotion.

The app will show predicted emotion and confidence.

🧠 Dataset

TESS Toronto Emotional Speech Set

14 emotion classes including happy, sad, angry, neutral, fear, surprise, and disgust.

📈 Model Performance

Achieved >97% training accuracy and ~100% validation accuracy.

Confusion matrix and classification report available in the Colab notebook.

💡 Future Improvements

Support longer audio files with dynamic padding.

Add more real-world datasets for better generalization.

Deploy as a fully hosted web app with FastAPI + Streamlit.

👨‍💻 Author

Hamza Amjad – LinkedIn
