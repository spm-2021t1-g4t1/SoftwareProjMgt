# Done by Chuen Kai
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
    
    def test_view_all_json(self):
        one_class = classes(course_id=3, class_no=1, start_date='2021-09-01', end_date='2021-09-01', class_size=15)
        c = course(
            course_id = 3,
            course_name = "Test Course 3",
            description = "Test Description 3",
            learning_objective = [learningObjective(course_id=3, learning_objective="Learning Objective 3"), learningObjective(course_id=3, learning_objective="Learning Objective 4")],
            classes = [one_class],
            prerequisite_courses = []
        )

        expected = {
            'course_id': 3, 
            'course_name': 'Test Course 3', 
            'description': 'Test Description 3', 
            'learning_objective': ['Learning Objective 3', 'Learning Objective 4'], 
            'classes': [
                {'course_id': 3, 
                'class_no': 1, 
                'start_date': '2021-09-01', 
                'end_date': '2021-09-01', 
                'start_time': 'None', 
                'end_time': 'None', 
                'class_size': 15, 
                'trainer_name': None, 
                'lesson': []
                }
            ],
            'prerequisite_courses': []
        }
        self.assertEqual(c.view_all_json(), expected)

    def test_view_all_json(self):
        one_class = classes(course_id=3, class_no=1, start_date='2021-09-01', end_date='2021-09-01', class_size=15)
        c = course(
            course_id = 3,
            course_name = "Test Course 3",
            description = "Test Description 3",
            learning_objective = [learningObjective(course_id=3, learning_objective="Learning Objective 3"), learningObjective(course_id=3, learning_objective="Learning Objective 4")],
            classes = [one_class],
            prerequisite_courses = []
        )

        expected = {
            'course_id': 3, 
            'course_name': 'Test Course 3', 
            'description': 'Test Description 3', 
            'learning_objective': ['Learning Objective 3', 'Learning Objective 4'], 
            'classes': [
                {'course_id': 3, 
                'class_no': 1, 
                'start_date': '2021-09-01', 
                'end_date': '2021-09-01', 
                'start_time': 'None', 
                'end_time': 'None', 
                'class_size': 15, 
                'trainer_name': None, 
                'lesson': []
                }
            ],
            'prerequisite_courses': []
        }
        self.assertEqual(c.view_all_json(), expected)

    def test_json(self):
        c = course(
            course_id = 3,
            course_name = "Test Course 3",
            description = "Test Description 3",
            learning_objective = [learningObjective(course_id=3, learning_objective="Learning Objective 3"), learningObjective(course_id=3, learning_objective="Learning Objective 4")],
            classes = []
        )
        expected = {
            'course_id': 3, 
            'course_name': 'Test Course 3', 
            'description': 'Test Description 3', 
            'learning_objective': ['Learning Objective 3', 'Learning Objective 4'],
            'prerequisite_courses': []
            }
        self.assertEqual(c.json(), expected)

    def test_get_listOfCourse(self):
        courseList = course.get_listOfCourse([])
        expected = {'data': 
        [
            {
                'course_id': 1, 
                'course_name': 'Test Course 1', 
                'description': 'Test Description 1', 
                'learning_objective': ['Learning Objective 1', 'Learning Objective 2'], 
                'prerequisite_courses': [],
                'classes': [
                    {'course_name': 'Test Course 1',
                    'course_id': 1, 
                    'class_no': 1, 
                    'start_date': (datetime(2021,9,1).replace(hour=0, minute=0, second=0, microsecond=0)), 
                    'end_date': (datetime(2021,9,2).replace(hour=0, minute=0, second=0, microsecond=0)), 
                    'start_time': 'None', 
                    'end_time': 'None', 
                    'class_size': 15, 
                    'trainer_name': None, 
                    'selfenrol_start': None, 
                    'selfenrol_end': None
                    }]
                
            }, 
            {
                'course_id': 2, 
                'course_name': 'Test Course 2', 
                'description': 'Test Description 2', 
                'learning_objective': ['Learning Objective 3', 'Learning Objective 4'], 
                'classes': [],
                'prerequisite_courses': []
            }
        ]
    }
        self.assertEqual(len(courseList["data"]), 2)
        self.assertEqual(courseList, expected)

    def test_get_specificCourse(self):
        result = course.get_specificCourse(1)
        expected = {
            'data': 
                {'course_id': 1, 
                'course_name': 'Test Course 1', 
                'description': 'Test Description 1', 
                'learning_objective': ['Learning Objective 1', 'Learning Objective 2'],
                'prerequisite_courses': []
                }
            }
        self.assertEqual(result, expected)
    
    def test_getInvalidCourse(self):
        # this really shouldn't be an attributeerror but we'll refactor this later i suppose
        with self.assertRaises(AttributeError):
            course.get_specificCourse(3)

class Test_API(TestApp):
    def test_API_getCourse(self):
        res = self.client.get("/course/1")
        expected = {
            'course_id': 1, 
            'course_name': 'Test Course 1', 
            'description': 'Test Description 1', 
            'learning_objective': ['Learning Objective 1', 'Learning Objective 2'],
            'prerequisite_courses': []
        }
        self.assertEqual(res.json['data'], expected)
    
    def test_API_getInvalidCourse(self):
        with self.assertRaises(AttributeError):
            self.client.get("/course/3")
    
    def test_API_getClass(self):
        res = self.client.get("/course/1/1")
        expected = {
            'classes': [{
                'class_no': 1, 
                'class_size': 15, 
                'course_id': 1, 
                'end_date': '2021-09-02 00:00:00', 
                'end_time': 'None', 
                'start_date': '2021-09-01 00:00:00', 
                'start_time': 'None', 
                'trainer_name': None
                }], 
            'course_id': 1, 
            'course_name': 'Test Course 1', 
            'description': 'Test Description 1', 
            'learning_objective': ['Learning Objective 1', 'Learning Objective 2']
            }
        # print(res.json["data"])
        self.assertEqual(res.json["data"], expected)

    def test_Get_Prerequisite_Courses(self):
        db.session.add(course_prerequisite(
            course_id=2, 
            prerequisite_course_id = 1))
        db.session.commit()

        res = course.get_prerequisite_courses(2)
        expected = {'data': [1]}
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()