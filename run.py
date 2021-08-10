
from flask import Flask
from app import api_bp


def create_app(app_name):
    app = Flask(__name__)
    app.config.from_object(app_name)

    app.register_blueprint(api_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)