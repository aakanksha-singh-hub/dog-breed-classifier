import streamlit as st
from PIL import Image
import os
from classifier import classifier
import tempfile

# --- Hero Section ---
st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=100)
st.title("Dog Breed Classifier 🐶")
st.markdown("""
Welcome to the Dog Breed Classifier!  
Upload a photo of a dog, and our AI will predict its breed using state-of-the-art deep learning models (ResNet, AlexNet, VGG).

**How it works:**  
1. Choose a model from the sidebar  
2. Upload a dog image  
3. Get instant predictions!

---
""")

# --- Sidebar for Model Selection ---
st.sidebar.header("Settings")
model_name = st.sidebar.selectbox("Choose a model", ["resnet", "alexnet", "vgg"])

# --- File Uploader ---
st.header("Upload a Dog Image")
st.write("Accepted formats: JPG, JPEG, PNG")
uploaded_file = st.file_uploader("Upload a dog image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your uploaded image", use_column_width=True)
    st.info("Classifying...")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        image.save(tmp_file.name)
        tmp_path = tmp_file.name
    result = classifier(tmp_path, model_name)
    st.success(f"**Prediction:** {result}")

# --- About / Footer ---
st.markdown("""
---
**About:**  
This app uses PyTorch and pre-trained models to identify dog breeds from images.  
Created by [Aakanksha Singh].  
[GitHub Repo](https://github.com/aakanksha-singh-hub/dog-breed-classifier)
""") 