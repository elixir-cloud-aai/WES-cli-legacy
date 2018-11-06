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

URL = "https://localhost/ga4gh/wes/v1/swagger.json"

client = init_client(URL)
service_info = get_service_info(client=client)
runs = get_runs(client=client)
run = get_run(client=client, run_id="IXOH4X")
run_status = get_run_status(client=client, run_id="IXOH4X")

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
