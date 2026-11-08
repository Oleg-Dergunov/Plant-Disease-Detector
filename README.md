# Plant Disease Detector

### Overview
A Flask web application that recognises one of 14 crops and, where possible, its disease from a photo of a leaf. It uses a MobileNetV3-Large model fine-tuned on the PlantVillage dataset (38 classes). Users can rate results and submit photos that experts review, building a more varied dataset for future work.

Research Project (BSC30926A Computing)
Authors: Oleg Dergunov (76522), Nathan Santos (77304)
Supervisor: Rod Haanappel

### 🚀 Planned Features

🔲 Crop and disease recognition from a leaf photo
🔲 Confidence score and top-3 predictions
🔲 "Not sure" message for low-confidence results
🔲 Sign-in with Google and Facebook (OAuth 2.0)
🔲 Ratings and reviews of results
🔲 Photo submission with consent and metadata removal
🔲 Roles:
- User — Check leaf photos, rate results, submit photos
- Expert — Review submitted photos, approve or reject, correct labels
- Administrator — Manage accounts, roles and statistics

### 🌱 Supported Crops

Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato.
For Blueberry, Raspberry, Soybean, Orange and Squash, only the crop is recognised (no disease detection).

### 📂 Project Structure

The project is split into two parts:

plant-disease-detector/
│
├── ml/          # Machine learning: data preparation, training, evaluation
├── web/         # Flask web application
├── models/      # Exported model file (not stored in Git)
├── config/      # Shared settings (confidence threshold, etc.)
└── docs/        # Interface between the model and the app

### 🛠 Technologies Used
- Python 3.x
- PyTorch (MobileNetV3-Large)
- scikit-learn, Matplotlib
- Google Colab (training)
- Flask
- SQLite
- HTML, CSS, JavaScript

### 👥 Team
- Oleg Dergunov — Machine learning and integration
- Nathan Santos — Web application (backend and frontend)

### 🔧 Installation & Usage
Python 3 is required.

```bash
git clone https://github.com/Oleg-Dergunov/Plant-Disease-Detector.git
cd plant-disease-detector
```

Setup and run instructions will be added as the project develops.

### 📚 Dataset
PlantVillage — Hughes & Salathé (2015), https://github.com/spMohanty/PlantVillage-Dataset
