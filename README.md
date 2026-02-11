Link to the streamlit app for online use : https://mri-app-hup3qtd0ws8.streamlit.app/
# MRI Brain Tumor Classification

This project provides a web application for classifying MRI brain scans into four categories: glioma tumor, meningioma tumor, no tumor, and pituitary tumor. It uses a pre-trained EfficientNetB3 model to analyze uploaded MRI images and predict the tumor type.

## Features

- **Image Classification**: Upload MRI scan images (JPG, JPEG, PNG) and get instant classification results.
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience.
- **Pre-trained Model**: Utilizes EfficientNetB3, a state-of-the-art convolutional neural network for image classification.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Khogeta/MRI_classification.git
   cd MRI_classification
   ```

2. **Install Git LFS** (if not already installed):
   - Download and install Git LFS from [https://git-lfs.github.com/](https://git-lfs.github.com/).
   - Initialize Git LFS in the repository:
     ```bash
     git lfs install
     git lfs pull
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:
   - streamlit
   - tensorflow
   - pillow
   - numpy

## Usage

1. **Run the Application**:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the App**:
   - Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. **Classify an Image**:
   - Upload an MRI scan image using the file uploader.
   - Click the "Classify" button to get the prediction.

## Model Details

- **Model File**: `EfficientNetB3.keras` (125 MB, managed with Git LFS).
- **Input Size**: Images are resized to 300x300 pixels.
- **Preprocessing**: Uses EfficientNet's built-in preprocessing.
- **Classes**: glioma_tumor, meningioma_tumor, no_tumor, pituitary_tumor.

## Training Notebook

The `notebook.ipynb` contains the code used to train the EfficientNetB3 model on a dataset of MRI brain tumor images. It includes data loading, preprocessing, model training, and evaluation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application is for educational and research purposes only. It is not intended for medical diagnosis. Always consult with qualified medical professionals for health-related decisions.
