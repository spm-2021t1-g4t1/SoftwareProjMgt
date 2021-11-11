import unittest
import json
import flask_testing
from datetime import datetime, timedelta
from helper import *

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
            course(
            course_id=1,
            course_name='Test Course 1',
            description='Test Description 1'
            ),
            course(
            course_id=2,
            course_name='Test Course 2',
            description='Test Description 2'
            ),
            course(
            course_id=3,
            course_name='Test Course 3',
            description='Test Description 3'
            ),
            course(
            course_id=4,
            course_name='Test Course 4',
            description='Test Description 4'
            ),
            course(
            course_id=5,
            course_name='Test Course 5',
            description='Test Description 5'
            ),
            course_prerequisite(
                course_id = 2,
                prerequisite_course_id = 1
            ),
            course_prerequisite(
                course_id = 4,
                prerequisite_course_id = 3
            ),
            course_completion(
                course_id = 1,
                staff_username = "darrelwilde"
            ),
            classEnrolment(staff_username = 'darrelwilde', course_id = 2, class_no = 1),
        ]

        db.session.bulk_save_objects(Objects)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testGetStaffCompletion(TestApp):
    def testSuccess(self):
        data = self.client.get(f"/eligiblity/3/'darrelwilde")
        self.assert200(data)

        self.assertEqual(data.json, {'eligiblity': True})

    def testFailed(self):
        data = self.client.get(f"/eligiblity/4/'darrelwilde")
        self.assert200(data)
        self.assertEqual(data.json, {'eligiblity': False})

class testGetEligibleStaff(TestApp):
    def testGetRoute(self):
        data = self.client.get(f"/eligibility/5")
        self.assert200(data)

        # print(data.json)

class testFinal_Quiz_Eligibility(TestApp):
    def testGetRoute(self):
        data = self.client.get(f"/eligibility/final_quiz/1/<int:class_no>/<string:staff_username>")

if __name__ == "__main__":
    unittest.main()
