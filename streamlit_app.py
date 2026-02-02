import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input

# Define the labels
labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

# Cache the model to avoid reloading
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('EfficientNetB3.keras')
    return model

model = load_model()

st.title("MRI Scan Classification")
st.write("Upload an MRI scan image to classify it into one of the tumor categories.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Confirm button
    if st.button('Classify'):
        # Preprocess the image
        image = image.resize((300, 300))
        image_array = np.array(image)
        image_array = preprocess_input(image_array)  # EfficientNet preprocessing
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
        
        # Predict
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        predicted_label = labels[predicted_class]
        
        st.success(f"The predicted category is: **{predicted_label}**")
