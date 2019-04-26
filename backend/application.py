import os
from flask import Flask, render_template

template_dir = os.path.abspath('./frontend')
application = Flask(__name__, template_folder=template_dir)

@application.route("/")
def home():
  return render_template('home.html')
 
if __name__ == "__main__":
    application.run(debug=True)