# Dog Breed Classifier

Classify dog breeds from images using PyTorch models. Includes a Streamlit web app for easy image upload and instant predictions.

## 📽️ Demo Video

[![Watch the demo](https://img.youtube.com/vi/OBEkP6gD49Q/0.jpg)](https://youtu.be/OBEkP6gD49Q)


## Features
- Upload an image and get the predicted dog breed instantly
- Choose between ResNet, AlexNet, and VGG pre-trained models
- Powered by PyTorch and Streamlit
- Easily extensible for other image classification tasks

---

## Demo
Run locally and open your browser to `http://localhost:8501` to use the web app.

Or try the live version here: [https://dog-breed-classifier-ml.streamlit.app/](https://dog-breed-classifier-ml.streamlit.app/)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aakanksha-singh-hub/dog-breed-classifier.git
   cd dog-breed-classifier
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

---

## Usage
- Open the app in your browser (usually at `http://localhost:8501`)
- Upload a dog image (JPG/PNG)
- Select a model (ResNet, AlexNet, VGG)
- View the predicted breed

---

## File Structure
```
├── app.py                  # Streamlit web app
├── classifier.py           # Core image classification logic (PyTorch)
├── classify_images.py      # Batch classification utility
├── pet_images/             # Sample images for testing
├── uploaded_images/        # Folder for user-uploaded images
├── dognames.txt            # List of valid dog breed names
├── imagenet1000_clsid_to_human.txt # ImageNet class label mapping
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- PyTorch and TorchVision for pre-trained models
- Streamlit for the web app framework
- [ImageNet](http://www.image-net.org/) for the dataset and class labels

