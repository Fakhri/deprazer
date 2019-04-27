import os
from flask import Flask, render_template

template_dir = os.path.abspath('./frontend/template')
static_dir = os.path.abspath('./frontend/static')
application = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@application.route("/")
def home():
  return render_template('index.html')
 
if __name__ == "__main__":
    application.run(debug=True)