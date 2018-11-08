import urllib3
# urllib3.disable_warnings()
# Required to create a new Requests 'http_client' instance
from bravado.requests_client import RequestsClient
# Required to create a Bravado SwaggerClient instance
from bravado.client import SwaggerClient

def init_client(
        url,
        disable_fallback_results=False,
        validate_responses=True,
        validate_requests=True,
        validate_swagger_spec=True,
        use_models=True,
        ssl_verify=True,
):

    """Init client"""

    # Create a new Requests client instance
    http_client = RequestsClient()

    http_client.session.verify = ssl_verify

    swagger_client = SwaggerClient.from_url(
        url,
        http_client=http_client,
        config={'disable_fallback_results': disable_fallback_results,
                'validate_responses': validate_responses,
                'validate_requests': validate_requests,
                'validate_swagger_spec': validate_swagger_spec,
                'use_models': use_models}
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

def post_run(
    client,
    workflow_params,
    workflow_type,
    workflow_type_version,
    workflow_url
):

    """Post run"""

    post_run_id = client.WorkflowExecutionService.RunWorkflow(
        workflow_params=workflow_params,
        workflow_type=workflow_type,
        workflow_type_version=workflow_type_version,
        workflow_url=workflow_url
    ).response(timeout=60, fallback_result=[]).result

    return post_run_id

def post_cancel_run(client, run_id):

    """Cancel run"""

    return client.WorkflowExecutionService.CancelRun(
        run_id=run_id
    ).response(timeout=0.5, fallback_result=[]).result
