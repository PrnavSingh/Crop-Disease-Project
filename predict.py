import cv2
import numpy as np
import joblib
from skimage.feature import hog
from PIL import Image

# -------------------------------
# Load Required Files
# -------------------------------
MODEL_PATH = "models/best_model.pkl"
LABELS_PATH = "models/labels.pkl"
SCALER_PATH = "models/scaler.pkl"

def load_model():
    """Load model, labels, and scaler."""
    try:
        model = joblib.load(MODEL_PATH)
        labels = joblib.load(LABELS_PATH)  # This is a LabelEncoder
        scaler = joblib.load(SCALER_PATH)
        return model, labels, scaler
    except Exception as e:
        raise RuntimeError(f"Error loading model files: {str(e)}")


# -------------------------------
# Preprocessing Function
# -------------------------------
def preprocess_image(image_path):
    """
    Loads the image, converts to grayscale, resizes,
    extracts HOG features, and scales them.
    """
    try:
        # Load image
        img = Image.open(image_path).convert("RGB")
        img = np.array(img)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Resize to standard dimensions
        resized = cv2.resize(gray, (128, 128))

        # Extract HOG features
        features = hog(
            resized,
            orientations=9,
            pixels_per_cell=(8, 8),
            cells_per_block=(2, 2),
            block_norm='L2-Hys',
            visualize=False
        )

        return features.reshape(1, -1)

    except Exception as e:
        raise ValueError(f"Error preprocessing image: {str(e)}")


# -------------------------------
# Main Prediction Function
# -------------------------------
def predict(image_path):
    """
    Full prediction pipeline:
    - Load model + scaler + LabelEncoder
    - Preprocess image
    - Scale features
    - Predict label index
    - Convert index → actual label
    """
    # Load ML components
    model, labels, scaler = load_model()

    # Preprocess image
    features = preprocess_image(image_path)

    # Scale features
    scaled_features = scaler.transform(features)

    # Predict index
    prediction_idx = model.predict(scaled_features)[0]

    # Convert index → disease name (LabelEncoder)
    disease_name = labels.inverse_transform([prediction_idx])[0]

    return disease_name.lower()   # cleaner output
