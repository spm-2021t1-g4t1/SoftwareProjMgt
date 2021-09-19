from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
app = Flask(__name__)
CORS(app)

url = 'https://spm-g4t1.hasura.app/v1/graphql?'

@app.route("/view_section/<string:course_code>") ###
def view_section(course_code):
    filter = '{course_code: {_eq: "' + course_code +'"}}'
    query = """
            query MyQuery {
            section_schema_section(where: """ + filter + """) {
                section_code
                course_code
                section_description
                section_name
            }
        }    
    """

    response = requests.post(url, json={'query': query}, headers={'content-type': 'application/json', 'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ' })

    return_data = []
    for section in json.loads(response.text)['data']['section_schema_section']:
        course_code = section['course_code']
        section_code = section['section_code']
        section_description = section['section_description']
        section_name = section['section_name']
        course_materials = []
        filter = '{course_code: {_eq: "' + course_code + '"}, section_code: {_eq: ' + section_code + '}}'
        query = """
                query MyQuery {
                course_material_schema_course_material(where: """ + filter + """) {
                    file_id
                    file_path
                    course_code
                    section_code
                }
            }
        """
        response = requests.post(url, json={'query': query}, headers={'content-type': 'application/json', 'x-hasura-admin-secret': 'VzdZJkGQnpf3LdOqSq19hpvM6cCgL6OuwC0YYBxO72TYyLUFpsyBAp5uDC6kg5pQ' })    
        for course_material in json.loads(response.text)['data']['course_material_schema_course_material']:
            course_materials.append(course_material['file_path'])
        return_data.append({'course_code': course_code, 'section_code': section_code, 'section_description': section_description, 'section_name': section_name, 'course_materials': course_materials})         
    
    return jsonify(return_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
