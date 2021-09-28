from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from db import db
from static.model.staff import Staff #Import your classes here

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'

@app.route('/list_of_staff')
def list_of_staff():
    staff_list = Staff.query.all()
    return {'data': [staff.json() for staff in staff_list]}

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
    #just python app.py to execute
