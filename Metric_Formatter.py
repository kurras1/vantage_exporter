#------------------------------------------------------------------#
# Metric_Formatter.py                                              #
#                                                                  #
# Author:        Mike Kurras                                       #
# Date:          3/13/2025                                         #
# Description:   A generic function for formatting OpenMetrics     #
#                output for use with Prometheus exporters          #
#------------------------------------------------------------------#

from enum import Enum

#Define an Enum of the possible metric types
class METRIC_TYPE(Enum):
    unknown = 0
    gauge = 1
    counter = 2
    stateset = 3
    info = 4
    histogram = 5
    gaugehistogram = 6
    summary = 7

#------------------------------------------------------------------#
#Function to format a list of labels for a metric
#Expects a dictionary of labels where the key is label name and value is label value
#------------------------------------------------------------------#
def writeMetricLabel(labels):
    #Define an empty array for labels
    all_labels = []
    
    try:
        for label in labels:
            #Pull out the key and value and append it to the array
            all_labels.append(f'{label}=\"{"_".join(labels[label].split())}\"')
        
        #Return the formatted labels ready to be inserted into the metric line
        return f'{{{",".join(all_labels)}}}'
    except:
        #If something goes wrong just return an empty string
        return ""

#------------------------------------------------------------------#
#Function to format a list of labels for a metric
#Expects:
#    metric_name   (string)
#    metric_labels (dict)
#    metric_value  (single value or list)
#    metric_type   (METRIC_TYPE Enum)
#    help_text     (string)
#------------------------------------------------------------------#
def build_metric(metric_name, metric_labels, metric_value, metric_type, help_text):
    #Define an empty array to store metric lines
    metric = []
    if metric_labels is None:
        metric_labels = ""
        
    #Write Metric Help Line and append to array
    metric.append(f'# HELP {metric_name} {help_text}')
    
    #Write Metric Type Line and append to array
    metric.append(f'# TYPE {metric_name} {metric_type.name}')
    
    #Write Metric Lines
    try:
        #First try to iterate through multiple metric values appending each to array
        i = 0
        for line in metric_value:
            labels = writeMetricLabel(metric_labels[i])
            i += 1
            metric.append(f'{metric_name}{labels} {line}')
    except TypeError:
        #If iteration failes, then assume it is a single value and append single value to array
        metric.append(f'{metric_name}{metric_labels} {metric_value}')
    
    #Join it all together and return a fully formatted OpenMetric block
    return "\n".join(metric)