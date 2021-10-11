from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
app = Flask(__name__)
CORS(app)

url = 'https://spm-g4t1.hasura.app/v1/graphql?'


@app.route("/get_course")
def get_course():
    query = """
            query MyQuery {
                course_schema_course {
                    course_code
                    course_description
                    course_name
                    end_date
                    start_date
                }
            }
    """
    response = requests.post(url, json={'query': query}, headers={'content-type': 'application/json', 'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ' })
    return json.loads(response.text)['data']


@app.route("/get_course/<string:course_id>") ###
def get_course_by_id(course_id):
    filter = '{course_code: {_eq: "' + course_id +'"}}'
    query = """
        query MyQuery {
            course_schema_course(where: """ + filter + """) {
                course_code
                course_description
                course_name
                end_date
                start_date
            }
        }
    """
    response = requests.post(url, json={'query': query}, headers={'content-type': 'application/json', 'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ' })
    return json.loads(response.text)['data']

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
