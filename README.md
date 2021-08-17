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


############Integration to Solarwinds#######################
>>>> Main tasks include
1. Open Solarwinds rest api ports from your server for connection TCP17778.
2. Rest api authentication ==> OrionSDK ==> https://github.com/solarwinds/orionsdk-python.
3. Queries to solarwinds rest api to retrieve performance data ==> Schema ==> https://solarwinds.github.io/OrionSDK/schema/index.html ==> Sample ==> https://github.com/munnathampi/Monitoring-Dashboard/blob/master/Solarwinds_performance_data.
4. Convert the data to influxdb line protocol format ==> https://docs.influxdata.com/influxdb/v1.8/write_protocols/line_protocol_tutorial/.
5. write the data to influxdb using telegraf ==> https://docs.influxdata.com/influxdb/v2.0/write-data/no-code/use-telegraf/manual-config/.
6. Create the dashboards in grafana ==> Influx Language ==> https://docs.influxdata.com/influxdb/v1.8/query_language/explore-data/.

![Network_sw.NG](https://github.com/munnathampi/Monitoring-Dashboard/blob/master/Network_sw.PNG![image](https://user-images.githubusercontent.com/23253649/129666236-a95e9031-837f-4ee0-9fd0-730fedd97ac5.png)
)



############Integration to Mainframe#######################
1. Open db2 port from your server.
2. Install db2 client on your server ==> https://www.ibm.com/docs/en/tfim/6.2.1?topic=products-installing-db2-administration-client-linux-unix-systems.
3. Python script to query your db2 mainframe and parse the data to influxdb ==> https://github.com/munnathampi/Monitoring-Dashboard/blob/master/db2mainframe.py.
4. Create dashboards in Grafana.
