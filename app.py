# Dependancies
import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Database Setup
file = "C:/Users/Teresa Barajas/Anaconda/Anaconda3/envs/NFL-QB-Analytics/Assets/Data_Files/Cleaned_QB_data_groups.csv"

# Home route
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/years")
def names():
    """Return a list of years."""

    df = pd.read_csv(file)

    # Return a list of the column names (sample names)
    return jsonify(list((df.Year)))


@app.route("/metadata/<year>")
def sample_metadata(year):
    """Return the MetaData for a given year."""
    df = pd.read_csv(file)

    results = df.loc[df['Year'] == int(year)]

    # Create a dictionary entry for each row of metadata information
    data = {
        'Name': results['Name'].values.tolist(),
        'Year': results['Year'].values.tolist(),
        'Season': results['Season'].values.tolist(),
        'Wins': results['Wins'].values.tolist(),
        'Passing_Yards': results['Passing Yards'].values.tolist(),
        'TD_Passes': results['TD Passes'].values.tolist(),
    }
    return jsonify(data)

# Data route
@app.route("/all-data")
def data():

    # Use Pandas to perform the sql query
    df = pd.read_csv(file)

    # Return a list of the data
    data = {
        'Name': df['Name'].values.tolist(),
        'Year': df['Year'].values.tolist(),
        'Season': df['Season'].values.tolist(),
        'Wins': df['Wins'].values.tolist(),
        'Passing_Yards': df['Passing Yards'].values.tolist(),
        'TD_Passes': df['TD Passes'].values.tolist(),
    }
    return jsonify(data)




if __name__ == "__main__":
    app.run()
