# Climate Flask App

## Background

Climate analysis was conducted on Honolulu Hawaii. 

## The Process

Python and SQLAlchemy was used to do basic climate analysis and data exploration of the climate database. In addtion, SQLAlchemy ORM queries, Pandas, and Matplotlib were used.  An engine was created to connect to the sqlite database provided and automap_base() was used to reflect the tables into classes.


### Precipitation Analysis

A query was designed to retrieve the last 12 months of precipitation data which was then loaded into a Pandas DataFrame.
The precipitation data was then plotted and summary statistics printed.

![Precipitation Analysis](Images/Precipitation)

![Precipitation Statistics](Images/PrecipitationStats)


### Station Analysis

Using a query the total number of stations was calculated, and the most active station was identified. Func.min, func.max, func.avg, and func.count were used to complete the queries. 
The temperature data for the most active station was plotted.

![Most Active Station Info](Images/MostActive)

![Most Active Station Temp Data](Images/MostActiveBar)


### Temperature Analysis

The `calc_temps` function was used to calculate the min, avg,and max temperatures for the chosen dates using the matching dates from the previous year.  The min, avg, and max temperature was depicted using a bar chart.

![Avg Trip Temperature](Images/AvgTemp)

  * Bar Height - Average temperature
  * Y Error Bar - Peak-to-Peak (tmax-tmin) value


### Daily Rainfall Average.

* Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic tobs that match that date string.

* Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/Samples/daily-normals.png)

## The App

After completing the initial analysis, a Flask API based on the queries conducted was develeoped.  The following routes were created:

* `/` - Home page

* `/api/v1.0/precipitation` - JSON list of precipitation data

* `/api/v1.0/stations` - JSON list of stations from the dataset

* `/api/v1.0/tobs` - JSON list of temperature observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`- JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, the `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date is calculated

  * When given the start and the end date, the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive is calcualated
