#------------------------------------------------------------------#
# Vantage_Exporter.py                                              #
#                                                                  #
# Author:        Mike Kurras                                       #
# Date:          3/13/2025                                         #
# Description:   OpenMetrics exporter for Telestream Vantage       #
#                Designed for use with Prometheus                  #
#------------------------------------------------------------------#

import Vantage_Formatter

import os
import requests
import datetime
import time
import json

#------------------------------------------------------------------#
#Default Settings Overridden by ENV Variables
#------------------------------------------------------------------#
DEBUG = os.getenv('Vantage_Exporter_Debug_Mode', False)

#Overridden at runtime
VANTAGE_IP_ADDRESS = '0.0.0.0'
VANTAGE_PORT = '8676'

#Development Only
API_ROOT = '/Rest'

#------------------------------------------------------------------#
#Logger Function
#------------------------------------------------------------------#
def debug(data):
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    if DEBUG:
        print(f'{timestamp}\t{data}')

#------------------------------------------------------------------#
#This method is the main API Call Skeleton
#------------------------------------------------------------------#
def api_get(schema):
    
    #Construct the Request URL
    request_url = f'http://{VANTAGE_IP_ADDRESS}:{VANTAGE_PORT}{API_ROOT}{schema}'
    
    debug(f'Sending Request to: {request_url}')
    
    #Set Headers
    headers = {
        "accept": "application/json"
    }
    
    try:
        response = requests.get(request_url, headers=headers)
        response.raise_for_status()
        

        #Check for HTTP 200 OK Response
        if response.status_code == 200:
            #If HTTP 200 OK, then return response body
            debug("Response 200 OK!")
            debug("Parsing JSON...")
            
            try:
                json_response = json.loads(response.text)
                debug("JSON Data Successfully Parsed!")
                return json_response
            except Exception as e:
                debug(f'A JSON Parsing Error Occurred: {e}')
        
        #Otherwise Raise an Exception    
        else:
            raise()
    
    except requests.exceptions.RequestException as e:
        debug(f'An Error Occurred with HTTP Request: {e}')
        
#------------------------------------------------------------------#
#This is the primary execution block for processing an API request
#------------------------------------------------------------------#
def service_discover(target_ip, target_port):
    #Runtime override of target IP
    global VANTAGE_IP_ADDRESS 
    VANTAGE_IP_ADDRESS = target_ip
    
    #Runtime override of target port
    global VANTAGE_PORT
    VANTAGE_PORT = target_port
    
    discovered_services = {}
    #First read the services
    services_raw = api_get("/Services")
    
    #Iterate through discovered services
    for service in services_raw['Services']:
        
        discovered_services.setdefault(service['ServiceTypeName'], {}).setdefault('Identifier',service['Identifier'])
        discovered_services.setdefault(service['ServiceTypeName'], {}).setdefault('State',service['State'])
        
        #Try to read down to the next data level for each discovered service
        try:
            service_metrics = api_get(f"/Services/{service['Identifier']}/Metrics")
            discovered_services.setdefault(service['ServiceTypeName'], {}).setdefault('Metrics',service_metrics['Metric'])
        except:
            #If it fails just skip that service
            pass
    
    #Pass data to the formatter
    return Vantage_Formatter.format_metrics(discovered_services)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
