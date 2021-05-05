#!/usr/bin/env python
import csv
import sys,os
import time
from time import *
from datetime import *
import subprocess

#####To get the credentials you may read from file or some path 

id = idvariable
pw = idpassword
#-----------------------------------------------------------
#Function to format the tags and fields into influxdb format
#-----------------------------------------------------------
def lpquote(s):
    if (s == None or s is None or s == ''):
      s = "unknown"
    else:
     s = s.strip()
     #s = s.replace("", "NA")
     s = s.replace(" ", "\ ")
     s = s.replace("=", "\=")
     s = s.replace(",", "\,")
     #s = s.replace(".","_")  
     #s = s.replace(":\\", ":")
    return s

#-----------------------------------------------------------
#Function to format the tags and fields into influxdb format
#-----------------------------------------------------------
def quoteAdder(s):
    double_q = '"'
    return double_q + s + double_q

csv = open("csvfilepath",'w')
DEVNULL = open(os.devnull,'w') 
args = '"pathtodb2client" connect to db2 user '+ id +' using '+ pw

#-----------------------------------------------------------------------------------------------
#connection to db2 and writting the quried output to csv
#-----------------------------------------------------------------------------------------------
subprocess.call(args,shell=True,stdout=DEVNULL)
#

subprocess.call("pathtodb2client \"your db2 query \"",shell=True,stdout=csv)

csv.close()
count = 0

#--------------------------------------------------------------------------------------------------------------------------------------------
#Writing Data output in line protocol to csv
#Here the data is written to a csv file in line protocol format. User can import the data from csv into influxdb using influx import function.
#---------------------------------------------------------------------------------------------------------------------------------------------

wfile1= open("yourcsvpath",'w')
wfile1.write("# DDL\n")
wfile1.write("CREATE DATABASE IF NOT EXISTS yourinfluxdb\n")
wfile1.write("# DML\n")
wfile1.write("# CONTEXT-DATABASE: yourinfluxdb\n")

with open("yourcsvfile",'r') as infile:
        for row in infile:
		  #parse your data here
          wfile1.write("convert your queried data to influxdb line protocol format")

wfile1.close()
subprocess.call("'pathtodb2client' connect reset",shell=True,stdout=DEVNULL)
