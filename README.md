# CRESHMap
CRESHMap


## References
This application follows the [flask application factory pattern](https://hackersandslackers.com/flask-application-factory/) and uses plotly to display the graphs as documented [here](https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946).


Set database connection string
```
export DATABASE_URL='postgresql://creshro:PASSWORD@pow/cresh?options=-c%20search_path=cresh'
```