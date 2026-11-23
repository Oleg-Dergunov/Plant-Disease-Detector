"""
Temporary stand-in for Oleg's predict.py.
Follows the agreed interface contract:
predict(image) -> {"label", "confidence", "status"}
Delete this file when the real model is ready.
"""
import random

SAMPLE_LABELS = [
    "Tomato___Early_blight",
    "Apple___healthy",
    "Corn___Common_rust",
    "Blueberry___healthy",
]

RECOGNITION_ONLY = ["Blueberry", "Raspberry", "Soybean", "Orange", "Squash"]
THRESHOLD = 0.6


def predict(image):
    label = random.choice(SAMPLE_LABELS)
    confidence = round(random.uniform(0.4, 0.99), 2)
    crop = label.split("___")[0]

    if confidence < THRESHOLD:
        status = "low_confidence"
    elif crop in RECOGNITION_ONLY:
        status = "recognition_only"
    else:
        status = "ok"

    return {"label": label, "confidence": confidence, "status": status}