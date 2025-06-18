import streamlit as st
from PIL import Image
import os
from classifier import classifier
import tempfile

st.title("Dog Breed Classifier")

# Model selection
def get_model_names():
    return ["alexnet", "resnet", "vgg"]

model_name = st.selectbox("Choose a model", get_model_names())

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")
    # Save uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        image.save(tmp_file.name)
        tmp_path = tmp_file.name
    # Call classifier function
    result = classifier(tmp_path, model_name)
    st.success(f"Prediction: {result}") 