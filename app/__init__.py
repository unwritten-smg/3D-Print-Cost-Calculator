from flask import Flask
import os

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))
    template_dir = os.path.join(project_root, "templates")
    static_dir = os.path.join(project_root, "static")

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    from app.routes import main
    app.register_blueprint(main)
    return app
