# Advanced SQL Challenge Module 10

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

There are two parts to this challenge:
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib

## Part 1: Analyse and Explore the Climate Data
### Precipitation Analysis
1.    Find the most recent date in the dataset.

2.    Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3.    Select only the "date" and "prcp" values.

4.    Load the query results into a Pandas DataFrame. Explicitly set the column names.

5.    Sort the DataFrame values by "date".

6.    Plot the results by using the DataFrame plot method.

7.    Use Pandas to print the summary statistics for the precipitation data

### Part 2: Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1.   Start at the homepage.
2.   List all the available routes: <br/>
    `/api/v1.0/precipitation` <br/>
    `/api/v1.0/stations` <br/>
    `/api/v1.0/tobs` <br/>
    `api/v1.0/<start>` <br/>
    `api/v1.0/<start>/<end>`
3.   Convert the query results to a dictionary by using date as the key and prcp as the value.
4.   Return the JSON representation of the dictionary
5.   Repeat the same for each route.
6.   `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>` <br/>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

7.  For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

8.  For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
<br/>

## 🧰 Languages and Tools

In this project I outline the tools, language and libraries required to complete the project brief.<br />

<img align="left" alt="Git" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />

<img align="left" alt="GitHub" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" />

<img align="left" alt="SQLalchemy" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" />

<img align="left" alt="SQLite" width="80px" style="padding-right:12px;" 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" />

<img align="left" alt="Jupyter" width="80px" style="padding-right:12px;" 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" />

<img align="left" alt="VSCode" width="80px" style="padding-right:12px;" 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg" />

<img align="left" alt="Google" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" />

<img align="left" alt="Google" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" />
          

<br /><br /><br /><br />

## ✅ Getting Started 
### 🛠️ Installation
Get up and running with the following command: <br/>
* Install SQLAlchemy
1.      pip install sqlalchemy
* Install Flask

2.      pip install flask


### ➡️ Run Workflows
Here is a code snippet that is used to handle the conversion of user-provided date strings into `datetime.date` objects.
This helps for a better user experience, providing formatted date strings to access the database. 

    try:

        start = dt.datetime.strptime(start,"%Y-%m-%d").date()
        
        end = dt.datetime.strptime(end, "%Y-%m-%d").date()

    except ValueError:

        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400



<br/>
# 📃 Documentation
The latest documentation is available at: <br/><br/>
https://www.sqlalchemy.org/docs/
https://flask.palletsprojects.com/en/3.0.x/installation/#virtual-environments


