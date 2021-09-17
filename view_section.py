from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
app = Flask(__name__)
CORS(app)

url = 'https://spm-g4t1.hasura.app/v1/graphql?'


@app.route("/get_all_sections/<string:course_id>")
def get_all_sections(course_id):
    filter = '{course_code: {_eq: "' + course_id +'"}}'
    query = """
            query MyQuery {
            section_schema_section(where: """ + filter + """) {
                section_no
                course_code
            }
        }    
    """
    response = requests.post(url, json={'query': query}, headers={'content-type': 'application/json', 'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ' })
    return json.loads(response.text)['data']


@app.route("/view_section/<string:course_id>/<string:section_id>") ###
def view_section(course_id, section_id):
    filter = '{course_code: {_eq: "' + course_id + '"}, section_no: {_eq: ' + section_id + '}}'
    query = """
            query MyQuery {
            course_material_schema_course_material(where: """ + filter + """) {
                file_id
                file_path
                course_code
                section_no
            }
        }
    """
    response = requests.post(url, json={'query': query}, headers={'content-type': 'application/json', 'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ' })
    return json.loads(response.text)['data']

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
