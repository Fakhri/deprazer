import json
import datetime
import importlib

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from backend.service import get_verbose_area_depression_level, get_user_depression_level
from flask import Blueprint, request, json, render_template, request
from flask_cors import CORS

controller = Blueprint("backend", __name__)
CORS(controller)

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
one_week = datetime.timedelta(weeks=1)

@controller.route("/")
def index():
#   todo
#   state_data = [
#     get_verbose_area_depression_level('Alabama', today - one_week),
#     get_verbose_area_depression_level('Alaska', today - one_week),
#     ...
#   ]

#   sample data - start
  state_data = [
    {"state": "Alabama", "depression": 0, "keywords": ""},
    {"state": "Alaska", "depression": 0,  "keywords": ""},
    {"state": "Arkansas", "depression": 0,  "keywords": ""},
    {"state": "Arizona", "depression": 0.7,  "keywords": "depressed, anxious, sick, bad, hopeless"},
    {"state": "California", "depression": 0.9,  "keywords": "hopeless, sick, work, weather, suffer"},
    {"state": "Colorado", "depression": 0,  "keywords": ""},
    {"state": "Connecticut", "depression": 0,  "keywords": ""},
    {"state": "Delaware", "depression": 0,  "keywords": ""},
    {"state": "Florida", "depression": 0,  "keywords": ""},
    {"state": "Georgia", "depression": 0,  "keywords": ""},
    {"state": "Hawaii", "depression": 0,  "keywords": ""},
    {"state": "Iowa", "depression": 0,  "keywords": ""},
    {"state": "Idaho", "depression": 0.5,  "keywords": "crime, depressed, tired, bad, cloud"},
    {"state": "Illinois", "depression": 0,  "keywords": ""},
    {"state": "Indiana", "depression": 0,  "keywords": ""},
    {"state": "Kansas", "depression": 0,  "keywords": ""},
    {"state": "Kentucky", "depression": 0,  "keywords": ""},
    {"state": "Louisiana", "depression": 0,  "keywords": ""},
    {"state": "Maine", "depression": 0,  "keywords": ""},
    {"state": "Maryland", "depression": 0,  "keywords": ""},
    {"state": "Massachusetts", "depression": 0,  "keywords": ""},
    {"state": "Michigan", "depression": 0,  "keywords": ""},
    {"state": "Minnesota", "depression": 0,  "keywords": ""},
    {"state": "Missouri", "depression": 0,  "keywords": ""},
    {"state": "Mississippi", "depression": 0,  "keywords": ""},
    {"state": "Montana", "depression": 0,  "keywords": ""},
    {"state": "North Carolina", "depression": 0,  "keywords": ""},
    {"state": "North Dakota", "depression": 0,  "keywords": ""},
    {"state": "Nebraska", "depression": 0,  "keywords": ""},
    {"state": "New Hampshire", "depression": 0,  "keywords": ""},
    {"state": "New Jersey", "depression": 0,  "keywords": ""},
    {"state": "New Mexico", "depression": 0,  "keywords": ""},
    {"state": "Nevada", "depression": 0.4,  "keywords": "stress, sick, down, angry, tired"},
    {"state": "New York", "depression": 0,  "keywords": ""},
    {"state": "Ohio", "depression": 0,  "keywords": ""},
    {"state": "Oklahoma", "depression": 0,  "keywords": ""},
    {"state": "Oregon", "depression": 0.5,  "keywords": "bad, lost, depressed, anxious, old"},
    {"state": "Pennsylvania", "depression": 0,  "keywords": ""},
    {"state": "Rhode Island", "depression": 0,  "keywords": ""},
    {"state": "South Carolina", "depression": 0,  "keywords": ""},
    {"state": "South Dakota", "depression": 0,  "keywords": ""},
    {"state": "Tennessee", "depression": 0,  "keywords": ""},
    {"state": "Texas", "depression": 0,  "keywords": ""},
    {"state": "Utah", "depression": 0,  "keywords": ""},
    {"state": "Virginia", "depression": 0,  "keywords": ""},
    {"state": "Vermont", "depression": 0,  "keywords": ""},
    {"state": "Washington", "depression": 0.2,  "keywords": "job, work, tired, stress, sick"},
    {"state": "Wisconsin", "depression": 0,  "keywords": ""},
    {"state": "West Virginia", "depression": 0,  "keywords": ""},
    {"state": "Wyoming", "depression": 0,  "keywords": ""}
  ]
#   sample data - end

  return render_template('index.html', data=json.dumps(state_data), cityData=json.dumps("US"))
 
@controller.route("/detail/California")
def region():
#   todo
#   state_data = [
#     get_verbose_area_depression_level('Alabama', today - one_week),
#     get_verbose_area_depression_level('Alaska', today - one_week),
#     ...
#   ]

#   sample data - start
  california_data = [
    {"state": "Santa Clara", "depression": 0.9,  "keywords": "job, work, tired, stress, sick"},
    {"state": "Stanislaus", "depression": 0.6,  "keywords": "hopeless, sick, work, weather, suffer"},
    {"state": "Merced", "depression": 0.8,  "keywords": "bad, lost, depressed, anxious, old"},
    {"state": "San Benito", "depression": 0.4,  "keywords": "crime, depressed, tired, bad, cloud"},
    {"state": "Fresno", "depression": 0.6,  "keywords": "stress, sick, down, angry, tired"}
  ]
#   sample data - end

  return render_template('index.html', data=json.dumps(california_data), cityData=json.dumps("California"))

@controller.route("/personal", methods=['GET', 'POST'])
def personal():
    if request.method == 'POST': 
      twitter_account = request.form['twitter_account']
      user_depression_level = get_user_depression_level(twitter_account, today - one_week)
      print(user_depression_level)
      result = sum(user_depression_level["value"]) / len(user_depression_level["value"]) * 100
      return render_template("personal.html", input=twitter_account, result=round(result, 2))
    else:
      return render_template("personal.html")
    
