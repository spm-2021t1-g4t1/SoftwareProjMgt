import unittest
import flask_testing
import json
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

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testIntegrate(TestApp):
    def test_to_dict(self):
        c1 = classEnrolmentQueue(staff_username = 'stevejob',course_id = '3', class_no = '2')
        db.session.add(c1)
        db.session.commit()

        response = self.client.get('/queue/stevejob/3')
        print(response.json)

class testUni(unittest.TestCase):
    def test_sample2(self):
        c1 = classEnrolmentQueue(staff_username = 'stevejob',course_id = '3', class_no = '2')
        print(c1.json())

if __name__ == "__main__":
    unittest.main()
