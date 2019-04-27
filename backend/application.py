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
    {"state": "Alabama", "depression": 0.6, "keywords": ""},
    {"state": "Alaska", "depression": 0.4},
    {"state": "Arkansas", "depression": 0.9},
    {"state": "Arizona", "depression": 0.2},
    {"state": "California", "depression": 0.9},
    {"state": "Colorado", "depression": 0},
    {"state": "Connecticut", "depression": 0},
    {"state": "Delaware", "depression": 0.6},
    {"state": "Florida", "depression": 0.7},
    {"state": "Georgia", "depression": 0.4},
    {"state": "Hawaii", "depression": 0.8},
    {"state": "Iowa", "depression": 0.6},
    {"state": "Idaho", "depression": 0.5},
    {"state": "Illinois", "depression": 0.8},
    {"state": "Indiana", "depression": 0.6},
    {"state": "Kansas", "depression": 0.7},
    {"state": "Kentucky", "depression": 0.4},
    {"state": "Louisiana", "depression": 0.8},
    {"state": "Maine", "depression": 0.8},
    {"state": "Maryland", "depression": 0.5},
    {"state": "Massachusetts", "depression": 0.1},
    {"state": "Michigan", "depression": 0.6},
    {"state": "Minnesota", "depression": 0.1},
    {"state": "Missouri", "depression": 0.1},
    {"state": "Mississippi", "depression": 0.3},
    {"state": "Montana", "depression": 0.1},
    {"state": "North Carolina", "depression": 0.2},
    {"state": "North Dakota", "depression": 0.1},
    {"state": "Nebraska", "depression": 0.1},
    {"state": "New Hampshire", "depression": 0.2},
    {"state": "New Jersey", "depression": 0.3},
    {"state": "New Mexico", "depression": 0.2},
    {"state": "Nevada", "depression": 0.4},
    {"state": "New York", "depression": 0.9},
    {"state": "Ohio", "depression": 0.2},
    {"state": "Oklahoma", "depression": 0.3},
    {"state": "Oregon", "depression": 0.5},
    {"state": "Pennsylvania", "depression": 0.2},
    {"state": "Rhode Island", "depression": 0.6},
    {"state": "South Carolina", "depression": 0.3},
    {"state": "South Dakota", "depression": 0.5},
    {"state": "Tennessee", "depression": 1},
    {"state": "Texas", "depression": 0.6},
    {"state": "Utah", "depression": 0.5},
    {"state": "Virginia", "depression": 0.3},
    {"state": "Vermont", "depression": 0.3},
    {"state": "Washington", "depression": 0.2},
    {"state": "Wisconsin", "depression": 0.2},
    {"state": "West Virginia", "depression": 0.6},
    {"state": "Wyoming", "depression": 0.1}
  ]
  # sample data - end

  return render_template('index.html', data=json.dumps(data))
 
if __name__ == "__main__":
    application.run(debug=True)