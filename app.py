# Dependancies
import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Database Setup
cwd = os.getcwd()
f = "Assets\\Data_Files"
file = "data.json"
path = os.path.join(cwd, f, file)


# Home route
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

# All-Data route
@app.route("/all-data")
def names():

    # Use Pandas to read in data
    df = pd.read_json(path)

    data = {
        'Name': df['Name'].values.tolist(),
        'Year': df['Year'].values.tolist(),
        'Season': df['Season'].values.tolist(),
        'Wins': df['Wins'].values.tolist(),
        'Passing Yards': df['Passing Yards'].values.tolist(),
        'TD Passes': df['TD Passes'].values.tolist(),
    }

    return jsonify(data)

# All-Data route
@app.route("/json-data")
def json():

    # Use Pandas to read in data
    df = pd.read_json(path)

    data = []
    # data = {
    #     'Name': df['Name'].values.tolist(),
    #     'Year': df['Year'].values.tolist(),
    #     'Season': df['Season'].values.tolist(),
    #     'Wins': df['Wins'].values.tolist(),
    #     'Passing Yards': df['Passing Yards'].values.tolist(),
    #     'TD Passes': df['TD Passes'].values.tolist(),
    # }
    for d in df:
        qb_dict = {}
        qb_dict["Name"] = df['Name']
        qb_dict["Year"] = df['Year']
        qb_dict["Season"] = df['Season']
        qb_dict["Wins"] = df['Wins']
        qb_dict["Passing_Yards"] = df['Passing Yards']
        qb_dict["TD_Passes"] = df['TD Passes']
        data.append(qb_dict)

    return jsonify(data)


if __name__ == "__main__":
    app.run()
