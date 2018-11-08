import urllib3
# urllib3.disable_warnings()
# Required to create a new Requests 'http_client' instance
from bravado.requests_client import RequestsClient
# Required to create a Bravado SwaggerClient instance
from bravado.client import SwaggerClient

from wes_client import init_client
from wes_client import get_service_info
from wes_client import get_runs
from wes_client import get_run
from wes_client import get_run_status
from wes_client import post_run
from wes_client import post_cancel_run

URL = "https://localhost/ga4gh/wes/v1/swagger.json"

workflow_type = 'cwl'
workflow_type_version = 'v1.0'
workflow_url = 'https://github.com/fgypas/cwl-example-workflows/blob/master/hashsplitter-workflow.cwl'
workflow_params = '{"input":{"class":"File","path":"ftp://ftp-private.ebi.ac.uk/upload/foivos/test.txt"}}'
tags='{}'
workflow_engine_parameters='{}'
# workflow_attachment='{}'

client = init_client(url=URL, ssl_verify=False, use_models=False)
service_info = get_service_info(client=client)
runs = get_runs(client=client)
run = get_run(client=client, run_id="S53NI4")
run_status = get_run_status(client=client, run_id="S53NI4")
post_run_id = post_run(
    client=client,
    workflow_params=workflow_params,
    workflow_type=workflow_type,
    workflow_type_version=workflow_type_version,
    workflow_url=workflow_url
)

print("SERVICE INFO")
print(service_info)
print("*" * 80)
print("RUNS")
print(runs)
print("*" * 80)
print("RUNS")
print(run)
print("*" * 80)
print("RUN STATUS")
print(run_status)
print("*" * 80)
print("POST RUN")
print(post_run_id)
print("*" * 80)
