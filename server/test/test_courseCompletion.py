# Done by Chuen Kai
# ck.ong.2018
import unittest
import flask_testing
import json
from helper import *

class TestApp(flask_testing.TestCase):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
    app.config["TESTING"] = True

    def create_app(self):
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()
        
        course1 = course(
            course_id = 1,
            course_name = "Test Course 1",
            description = "Test Description 1"
        )
        course2 = course(
            course_id = 2,
            course_name = "Test Course 2",
            description = "Test Description 2",
        )
        db.session.add(course1)
        db.session.add(course2)

        db.session.add(staff(
            staff_username = "Staff1",
            staff_name = "Staff 1",
            role = "Learner",
            department = "Ops",
            current_designation = "Manager"
        ))

        db.session.add(staff(
            staff_username = "Staff2",
            staff_name = "Staff 2",
            role = "Learner",
            department = "Ops",
            current_designation = "Manager"
        ))

        db.session.add(course_completion(
            course_id = 1,
            staff_username = "Staff1"
        ))

        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCourseCompletion(TestApp):
    def test_getCompletionByCourse(self):
        res = course_completion.getCompletionByCourse(1)
        expected = ["Staff1"]
        self.assertEqual(res, expected)
    
    def test_insert_course_completion(self):
        CC1 = course_completion(
            course_id = 1,
            staff_username = "Staff2"
        )
        res = course_completion.insert_course_completion(CC1)
        self.assertEqual(res,{"code": 200, "message": "Course marked as complete"})
    
    def test_insert_course_completion(self):
        res = course_completion.getStaffCompletion('Staff1')

        expected = {'data': 
                        {0: {'course_id': 1, 'staff_username': 'Staff1'}}
                    }
        self.assertEqual(res,expected)
    

if __name__ == "__main__":
    unittest.main()