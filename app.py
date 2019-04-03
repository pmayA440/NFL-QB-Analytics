# Dependancies
import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# Database Setup
cwd = os.getcwd()
f = "Assets\\Data_Files"
# url_for=
file = "Cleaned_QB_data.csv"
path = os.path.join(cwd, f, file)


# Home route
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

# All-Data route
@app.route("/all-data/<start>/<end>")
def names(start,end):

    # Use Pandas to read in data
    df = pd.read_csv(path)
    defOne= df[(df.Year >=int(start)) & (df.Year <= int(end))]
    defOne = defOne[['Name','Passing Yards','TD Passes','Wins']].groupby(['Name']).agg(np.sum)
    defOne.reset_index(inplace = True)
    defOne.sort_values('Wins',ascending =False,inplace = True)
    

    # Return a list of the data
  # Return a list of the data
    # data = {
    #     'Year': df['Year'].values.to_dict(),
    #     'Name': df['Name'].values.to_dict(),
    #     'Season': df['Season'].values.to_dict(),
    #     'Passing Yards': df['Passing Yards'].values.to_dict(),
    #     'TD Passes': df['TD Passes'].values.to_dict(),
    #     'Wins': df['Wins'].values.to_dict(),
    # }
    return jsonify(defOne.to_dict(orient="records"))


if __name__ == "__main__":
    app.run()
