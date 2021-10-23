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
        aStaff = staff(
            staff_username = 'coreyroberts',
            staff_name = 'Corey Roberts',
            role = 'Learner',
            department = 'Operation',
            current_designation = 'Engineer'
        )
        db.session.add(aStaff)
        db.session.commit()
        aStaff2 = staff(
            staff_username = 'hello',
            staff_name = 'Corey Roberts',
            role = 'Learner',
            department = 'Operation',
            current_designation = 'Engineer'
        )
        db.session.add(aStaff2)
        db.session.commit()

        # aCourse = course(
        #     course_id = 1,
        #     course_name = 'course1',
        #     description = 'description',
        #     learning_objective = 'learning objective',
        #     classes = 
        # )
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testClassEnrollment(TestApp):
    def testGetClassList(self):
        aStudent1 = classEnrolment(
            staff_username = 'coreyroberts',
            course_id = 1,
            class_no = 1
        )
        aStudent2 = classEnrolment(
            staff_username = 'hello',
            course_id = 1,
            class_no = 1
        )

        db.session.add(aStudent1)
        db.session.add(aStudent2)
        db.session.commit()

        data = self.client.get(f"/enrolment/{1}/{1}")
        insertedStudents = data.json["data"]

        # print(insertedStudents)
        # print(insertedStudents['0'])

        self.assertEqual(insertedStudents['0']['staff_username'], 'coreyroberts')
        self.assertEqual(insertedStudents['1']['staff_username'], 'hello')
    

    # def testGetStaffEnrollment(self):
    #     aStudent1 = classEnrolment(
    #         staff_username = 'coreyroberts',
    #         course_id = 1,
    #         class_no = 1
    #     )
    #     aStudent2 = classEnrolment(
    #         staff_username = 'coreyroberts',
    #         course_id = 2,
    #         class_no = 2
    #     )
    #     db.session.add(aStudent1)
    #     db.session.add(aStudent2)
    #     db.session.commit()

    #     data = self.client.get(f"/enrolment/coreyroberts")
    #     # insertedStaff = data.json['data']
    #     print(data)



if __name__ == "__main__":
    unittest.main()
