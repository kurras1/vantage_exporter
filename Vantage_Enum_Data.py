#------------------------------------------------------------------#
# Vantage_Enum_Data.py                                             #
#                                                                  #
# Author:        Mike Kurras                                       #
# Date:          3/13/2025                                         #
# Description:   OpenMetrics exporter for Telestream Vantage       #
#                Designed for use with Prometheus                  #
#------------------------------------------------------------------#

service_state = {
    "Online": 0,
    "Unreachable": 1,
    "Restarting": 2,
    "MaintenanceMode": 3,
    "PreShutdown": 4
}

job_session_state = {
    "Active": 0,
    "Ignored": 1,
    "Complete": 2,
    "Failed": 3,
    "Pending": 4,
    "Idle": 5,
    "Paused": 6,
    "Interrupted": 7,
    "Suspended": 8,
    "StoppedByUser": 9,
    "WaitingToRetry": 10,
    "WaitingOnLicense": 11,
    "WaitingOnService": 12,
    "WaitingOnRunOnRule": 13
}

workflow_job_state = {
    "Active": 0,
    "Stopping": 1,
    "Pausing": 2,
    "Paused": 3,
    "Failed": 4,
    "Complete": 5,
    "Waiting": 6,
    "StoppedByUser": 7,
    "WaitingToRetry": 8,
    "ErrorsDetected": 9,
    "QueuedForSubmission": 10,
    "DoesNotExist": 11
}