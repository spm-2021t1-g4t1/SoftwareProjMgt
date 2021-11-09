import unittest
import flask_testing
import json
from helper import *
from app import *
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
            staff(staff_username = 'darrelwilde', staff_name = 'Darrel Wilde', role = 'Learner', department = 'Development', current_designation = 'Engineer'),
            staff(staff_username = 'hananhyde', staff_name = 'Hanan Hyde', role = 'Administrator', department = 'Human Resources', current_designation = 'Executive')
        ]
        db.session.bulk_save_objects(Objects)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testStaff(TestApp):
    def test_viewjson(self):
        staff1 = staff(staff_username = 'coreyroberts', staff_name = 'Corey Roberts', role = 'Learner', department = 'Operation', current_designation = 'Engineer')

        expected = {
            'staff_username': 'coreyroberts',
            'staff_name': 'Corey Roberts', 
            'role': 'Learner',
            'department': 'Operation',
            'current_designation': 'Engineer'
        }

        self.assertEqual(staff1.viewjson(), expected)

    def test_getStaffList(self):
        data = staff.get_staffList()
        self.assertEqual(data['data'], 
        [{'staff_username': 'coreyroberts', 'staff_name': 'Corey Roberts', 'role': 'Learner', 'department': 'Operation', 'current_designation': 'Engineer'}, {'staff_username': 'darrelwilde', 'staff_name': 'Darrel Wilde', 'role': 'Learner', 'department': 'Development', 'current_designation': 'Engineer'}, {'staff_username': 'hananhyde', 'staff_name': 'Hanan Hyde', 'role': 'Administrator', 'department': 'Human Resources', 'current_designation': 'Executive'}]
        )

    def test_getStaffByUsername(self):
        data = staff.get_staff_by_username('coreyroberts')
        self.assertEqual(data['data'],
        {'staff_username': 'coreyroberts', 'role': 'Learner', 'staff_name': 'Corey Roberts'}
        )

    def test_getEngineerList(self):
        data = staff.get_engineerList()
        self.assertEqual(data['data'],
        [{'staff_username': 'coreyroberts', 'staff_name': 'Corey Roberts', 'role': 'Learner', 'department': 'Operation', 'current_designation': 'Engineer'}, {'staff_username': 'darrelwilde', 'staff_name': 'Darrel Wilde', 'role': 'Learner', 'department': 'Development', 'current_designation': 'Engineer'}]
        )



if __name__ == "__main__":
    unittest.main()