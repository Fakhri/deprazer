import os
import json

from flask import Flask, render_template

template_dir = os.path.abspath('./frontend/template')
static_dir = os.path.abspath('./frontend/static')
application = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# class region():
#     def __init__(self, name, depression, keywords):
#         self.name = name
#         self.depression = depression
#         self.keywords = keywords

@application.route("/")
def home():
  # sample data - start
  data = [
    {"state": "Alabama", "depression": 0.6, "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Alaska", "depression": 0.4,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Arkansas", "depression": 0.9,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Arizona", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "California", "depression": 0.9,  "keywords": "hopeless,anxiety,drug,love,suffer"},
    {"state": "Colorado", "depression": 0,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Connecticut", "depression": 0,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Delaware", "depression": 0.6,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Florida", "depression": 0.7,  "keywords": "depression,anxiety,drug,love,pain"},
    {"state": "Georgia", "depression": 0.4,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Hawaii", "depression": 0.8,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Iowa", "depression": 0.6,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Idaho", "depression": 0.5,  "keywords": "depression,anxiety,anger,love,suffer"},
    {"state": "Illinois", "depression": 0.8,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Indiana", "depression": 0.6,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Kansas", "depression": 0.7,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Kentucky", "depression": 0.4,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Louisiana", "depression": 0.8,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Maine", "depression": 0.8,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Maryland", "depression": 0.5,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Massachusetts", "depression": 0.1,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Michigan", "depression": 0.6,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Minnesota", "depression": 0.1,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Missouri", "depression": 0.1,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Mississippi", "depression": 0.3,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Montana", "depression": 0.1,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "North Carolina", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "North Dakota", "depression": 0.1,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Nebraska", "depression": 0.1,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "New Hampshire", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "New Jersey", "depression": 0.3,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "New Mexico", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Nevada", "depression": 0.4,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "New York", "depression": 0.9,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Ohio", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Oklahoma", "depression": 0.3,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Oregon", "depression": 0.5,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Pennsylvania", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Rhode Island", "depression": 0.6,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "South Carolina", "depression": 0.3,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "South Dakota", "depression": 0.5,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Tennessee", "depression": 1,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Texas", "depression": 0.6,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Utah", "depression": 0.5,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Virginia", "depression": 0.3,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Vermont", "depression": 0.3,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Washington", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Wisconsin", "depression": 0.2,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "West Virginia", "depression": 0.6,  "keywords": "depression,anxiety,drug,love,suffer"},
    {"state": "Wyoming", "depression": 0.1,  "keywords": "depression,anxiety,drug,love,suffer"}
  ]
  # sample data - end

  return render_template('index.html', data=json.dumps(data))
 
if __name__ == "__main__":
    application.run(debug=True)