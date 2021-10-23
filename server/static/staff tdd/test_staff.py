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

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testStaff(TestApp):
    def testGetClassList(self):
        aStaff = staff(
            staff_username = 'coreyroberts',
            staff_name = 'Corey Roberts',
            role = 'Learner',
            department = 'Operation',
            current_designation = 'Engineer'
        )
        db.session.add(aStaff)
        db.session.commit()

        data = self.client.get(f"/staff")
        insertedStaff = data.json["data"][0]
        # print(data.json)
        # print(insertedStaff)
        self.assertEqual(insertedStaff["staff_username"], 'coreyroberts')
        self.assertEqual(insertedStaff["staff_name"], 'Corey Roberts')
        self.assertEqual(insertedStaff["role"], 'Learner')
        self.assertEqual(insertedStaff["department"], 'Operation')
        self.assertEqual(insertedStaff["current_designation"], 'Engineer')
    
    def testGetStaffByUsername(self):
        aStaff = staff(
            staff_username = 'darrelwilde',
            staff_name = 'Darrel Wilde',
            role = 'Learner',
            department = 'Development',
            current_designation = 'Engineer'
        )
        db.session.add(aStaff)
        db.session.commit()

        data = self.client.get(f"/login/darrelwilde")
        # insertedStaff =data.json['data'][0]
        insertedStaff = data.json['data']['staff_username']
        # print(insertedStaff)

        self.assertEqual(insertedStaff, 'darrelwilde')


        


# class testIntegrate(TestApp):
#     def test_to_dict(self):
#         c1 = classEnrolmentQueue(staff_username = 'stevejob',course_id = '3', class_no = '2')
#         db.session.add(c1)
#         db.session.commit()

#         response = self.client.get('/queue/stevejob/3')
#         print(response.json)

# class testUni(unittest.TestCase):
#     def test_sample2(self):
#         c1 = classEnrolmentQueue(staff_username = 'stevejob',course_id = '3', class_no = '2')
#         print(c1.json())

if __name__ == "__main__":
    unittest.main()
