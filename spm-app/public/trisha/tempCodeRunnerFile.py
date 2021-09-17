
import requests
query = f"""query MyQuery {{
            engineers {{
                name
                type
                engineer_id
                email
            }}
            }}"""

url = 'https://human-resource.hasura.app/v1/graphql'
myobj = {
    'x-hasura-admin-secret': 'R4q79TU2Z13Q22LVeawbwkhBynR4pbHUK8zZY5V4KhCw0Unse0zhh6h7hTtnpJHm',
    'content-type': 'application/json'
}

r = requests.post(url, headers = myobj, json = {'query': query})
results = r.json()['data']
print(results)