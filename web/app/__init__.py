from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB max upload

    from .routes import main
    app.register_blueprint(main)

    return app