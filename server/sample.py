from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
db = SQLAlchemy(app)

class CourseEnrolment(db.Model):
    __tablename__ ="course_enrolment"
    staff_email = db.Column(db.String(255), primary_key=True)
    course_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, staff_email, course_id):
        self.staff_email = staff_email
        self.course_id = course_id

    def json(self):
        return {
            "staff_email": self.staff_email,
            "course_id": self.course_id
        }

    def add_enrolment(self):
        try:
            db.session.add(self)
            db.session.commit()
            return "Added!"
        except:
            return "Failed to add"

class Staff(db.Model):
    __tablename__ = "staff"

    staff_email = db.Column(db.String(255), primary_key=True)
    years_of_service = db.Column(db.Integer)

    def __init__(self, staff_email, years_of_service):
        self.staff_email = staff_email
        self.years_of_service = years_of_service
    
    def json(self):
        return {
            "staff_email": self.staff_email,
            "years_of_service": self.years_of_service
        }

    @classmethod
    def get_all_staff(cls):
        return cls.query.all() # Returns a list of Staff Object [<staff1]

    @classmethod
    def get_specific_staff(cls, staff_email):
        return cls.query.filter_by(staff_email=staff_email).first() #Returns a Staff Object

    # @classmethod
    # def get_enrolment_by_staff_email(cls, staff_email):
    #     enrolment = CourseEnrolment.query.filter_by(staff_email=staff_email).all() ##CourseEnrolment type
    #     return enrolment


@app.route('/list_of_staff')
def list_of_staff():
    staff_list = Staff.get_all_staff()
    staff_email_list = []
    for staff in staff_list:
        staff_email_list.append(staff.staff_email)
    return {'data': staff_email_list}

@app.route('/staff/<string:staff_email>')
def staff(staff_email):
    staff = Staff.get_specific_staff(staff_email).json()
    return staff


@app.route('/enrolment/<string:course_id>/<string:staff_email>') #enroll a staff to a specific course
def enrolment(course_id, staff_email):
    #staff_to_enroll = Staff.get_specific_staff(staff_email).staff_email
    commit = CourseEnrolment(staff_email, course_id).add_enrolment()
    return commit

if __name__ == "__main__":
    app.run(debug=True)
    #just python app.py to execute