#import all necessary libraries
import numpy as np
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import request
from flask import Flask, jsonify, Response


app = Flask(__name__)

################################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect database into model
Base = automap_base()
# Reflect tabe
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)
session.query(Measurement.date).order_by(Measurement.date.desc()).first()
recent_year = dt.date(2017, 8, 23)
last_year = recent_year - dt.timedelta(days=365)
###################################################################

# Flask Setup
#Setting up routes with endpoints.

@app.route("/")
# Create home page
def homepage():
    return (
        "Welcome to the Hawaii Climate Analysis API!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/temp/start=<start><br/>"
        "To access temperature data start date, use the following format: /api/v1.0/temp/start=YYYY-MM-DD<br/>"
        "/api/v1.0/temp/start=<start>/&end=<end><br/>"
        "To access temperature data from start date to end date, use the following format: /api/v1.0/temp/start=YYYY-MM-DD/&end=YYYY-MM-DD<br/>"
        "<strong>Example:</strong> /api/v1.0/temp/start=2017-01-01<br/>"
        "<strong>Example:</strong> /api/v1.0/temp/2017-01-01/2017-12-31"
    )
    
@app.route("/api/v1.0/precipitation")
# Create function for precipitation database session query
def precipitation():
    session = Session(engine) 

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year).all()
    
    session.close()
# Create a dictionary for the date and prcp
    precipitation = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        precipitation.append(prcp_dict)
    return jsonify(precipitation)
    
# Create function for stations database session query    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    results = session.query(Station.station).all()
    
    session.close()
    
    all_stations = []
    for result in results:
        station_dict = {}
        station_dict["station"] = result[0]
        all_stations.append(station_dict)
    return jsonify(all_stations)

# Create function for tobs database session query    
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= last_year).all()
    
    most_active_stations = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        most_active_stations.append(tobs_dict)
    return jsonify(most_active_stations)
 
# Create function for temperature database session query    
@app.route("/api/v1.0/temp/start=<start>")
def start_temperature(start):
     # Convert the start date string to a datetime object
    try:
        start = dt.datetime.strptime(start, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
        
    session.close()
    
    #Store list of tmin, tmax, tavg
    list_data = []
    for result in results:
        list_dict = {}
        list_dict["TMIN"] = result[0]
        list_dict["TMAX"] = result[1]
        list_dict["TAVG"] = round(result[2],2)
        list_data.append(list_dict)
        
    response_data = {"Your selected date": str(start), "Here is the temperature data": list_data}
    
    return jsonify(response_data)

@app.route("/api/v1.0/temp/start=<start>/&end=<end>")
def temperature_range(start, end ):
    try:
        # Convert start and end date strings to datetime objects
        start = dt.datetime.strptime(start, "%Y-%m-%d").date()
        end = dt.datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
    
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start, Measurement.date <= end).all()
    
    session.close()
    
    temperature_range = []
    for result in results:
        temperature_dict = {}
        temperature_dict["TMIN"] = result[0]
        temperature_dict["TMAX"] = result[1]
        temperature_dict["TAVG"] = round(result[2],2)
        temperature_range.append(temperature_dict)
        
    response_date = {"Your selected date": f"{start} to {end}", "Here is the temperature data": temperature_range}    
    return jsonify(response_date)
    
#Define behaviour of app    
if __name__ == '__main__':
    app.run(debug=True)