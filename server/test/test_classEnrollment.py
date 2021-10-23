import unittest
import flask_testing
import json
from helper import *
from app import *
from datetime import datetime
# from app.model import staff
# from app import app, db

# staff.py
# do for classenrollment too

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()
        Objects = [
            staff(staff_username = 'coreyroberts', staff_name = 'Corey Roberts', role = 'Learner', department = 'Operation', current_designation = 'Engineer'),
            staff(staff_username = 'hello', staff_name = 'hello', role = 'Learner', department = 'Operation', current_designation = 'Engineer'),
            course(course_id = 1, course_name = "Test Course 1", description = "Test Description 1" ),
            course(course_id = 2, course_name = "Test Course 2", description = "Test Description 2"),
            classes(course_id = 1, class_no = 1, start_date = datetime(2021,9,1), end_date = datetime(2021,9,2), class_size = 40, trainer_name = 'stevejobs'),
            classes(course_id = 2, class_no = 1, start_date = datetime(2021,9,1), end_date = datetime(2021,9,2), class_size = 40, trainer_name = 'stevejobs'),
            classEnrolment(staff_username = 'coreyroberts', course_id = 1, class_no = 1),
            classEnrolment(staff_username = 'hello', course_id = 1, class_no = 1),
            classEnrolment(staff_username = 'coreyroberts', course_id = 2, class_no = 1)
        ]
        
        db.session.bulk_save_objects(Objects)
        db.session.commit()

        

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testClassEnrollment(TestApp):
    def testGetClassList(self):

        data = self.client.get(f"/enrolment/{1}/{1}")
        insertedStudents = data.json["data"]

        self.assertEqual(insertedStudents['0']['staff_username'], 'coreyroberts')
        self.assertEqual(insertedStudents['1']['staff_username'], 'hello')
    

    def testGetClassNumber(self):
        data = self.client.get(f"/enrolment/{1}/{1}/length")
        numStudents = data.json['message']

        self.assertEqual(numStudents, 2)

    
    def testGetStaffEnrollment(self):

        data = self.client.get(f"/enrolment/coreyroberts")

        course_id1 = data.json['data'][0]['course_id']
        class_no1 = data.json['data'][0]['classes'][0]['class_no']
        course_id2 = data.json['data'][1]['course_id']
        class_no2 = data.json['data'][1]['classes'][0]['class_no']
        
        self.assertEqual(course_id1, 1)
        self.assertEqual(course_id2, 2)
        self.assertEqual(class_no1, 1)
        self.assertEqual(class_no2, 1)



if __name__ == "__main__":
    unittest.main()


