#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:31:27 2019

@author: jessicaetchechury
"""
# add dependencies

import numpy as np


from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
import os
import datetime as dt

engine = create_engine("sqlite:///hawaii.sqlite")

# engine = create_engine("sqlite:///hawaii.sqlite")
#/Users/jessicaetchechury/Desktop/SMU_Data_Science/Unit_10_FlaskSQLAlchemy/Resources
Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

session = Session(engine)

# Calculate the date 1 year ago from the last data point in the database
last_date = session.query(func.strftime(Measurement.date)).order_by(Measurement.date.desc()).first()[0]
#Slice string as int then perform timedelta calculation and convert back to string
query_date = str(dt.date(int(last_date[0:4]),int(last_date[5:7]),int(last_date[8:10])) - dt.timedelta(days=365))

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    #Query precipation data (Date and Prcp)
    precipitation_query=session.query(Measurement.date,Measurement.prcp).all()
    #Convert query to a dictionary using date as the key and prcp as the value
    all_precipitation=[]
    for date, prcp in precipitation_query:
        precipitation_dict={}
        precipitation_dict["date"]=date
        precipitation_dict["prcp"]=prcp
        all_precipitation.append(precipitation_dict)
    #return JSON represen
    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def station():
    
    ##Return a dictionary of stations from the db##
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).\
                                group_by(Station.station).all()
    y=0
    stationlist=[]
    for _ in results:
        stationdictouter = {}
        stationdictinner = {}
        stationdictouter[results[y][0]] = stationdictinner
        stationdictinner["Station Name"] = results[y][1]
        stationdictinner["Station Latitude"] = results[y][2]
        stationdictinner["Station Longitude"] = results[y][3]
        y +=1
        stationlist.append(stationdictouter)

    return jsonify(stationlist)

@app.route("/api/v1.0/tobs")
def temperature():
    
    session = Session(engine)
    #Determine lastest date
    end_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    #Assign variable to latested date
    end_date=end_date[0]
    #Determine date one year prior to latest date
    start_date=dt.datetime.strptime(end_date,"%Y-%m-%d")-dt.timedelta(days=365)
    #Query temperature data for the time frame in question
    tobs_query=session.query(Measurement.date,Measurement.tobs).filter(Measurement.date>=start_date).all()
    #Create list of data
    tobs_list=list(tobs_query)
    #return JSON list of Temperature Observations for the previous year
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start):
#     """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start:
#     calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date supplied by the user"""

    session = Session(engine)
    start = str(start)
    end = last_date

    d1 = dt.date(int(start[0:4]),int(start[5:7]),int(start[8:10]))
    d2 = dt.date(int(end[0:4]),int(end[5:7]),int(end[8:10]))
    # Use the start and end date to create a range of dates
    daterange = [str(d1 + dt.timedelta(days=x)) for x in range((d2-d1).days + 1)]
    # Stip off the year and save a list of %m-%d strings
    md = [x[5:10] for x in daterange]
    # Loop through the list of %m-%d strings and calculate the normals for each date
    normals = [session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == x).all()[0] for x in md]
    normlist = []
    y = 0
    for _ in normals:
        normdictouter = {}
        normdictinner = {}
        normdictouter[daterange[y]] = normdictinner
        normdictinner["minimum temperature"] = normals[y][0]
        normdictinner["average temperature"] = normals[y][1]
        normdictinner["max temperature"] = normals[y][2]
        y +=1
    normlist.append(normdictouter)
    return jsonify(normlist )

app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start:
    calculate TMIN, TAVG, and TMAX for all dates between the start and end date provided by user inclusive"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    start = str(start)
    end = str(end)

    d1 = dt.date(int(start[0:4]),int(start[5:7]),int(start[8:10]))
    d2 = dt.date(int(end[0:4]),int(end[5:7]),int(end[8:10]))
    # Use the start and end date to create a range of dates
    daterange = [str(d1 + dt.timedelta(days=x)) for x in range((d2-d1).days + 1)]
    # Stip off the year and save a list of %m-%d strings
    md = [x[5:10] for x in daterange]
    # Loop through the list of %m-%d strings and calculate the normals for each date
    normals = [session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == x).all()[0] for x in md]
    normlist = []
    y = 0
    for _ in normals:
        normdictouter = {}
        normdictinner = {}
        normdictouter[daterange[y]] = normdictinner
        normdictinner["minimum temperature"] = normals[y][0]
        normdictinner["average temperature"] = normals[y][1]
        normdictinner["max temperature"] = normals[y][2]
        y +=1
        normlist.append(normdictouter)
    return jsonify(normlist )

if __name__ == "__main__":
    app.run(debug=True)