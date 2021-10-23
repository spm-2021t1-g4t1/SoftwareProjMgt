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
            classes = [one_class]
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
            ]
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
            'learning_objective': ['Learning Objective 3', 'Learning Objective 4']
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
                'classes': []
            }, 
            {
                'course_id': 2, 
                'course_name': 'Test Course 2', 
                'description': 'Test Description 2', 
                'learning_objective': ['Learning Objective 3', 'Learning Objective 4'], 
                'classes': []
            }
        ]
    }
        self.assertEqual(len(courseList["data"]), 2)
        print(courseList)
        self.assertEqual(courseList, expected)

    def test_get_specificCourse(self):
        result = course.get_specificCourse(1)
        expected = {
            'data': 
                {'course_id': 1, 
                'course_name': 'Test Course 1', 
                'description': 'Test Description 1', 
                'learning_objective': ['Learning Objective 1', 'Learning Objective 2']
                }
            }
        self.assertEqual(result, expected)
    
    def test_getInvalidCourse(self):
        # this really shouldn't be an attributeerror but we'll refactor this later i suppose
        with self.assertRaises(AttributeError):
            course.get_specificCourse(3)


if __name__ == "__main__":
    unittest.main()