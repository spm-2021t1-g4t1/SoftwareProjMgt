# Done by Trisha
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
    def testGetStaffList(self):
        data = self.client.get(f"/staff")
        self.assert200(data)
        insertedStaff = data.json["data"][0]

        self.assertEqual(insertedStaff["staff_username"], 'coreyroberts')
        self.assertEqual(insertedStaff["staff_name"], 'Corey Roberts')
        self.assertEqual(insertedStaff["role"], 'Learner')
        self.assertEqual(insertedStaff["department"], 'Operation')
        self.assertEqual(insertedStaff["current_designation"], 'Engineer')
    
    def testGetStaffByUsername(self):
        data = self.client.get(f"/login/darrelwilde")
        self.assert200(data)
        insertedStaff = data.json['data']['staff_username']

        self.assertEqual(insertedStaff, 'darrelwilde')
    
    def testGetEngineerList(self):
        data = self.client.get(f"/staff/engineers")
        self.assert200(data)
        engineersList = data.json['data']
        # print(data.json['data'])
        
        self.assertEqual(engineersList[0]['staff_username'], 'coreyroberts')
        self.assertEqual(engineersList[0]['current_designation'], 'Engineer')
        self.assertEqual(engineersList[1]['staff_username'], 'darrelwilde')
        self.assertEqual(engineersList[1]['current_designation'], 'Engineer')





if __name__ == "__main__":
    unittest.main()
