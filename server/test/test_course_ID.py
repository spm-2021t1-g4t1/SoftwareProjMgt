from datetime import datetime
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
        
        # Set up course objects
        course1 = course(
            course_id = 1,
            course_name = "Test Course 1",
            description = "Test Description 1"
        )
        course2 = course(
            course_id = 2,
            course_name = "Test Course 2",
            description = "Test Description 2"
        )
        db.session.add(course1)
        db.session.add(course2)

        # Set up learning objectives that correspond to each course
        for i in range(4):
            db.session.add(learningObjective(
                course_id = i // 2 + 1,
                learning_objective = f"Learning Objective {i + 1}"
            ))

        db.session.add(classes(
            course_id=1, 
            class_no=1, 
            start_date=datetime(2021,9,1), 
            end_date=datetime(2021,9,2), 
            class_size=15))

        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCourse_DB(TestApp):
    def test_get_one_course(self):
        response = self.client.get(f"/course/1")
        self.assert200(response)
        data = response.json
        self.assertEqual(data['data'], 
        {'course_id': 1, 'course_name': 'Test Course 1', 'description': 'Test Description 1', 'learning_objective': ['Learning Objective 1', 'Learning Objective 2'], 'prerequisite_courses': []}
        )
        self.assertEqual(len(data), 1)

    def test_get_specificCourseDetail(self):
        response = self.client.get(f"/course/1/1")
        self.assert200(response)
        data = response.json
        self.assertEqual(data['data'], 
        {'classes': [{'class_no': 1, 'class_size': 15, 'course_id': 1, 'end_date': '2021-09-02 00:00:00', 'end_time': 'None', 'start_date': '2021-09-01 00:00:00', 'start_time': 'None', 'trainer_name': None}], 
        'course_id': 1, 'course_name': 
        'Test Course 1', 
        'description': 'Test Description 1',
        'learning_objective': ['Learning Objective 1', 'Learning Objective 2']}
        )
        self.assertEqual(len(data), 1)

    def test_get_allCourse(self):
        response = self.client.get(f"/course/getList")
        self.assert200(response)
        data = response.json
        self.assertEqual(data['data'], 
        [{'classes': [{'class_no': 1, 'class_size': 15, 'course_id': 1, 'course_name': 'Test Course 1', 'end_date': 'Thu, 02 Sep 2021 00:00:00 GMT', 'end_time': 'None', 'selfenrol_end': None, 'selfenrol_start': None, 'start_date': 'Wed, 01 Sep 2021 00:00:00 GMT', 'start_time': 'None', 'trainer_name': None}], 
        'course_id': 1, 
        'course_name': 'Test Course 1', 
        'description': 'Test Description 1', 
        'learning_objective': ['Learning Objective 1', 'Learning Objective 2'], 'prerequisite_courses': []}, {'classes': [], 
        'course_id': 2, 
        'course_name': 'Test Course 2', 
        'description': 'Test Description 2', 
        'learning_objective': ['Learning Objective 3', 'Learning Objective 4'], 
        'prerequisite_courses': []}]
        )


if __name__ == "__main__":
    unittest.main()