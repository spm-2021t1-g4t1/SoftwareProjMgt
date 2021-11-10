# Done by Trisha
import unittest
import flask_testing
import json
from helper import *
from app import *
from datetime import datetime

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

    def test_json(self):
        staff1 = staff(staff_username = 'coreyroberts', staff_name = 'Corey Roberts', role = 'Learner', department = 'Operation', current_designation = 'Engineer')
        enrollment = classEnrolment(staff_username = 'coreyroberts', course_id = 1, class_no = 1, staff = staff1)
        

        expected = {
            "staff_name" : 'Corey Roberts',
            "staff_username": 'coreyroberts',
            "course_id": 1,
            "class_no": 1
        }

        self.assertEqual(enrollment.json(), expected)

    def testGetClasslist(self):
        data = classEnrolment.getClasslist(1, 1)
        self.assertEqual(data['data'],
        [{'staff_username': 'coreyroberts', 'staff_name': 'Corey Roberts', 'role': 'Learner', 'department': 'Operation', 'current_designation': 
        'Engineer'}, {'staff_username': 'hello', 'staff_name': 'hello', 'role': 'Learner', 'department': 'Operation', 'current_designation': 'Engineer'}]
        )
    
    def testGetClasslistByCourse(self):
        data = classEnrolment.getClasslistByCourse(1)
        self.assertEqual(data['data'], 
        [{'staff_username': 'coreyroberts', 'staff_name': 'Corey Roberts', 'role': 'Learner', 'department': 'Operation', 'current_designation': 'Engineer'}, {'staff_username': 'hello', 'staff_name': 'hello', 'role': 'Learner', 'department': 'Operation', 'current_designation': 'Engineer'}]
        )

    def testGetStaffEnrollment(self):
        data = classEnrolment.getStaffEnrollment('coreyroberts')
        self.assertEqual(data['data'],
        {0: {'staff_name': 'Corey Roberts', 'staff_username': 'coreyroberts', 'course_id': 1, 'class_no': 1}, 1: {'staff_name': 'Corey Roberts', 'staff_username': 'coreyroberts', 'course_id': 2, 'class_no': 1}}
        )

    def testEnrollToClass(self):
        data = classEnrolment.enrollToClass('hello', 2, 1)
        
        self.assertEqual(data['data'], 'Added')
        classList = classEnrolment.getClasslist(2, 1)
        self.assertEqual(classList['data'], 
        [{'staff_username': 'coreyroberts', 'staff_name': 'Corey Roberts', 'role': 'Learner', 'department': 'Operation', 'current_designation': 'Engineer'}, {'staff_username': 'hello', 'staff_name': 'hello', 'role': 'Learner', 'department': 'Operation', 'current_designation': 'Engineer'}])


if __name__ == "__main__":
    unittest.main()