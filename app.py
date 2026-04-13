%%writefile app.py
import streamlit as st
from PIL import Image
import numpy as np

# -------------------------
# Dummy prediction function (replace with your model)
# -------------------------
def predict(image):
    # Example classes
    classes = ["Healthy", "Early Blight", "Late Blight"]
    
    # Random prediction (REPLACE THIS WITH MODEL)
    probs = np.random.rand(len(classes))
    probs = probs / probs.sum()
    
    predicted_class = classes[np.argmax(probs)]
    confidence = np.max(probs) * 100
    
    return predicted_class, confidence, probs

# -------------------------
# UI
# -------------------------
st.set_page_config(page_title="Plant Disease Detector", layout="centered")

st.title("🌿 Plant Disease Detection System")

uploaded_file = st.file_uploader("📤 Upload a leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    
    st.image(image, caption="📸 Uploaded Image", use_column_width=True)
    
    st.write("🔍 Analyzing...")
    
    # Prediction
    disease, confidence, probs = predict(image)
    
    st.subheader("🧾 Result")
    
    # Status
    if disease == "Healthy":
        st.success("🌱 Status: Healthy")
    else:
        st.error("⚠️ Status: Diseased")
    
    # Disease name
    st.write(f"**🦠 Disease:** {disease}")
    
    # Confidence
    st.write(f"**📊 Confidence:** {confidence:.2f}%")
    
    # Progress bar
    st.progress(int(confidence))
    
    # Probability breakdown
    st.subheader("📈 All Class Probabilities")
    
    classes = ["Healthy", "Early Blight", "Late Blight"]
    for i in range(len(classes)):
        st.write(f"{classes[i]}: {probs[i]*100:.2f}%")
