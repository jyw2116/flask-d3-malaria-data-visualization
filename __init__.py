import flask
from flask import request
import json, csv
from os.path import join


app = flask.Flask(__name__)

file_name = join('data', 'reported_confirmed_cases.csv')

@app.route("/")
@app.route("/search/<country>")
def index(country = "India"):
    """
    When you request the root path, you'll get the index.html template.

    """
    return flask.render_template("index.html", countries = parseCountries(), country = country)


@app.route("/jendata")
@app.route("/jendata/<country>")
def selectColumns(file_name = file_name, country = "India"):
    """
    DESCRIPTION!!!
    :param blarg:
    :returns data:
        A JSON string of ``ndata`` data points.

    """
    input_file = csv.DictReader(open(file_name))
    arr_tuple = []
    print request
    for row in input_file:
        # TODO : All Countries
        if row['Country'] == country:
            arr_tuple.append({"year": int(row['Year']),
                        "numeric": float(row['Numeric'])
                        }
                       )
    return json.dumps(arr_tuple)


def parseCountries(file_name = file_name):

    input_file = csv.DictReader(open(file_name))
    countries = set()

    for row in input_file:
        countries.add(row['Country'].decode('utf8'))

    return sorted(countries)


if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
