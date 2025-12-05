import streamlit as st
import numpy as np
import cv2
from PIL import Image
from predict import predict  # Import your prediction function

st.set_page_config(page_title="Crop Disease Predictor")


# ---------------------------------------------------------
# BEAUTIFUL CUSTOM UI (BACKGROUND + CARD DESIGN + STYLING)
# ---------------------------------------------------------
page_bg_img = '''
<style>

/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Soft white overlay for readability */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255,255,255,0.65);
    z-index: -1;
}

/* Center main content */
.block-container {
    background-color: rgba(255, 255, 255, 0.92) !important;
    padding: 2rem 3rem;
    border-radius: 20px;
    max-width: 850px;
    margin: auto;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

/* Title styling */
h1 {
    color: #145A32 !important;
    text-align: center;
    font-family: 'Segoe UI';
    font-weight: 900;
    font-size: 42px !important;
}

/* Subheaders */
h2, h3 {
    color: #1D8348 !important;
    font-family: 'Segoe UI';
}

/* Styled prediction box */
.prediction-box {
    background-color: #E8F8F5;
    border-left: 6px solid #1ABC9C;
    padding: 15px;
    border-radius: 10px;
    font-size: 20px;
    margin-top: 20px;
}

/* File uploader styling */
.css-1n76uvr {
    background-color: rgba(255,255,255,0.95) !important;
    padding: 1rem;
    border-radius: 12px;
    border: 2px dashed #1ABC9C !important;
}

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
# ---------------------------------------------------------



# -------------------------------
# Disease Information Dictionary
# -------------------------------
DISEASE_INFO = {
    "late_blight": {
        "cause": "Caused by the fungus-like organism *Phytophthora infestans*. It spreads quickly in cool, moist environments.",
        "solution": "Use certified disease-free seeds, ensure proper field drainage, remove infected plants, and spray fungicides like Mancozeb or Metalaxyl."
    },
    "early_blight": {
        "cause": "Caused by the fungus *Alternaria solani*. Often impacts older leaves first.",
        "solution": "Rotate crops, remove plant debris, maintain proper spacing, and apply chlorothalonil or copper-based fungicides."
    },
    "healthy": {
        "cause": "No disease detected.",
        "solution": "Maintain regular irrigation, balanced fertilizers, and monitor leaves weekly to prevent infections."
    },
    "black_rot": {
        "cause": "Caused by the bacterium *Xanthomonas campestris*. Spread through water, insects, and infected soil.",
        "solution": "Use disease-free seeds, avoid overhead irrigation, remove infected leaves, and apply copper-based sprays."
    },
    "brown_spot": {
        "cause": "Caused by the fungus *Bipolaris oryzae*. Common in rice plants grown in nutrient-poor soils.",
        "solution": "Apply nitrogen fertilizer appropriately, remove weeds, improve field drainage, and use fungicides like propiconazole."
    },
    "leaf_blast": {
        "cause": "Caused by the rice blast fungus *Magnaporthe oryzae*. Favors humid and warm conditions.",
        "solution": "Avoid excess nitrogen, maintain good spacing, use resistant rice varieties, and apply tricyclazole fungicide."
    },
    "hispa": {
        "cause": "Caused by rice Hispa beetle (*Dicladispa armigera*). Larvae feed on plant tissue.",
        "solution": "Spray neem oil, avoid overuse of fertilizers, hand-pick adult beetles, or use approved insecticides like chlorpyrifos."
    }
}


# -------------------------------
# Streamlit UI
# -------------------------------
st.markdown("<h1>🌿 Crop Disease Predictor</h1>", unsafe_allow_html=True)
st.write("Upload a leaf image (potato or rice) and get predicted disease, its cause, and solutions for farmers.")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png", "jfif"]
)

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=350)

    # Convert to numpy array
    img_array = np.array(image)

    # Fix color formats
    if img_array.ndim == 2:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
    elif img_array.shape[2] == 4:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)

    # Save temp file
    temp_path = "temp_image.jpg"
    Image.fromarray(img_array).save(temp_path)

    # Spinner for prediction
    with st.spinner("Processing the image... Please wait."):
        try:
            result = predict(temp_path)
        except Exception as e:
            st.error("⚠️ Error while predicting. Check terminal for details.")
            st.code(str(e))
            st.stop()

    # Pretty prediction box
    st.markdown(
        f"""
        <div class="prediction-box">
            🌱 <b>Predicted Disease:</b> {result}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Cause + Solution
    if result in DISEASE_INFO:
        info = DISEASE_INFO[result]

        st.subheader("🦠 Cause of Disease")
        st.write(info["cause"])

        st.subheader("🌾 How to Overcome / Solution for Farmers")
        st.write(info["solution"])
    else:
        st.warning("No details available for this disease.")
