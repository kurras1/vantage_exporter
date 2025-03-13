#------------------------------------------------------------------#
# Vantage_Exporter_HTTP.py                                         #
#                                                                  #
# Author:        Mike Kurras                                       #
# Date:          3/13/2025                                         #
# Description:   OpenMetrics exporter for Telestream Vantage       #
#                Designed for use with Prometheus                  #
#------------------------------------------------------------------#

from flask import Flask, request, Response
import Vantage_Exporter

script_name = "Vantage_Exporter.py"

app = Flask(__name__)

@app.route('/metrics')
def get_data():
    
    #GET target and target port from HTTP Request
    target_ip = request.args.get('target')
    target_port = request.args.get('target_port')
    
    #Pass the target values from the GET request to the Vantage Exporter function which returns the fully formatted openmetrics data
    data = Vantage_Exporter.service_discover(target_ip, target_port)
    
    
    return Response(data, mimetype="text/document")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')