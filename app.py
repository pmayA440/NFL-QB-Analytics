# Dependancies
import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Database Setup
cwd = os.getcwd()
f = "Assets\\Data_Files"
file = "Cleaned_QB_data_groups.csv"
path = os.path.join(cwd, f, file)


# Home route
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

# # All-Data route
# @app.route("/all-data")
# def names():

#     # Use Pandas to read in data
#     df = pd.read_csv(path)

#     # Return a list of the data
#     data = {
#         'Name': df['Name'].values.tolist(),
#         'Year': df['Year'].values.tolist(),
#         'Season': df['Season'].values.tolist(),
#         'Week': df['Week'].values.tolist(),
#         'Outcome': df['Outcome'].values.tolist(),
#         'Completion Percentage': df['Completion Percentage'].values.tolist(),
#         'Passing Yards': df['Passing Yards'].values.tolist(),
#         'TD Passes': df['TD Passes'].values.tolist(),
#     }
#     return jsonify(data)

# Group route
@app.route("/groups")
def sums():

    # # Use Pandas to read in data
    df = pd.read_csv(path)

    # Return a list of the data
    data = {
        'Year': df['Year'].values.todict(),
        'Name': df['Name'].values.todict(),
        'Season': df['Season'].values.todict(),
        'Passing Yards': df['Passing Yards'].values.todict(),
        'TD Passes': df['TD Passes'].values.todict(),
        'Wins': df['Wins'].values.todict(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
