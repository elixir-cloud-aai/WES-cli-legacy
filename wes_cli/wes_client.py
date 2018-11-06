import urllib3
# urllib3.disable_warnings()
# Required to create a new Requests 'http_client' instance
from bravado.requests_client import RequestsClient
# Required to create a Bravado SwaggerClient instance
from bravado.client import SwaggerClient

def init_client(url):

    """Init client"""

    # Create a new Requests client instance
    http_client = RequestsClient()
    # http_client = FidoClient()

    http_client.session.verify = False

    swagger_client = SwaggerClient.from_url(
        url,
        http_client=http_client,
        config={'also_return_response': True,
                'validate_responses': True}
    )

    return swagger_client

def get_service_info(client):
    """Get service info"""
    return client.WorkflowExecutionService.GetServiceInfo(
    ).response(timeout=0.5, fallback_result=[]).result

def get_runs(client):
    """Get runs"""
    return client.WorkflowExecutionService.ListRuns(
    ).response(timeout=0.5, fallback_result=[]).result

def get_run(client, run_id):
    """Get run id"""
    return client.WorkflowExecutionService.GetRunLog(
        run_id=run_id
    ).response(timeout=0.5, fallback_result=[]).result

def get_run_status(client, run_id):
    """Get run status"""
    return client.WorkflowExecutionService.GetRunStatus(
        run_id=run_id
    ).response(timeout=0.5, fallback_result=[]).result

# URL = "https://localhost/ga4gh/wes/v1/swagger.json"
#
# client = init_client(URL)
# service_info = get_service_info(client=client)
# runs = get_runs(client=client)
# run = get_run(client=client, run_id="IXOH4X")
# run_status = get_run_status(client=client, run_id="IXOH4X")
#
# print(client)
# print(service_info)
# print(runs)
# print(run)
# print(run_status)
