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
            course_id=2,
            course_name='Programming for Xerox WorkCentre with CardAccess and Integration',
            description='This course will equip you with basic programming skills as well as software integration.'
            ),
            classes(
            course_id=2,
            class_no=1,
            start_date=datetime(2012, 3, 3, 10, 10, 10),
            end_date=datetime(2012, 3, 3, 10, 10, 10),
            start_time=datetime(2012, 3, 3, 10, 10, 10),
            end_time=datetime(2012, 3, 3, 10, 10, 10),
            class_size=40,
            trainer_name='stevejobs'
            ),
            lesson(
            course_id = 2,
            class_no = 1,
            lesson_no = 1,
            lesson_name = "Test Lesson Name",
            lesson_description = "Test Description",
            quiz_assigned_id = 1),
            
            lesson(
            course_id=2,
            class_no=1,
            lesson_no=2,
            lesson_name="Lesson 2 - Programming for Xerox WorkCentre with CardAccess and Integration",
            lesson_description="The second lesson of Programming for Xerox WorkCentre with CardAccess and Integration",
            quiz_assigned_id = 2
            ),
            
            lesson_materials(
            course_id = 2,
            class_no = 1 ,
            lesson_no = 1, 
            course_material_title = "Test Material 1", 
            link = "./somewhere"),

            lesson_completion(
            course_id=2,
            class_no=1,
            lesson_no=1,
            staff_username='darrelwilde'
            ),

            Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="james_smith",
            duration="00:00:00",
            )

        ]

        db.session.bulk_save_objects(Objects)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testGet_all_lesson(TestApp):
    def testMethods(self):
        expected = {'data': [
                {   'course_id': 2, 
                    'class_no': 1, 
                    'lesson_no': 1, 
                    'lesson_name': 'Test Lesson Name', 
                    'lesson_description': 'Test Description', 
                    'lesson_materials': [
                        {'course_id': 2, 'class_no': 1, 'lesson_no': 1, 'course_material_title': 'Test Material 1', 'link': './somewhere'}
                    ], 
                    'quiz_assigned_id': 1   }, 
                {   'course_id': 2, 
                    'class_no': 1, 
                    'lesson_no': 2, 
                    'lesson_name': 'Lesson 2 - Programming for Xerox WorkCentre with CardAccess and Integration', 
                    'lesson_description': 'The second lesson of Programming for Xerox WorkCentre with CardAccess and Integration', 
                    'lesson_materials': [], 
                    'quiz_assigned_id': 2}
                    ], 'code': 200}

        self.assertEqual(lesson.get_all_lessons(),expected)
    
    def testGetRoute(self):
        data = self.client.get(f"/lesson")
        self.assert200(data)

class testGet_lessons(TestApp):
    def testMethods(self):
        res = lesson.get_lesson_of_quiz(1)
        expected = {'data': {
                        'course_id': 2, 
                        'class_no': 1, 
                        'lesson_no': 1, 
                        'lesson_name': 'Test Lesson Name', 
                        'lesson_description': 'Test Description', 
                        'lesson_materials': [
                            {
                                'course_id': 2, 
                                'class_no': 1, 
                                'lesson_no': 1, 
                                'course_material_title': 'Test Material 1', 
                                'link': './somewhere'
                            }
                        ], 'quiz_assigned_id': 1}, 'code': 200}
        self.assertEqual(res, expected)
    
    def testGetRoute(self):
        data = self.client.get(f"/get_lesson_of_quiz/1")
        self.assert200(data)
    
class testAssign_quiz_to_lesson(TestApp):
    def testMethods(self):
        res = lesson.save_quiz_to_lesson(2,1,1,3)
        expected = {
                    'data': {
                        'course_id': 2, 
                        'class_no': 1, 
                        'lesson_no': 1, 
                        'lesson_name': 'Test Lesson Name', 
                        'lesson_description': 'Test Description', 
                        'lesson_materials': [
                            {'course_id': 2, 
                            'class_no': 1, 
                            'lesson_no': 1, 
                            'course_material_title': 'Test Material 1', 
                            'link': './somewhere'}
                        ], 
                            'quiz_assigned_id': 3}, 
                    'code': 200}

        self.assertEqual(res, expected)
    
    def testGetRoute(self):
        data = self.client.get(f"/update_assign_quiz/2/1/1/3")
        self.assert200(data)

class testGet_quiz_for_lesson(TestApp):
    def testMethods(self):
        quizNo = lesson.get_quiz_for_lesson(2,1,1)
        self.assertEqual(quizNo, 1)
        
        quiz_info = Quiz.get_one_quiz(quizNo)
        expected = {
                'data': {
                    'quiz_id': 1, 
                    'quiz_name': 'Fundamentals of Xerox WorkCentre 7845', 
                    'description': 'SECTION 1 of Xerox WorkCentre 7845', 
                    'uploader': 'james_smith', 
                    'duration': '00:00:00', 
                    'question': []}, 
                'code': 200}

        self.assertEqual(quiz_info, expected)
    
    def testGetRoute(self):
        data = self.client.get("/get_assigned_quiz/2/1/1")
        self.assert200(data, 200)


if __name__ == "__main__":
    unittest.main()
