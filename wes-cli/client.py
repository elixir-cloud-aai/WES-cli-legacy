from bravado.client import SwaggerClient

def init_client(url):

    """Initialize client (no auth)"""

    return SwaggerClient.from_url(url)

# def service-info():
    # pass

url = "http://localhost:7777/ga4gh/wes/v1/swagger.json"

client = init_client(url)

print(client.runs)



# pet = client.pet.getPetById(petId=42).response().result
