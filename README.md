We have several monitoring tools available in the market like Solarwinds, BMC Truesight, CA , Dynatrace.
With this project i am trying to help the IT professionals to create a customised dashboard with performance metrics from different tools in the market with no additional cost or expenses.
The opensource tools I  used here is 
#GRAFANA
#INFLUXDB
#TELEGRAF

#INTEGRATIONS
We will use python language to integrate to different tools. 

>>> Integration to Solarwinds Monitoring tool.
>>> Integration to Dynatrace Monitoring tool.
>>> Integration to BMC truesight reporting database.
>>> Integration to SQL database.
>>> Integration to Mainframe.
>>> Integration to Servicenow.


############Integration to Solarwinds Rest API#######################
>>>> Main tasks include
1. Open Solarwinds rest api ports from your server for connection
2. Rest api authentication.
3. Queries to solarwinds rest api to retrieve performance data.
4. Convert the data to influxdb line protocol format.
5. write the data to influxdb using telegraf.
6. Create the dashboards in grafana.
#################################################################
