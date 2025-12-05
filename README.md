# 🌾 Edge-Optimized Crop Disease Predictor

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-ff4b4b.svg)
![Scikit-Learn](https://img.shields.io/badge/Sklearn-1.3+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Prototype-yellow.svg)

> **A lightweight, offline-first AI tool for detecting crop diseases in Potato and Rice using HOG features and Classical Machine Learning.**

---

## 📖 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Dataset Details](#-dataset-details)
- [Performance Metrics](#-performance-metrics)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Future Roadmap](#-future-roadmap)
- [License](#-license)

---

## 💡 About The Project

Modern agriculture faces a critical challenge: **Internet connectivity in remote fields is often poor or non-existent.** Most existing crop disease detection apps rely on heavy Deep Learning models (like ResNet or VGG) that require cloud servers and high-speed internet to function.

**This project is different.** We use **Histogram of Oriented Gradients (HOG)** for feature extraction combined with a **Support Vector Machine (SVM)** classifier. This "Lightweight AI" approach reduces the model size to **<50 MB** and allows the entire system to run **offline** on low-end devices without any internet connection.

### 🎯 Objective
To provide farmers with an instant, "Lab-to-Land" diagnostic tool that not only detects the disease but also recommends government-approved chemical and organic treatments.

---

## ✨ Key Features

* **🚀 100% Offline Inference:** Runs entirely on the local CPU. No API calls or cloud latency.
* **⚡ Blazing Fast:** Inference time is **<0.1 seconds** per image (10x faster than CNNs).
* **🧠 Explainable Features:** Uses texture and shape analysis (HOG) rather than "black box" pixel processing.
* **💊 Actionable Remediation:** Instantly maps the detected disease to specific medicines (e.g., *Mancozeb* for Late Blight).
* **📱 Edge-Ready:** Designed to run on entry-level hardware (Raspberry Pi, old laptops, budget phones).

---

## 🛠 Tech Stack

* **Language:** Python 3.9
* **Frontend:** [Streamlit](https://streamlit.io/) (Web UI)
* **Image Processing:** OpenCV, Scikit-Image (`skimage.feature.hog`)
* **Machine Learning:** Scikit-Learn (SVM, Random Forest)
* **Model Serialization:** Joblib

---

## 📊 Dataset Details

The model was trained on a balanced dataset of **4,200 images** aggregated from:
1.  **PlantVillage Dataset** (Potato classes)
2.  **Kaggle / UCI Repository** (Rice classes)

| Crop | Disease Classes |
| :--- | :--- |
| **Potato** | Early Blight, Late Blight, Healthy |
| **Rice** | Leaf Blast, Brown Spot, Hispa, Healthy |

> **Note:** Images were preprocessed using Grayscale conversion and resized to `128x128` pixels to optimize for HOG feature extraction.

---

## 📈 Performance Metrics

| Metric | Our Model (HOG + SVM) | Standard CNN (ResNet-50) |
| :--- | :--- | :--- |
| **Model Size** | **~45 MB** | > 100 MB |
| **Inference Time** | **0.05s** | ~0.5s |
| **Accuracy** | **~92%** | ~95% |
| **Dependency** | CPU Only | Requires GPU |

*While Deep Learning offers slightly higher accuracy, our model offers superior speed and portability for rural deployment.*

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites
* Python 3.8 or higher installed.
* Git installed.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/crop-disease-predictor.git](https://github.com/yourusername/crop-disease-predictor.git)
    cd crop-disease-predictor
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

```bash
streamlit run app.py

crop-disease-predictor/
│
├── 🟩 app.py               # Main Streamlit Application (Frontend)
├── 🟦 predict.py           # ML Pipeline (HOG extraction + Inference)
│
├── 🟪 models/              # Serialized Model Artifacts
│   ├── best_model.pkl      # Trained SVM Classifier
│   ├── scaler.pkl          # StandardScaler object
│   └── labels.pkl          # LabelEncoder (0 -> "Late_Blight")
│
├── 🟧 requirements.txt     # Python Dependencies
├── 🟫 README.md            # Project Documentation
└── ⬜ temp_uploaded.jpg    # Temporary storage for user upload
