import requests
import json
from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/engineers', methods = ['GET'])
def getengineers():
    
    # engineers_data = request.get_json()
    # name = engineers_data['name']
    # email = engineers_data['email']
    # engineer_id = engineers_data['id']
    # type = engineers_data['type']


    # call Graphql
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
    return render_template('get_all_details.html', results = results)


app.run(host="0.0.0.0", port=5000, debug=True)