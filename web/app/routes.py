from flask import Blueprint, render_template, request
from PIL import Image, UnidentifiedImageError

from .fake_predict import predict

main = Blueprint("main", __name__)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/predict", methods=["POST"])
def upload():
    file = request.files.get("photo")

    if not file or file.filename == "":
        return render_template("index.html", error="Please choose a photo.")

    if not allowed_file(file.filename):
        return render_template("index.html", error="Only JPG and PNG photos are allowed.")

    try:
        image = Image.open(file.stream).convert("RGB")
    except (UnidentifiedImageError, OSError):
        return render_template("index.html", error="This file is not a valid image.")

    result = predict(image)
    crop, _, disease = result["label"].partition("___")

    return render_template(
        "result.html",
        result=result,
        crop=crop,
        disease=disease.replace("_", " "),
    )


@main.app_errorhandler(413)
def file_too_large(error):
    return render_template("index.html", error="The photo is too large (max 5 MB)."), 413