from flask import Flask
from backend.controller import controller

application = Flask(__name__, static_folder="frontend/static", template_folder="frontend/template")
application.register_blueprint(controller)

if __name__ == "__main__":
    application.run(debug=True)
