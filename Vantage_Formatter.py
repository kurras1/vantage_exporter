#------------------------------------------------------------------#
# Vantage_Formatter.py                                             #
#                                                                  #
# Author:        Mike Kurras                                       #
# Date:          3/13/2025                                         #
# Description:   OpenMetrics exporter for Telestream Vantage       #
#                Designed for use with Prometheus                  #
#------------------------------------------------------------------#

import Metric_Formatter as formatter
import Vantage_Enum_Data as vantage_enums


#------------------------------------------------------------------#
#Get state of each service
#------------------------------------------------------------------#
def format_state(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'The current state of the Vantage service {vantage_enums.service_state}'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['State'])
    
    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_service_state", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Check if each service is accepting new work
#------------------------------------------------------------------#
def format_AcceptingWork(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'Is the Vantage service accepting work (False: 0, True: 1)'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        #This value is reported as a string boolean by the API so it needs to be converted to a numeric value for Open Metrics
        if bool(data[service]['Metrics']['AcceptingWork']):
            metric_list.append(1)
        else:
            metric_list.append(0)
        
    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_accepting_work", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get number of active sessions for each service
#------------------------------------------------------------------#
def format_ActiveSessionCount(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'How many active sessions does the Vantage service have'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['ActiveSessionCount'])

    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_active_session_count", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get average queue length for each service
#------------------------------------------------------------------#
def format_AverageQueueLength(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'What is the average queue length of the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['AverageQueueLength'])

    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_avg_queue_length", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get average wait time for the queue of each service
#------------------------------------------------------------------#
def format_AverageQueueWaitInSeconds(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'What is the average queue wait in seconds for the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['AverageQueueWaitInSeconds'])

    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_avg_queue_wait_seconds", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get current resource usage for each service
#------------------------------------------------------------------#
def format_CurrentResourceUsage(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'What is the current resource usage for the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['CurrentResourceUsage'])

    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_cur_resource_use", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get failed session count for each service
#------------------------------------------------------------------#
def format_FailedSessionCount(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'How many sessions have failed for the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['FailedSessionCount'])

    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_failed_session_count", label_service, metric_list, formatter.METRIC_TYPE.counter, help_text)

#------------------------------------------------------------------#
#Get successful session count for each service
#------------------------------------------------------------------#
def format_SuccessfulSessionCount(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'How many sessions have succeeded for the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['SuccessfulSessionCount'])
        
    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_success_session_count", label_service, metric_list, formatter.METRIC_TYPE.counter, help_text)

#------------------------------------------------------------------#
#Get total sessionc count for each service
#------------------------------------------------------------------#
def format_TotalSessionCount(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'How many sessions has the vantage service processed'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['TotalSessionCount'])
    
    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_total_session_count", label_service, metric_list, formatter.METRIC_TYPE.counter, help_text)

#------------------------------------------------------------------#
#Get queued session count for each service
#------------------------------------------------------------------#
def format_QueuedSessionCount(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'How many sessions are queued in the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['QueuedSessionCount'])
        
    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_queued_session_count", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get send queue size for each service
#------------------------------------------------------------------#
def format_SendQueueSize(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'What is the size of the send queue for the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['SendQueueSize'])
    
    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_send_queue_size", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get service utilization for each service
#------------------------------------------------------------------#
def format_ServiceUtilization(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'What is the current utilization of the vantage service'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['ServiceUtilization'])

    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_service_utilization", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Get target resource usage for each service
#------------------------------------------------------------------#
def format_TargetResourceUsage(data):
    #Define empty arrays for labels and metric values parsed from API Response
    label_service = []
    metric_list = []
    
    #Define help text for Open Metrics line
    help_text = f'What is the current usage of the target resource'
    
    #Iterate through all services to get the desired metric from each service as reported by the API response
    for service in data:
        label_service.append({"service": service})
        metric_list.append(data[service]['Metrics']['TargetResourceUsage'])
    
    #Pass parsed metric value to the open metrics formatter, and return the fully formatted metric line 
    return formatter.build_metric("vantage_target_resource_usage", label_service, metric_list, formatter.METRIC_TYPE.gauge, help_text)

#------------------------------------------------------------------#
#Primary execution block for Vantage formatting
#------------------------------------------------------------------#
def format_metrics(data):
    #Define an empty array to store metric lines
    metrics = []

    #Format data for each desired metric, append to array
    #The complete API response is passed to each helper function where it is parsed for desired metric
    metrics.append(format_state(data))
    metrics.append(format_AcceptingWork(data))
    metrics.append(format_ActiveSessionCount(data))
    metrics.append(format_AverageQueueLength(data))
    metrics.append(format_AverageQueueWaitInSeconds(data))
    metrics.append(format_CurrentResourceUsage(data))
    metrics.append(format_FailedSessionCount(data))
    metrics.append(format_SuccessfulSessionCount(data))
    metrics.append(format_TotalSessionCount(data))
    metrics.append(format_QueuedSessionCount(data))
    metrics.append(format_SendQueueSize(data))
    metrics.append(format_ServiceUtilization(data))
    metrics.append(format_TargetResourceUsage(data))
    
    #Join all the array lines together into a multi-line string and return
    return "\n".join(metrics)
    
