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
def years():
    """Return a list of years."""

    df = pd.read_csv(file)
    year_list = list((df.Year))
    scrubbed_list = list(dict.fromkeys(year_list))
    # Return a list of the column names (sample names)
    return jsonify(scrubbed_list)


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


@app.route("/wins/<start>/<end>")
def wins(start,end):

    # Use Pandas to read in data
    df = pd.read_csv(file)
    defOne= df[(df.Year >=int(start)) & (df.Year <= int(end))]
    defOne = defOne.groupby(['Name']).agg(np.sum)
    defOne.reset_index(inplace = True)
    defOne.sort_values('Wins',ascending=False,inplace = True)
    
    data = {
        'Name': defOne['Name'].values.tolist(),
        'Wins': defOne['Wins'].values.tolist(),
        'Passing_Yards': defOne['Passing Yards'].values.tolist(),
        'TD_Passes': defOne['TD Passes'].values.tolist(),
    }
    return jsonify(data)

@app.route("/td_passes/<start>/<end>")
def passes(start,end):

    # Use Pandas to read in data
    df = pd.read_csv(file)
    defOne= df[(df.Year >=int(start)) & (df.Year <= int(end))]
    defOne 
    defOne.reset_index(inplace = True)
    defOne.sort_values('TD Passes',ascending=False,inplace = True)
    
    data = {
        'Name': defOne['Name'].values.tolist(),
        'Year': defOne['Year'].values.tolist(),
        'Season': defOne['Season'].values.tolist(),
        'Wins': defOne['Wins'].values.tolist(),
        'Passing_Yards': defOne['Passing Yards'].values.tolist(),
        'TD_Passes': defOne['TD Passes'].values.tolist(),
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
