# Done by Shun Hui
# shunhui.lee.2019
import unittest
import flask_testing
import json
from datetime import datetime, timedelta
from helper import *

from model.lesson import *
from model.lesson_quiz_attempts import *


class TestApp(flask_testing.TestCase):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
    app.config["TESTING"] = True

    def create_app(self):
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()
        objects = [
            course(
            course_id = 1,
            course_name = "Test Course 1",
            description = "Test Description 1"
            ),
            classes(course_id = 1, 
                    class_no = 1, 
                    start_date = datetime.today().date() + timedelta(days=-2), 
                    end_date = datetime.today().date() +  timedelta(days=-1), 
                    start_time = None,
                    end_time = None,
                    class_size = 40, 
                    trainer_name = 'stevejobs',
                    selfenrol_start = None,
                    selfenrol_end = None,
                    finalquiz_id = 1, 
                    lesson = []
            ),
            
            lesson(
            course_id = 1,
            class_no = 1,
            lesson_no = 1,
            lesson_name = "Test Lesson Name",
            lesson_description = "Test Description",
            quiz_assigned_id = 1),
            lesson(
            course_id = 1,
            class_no = 1,
            lesson_no = 2,
            lesson_name = "Test Lesson Name 2",
            lesson_description = "Test Description 2",
            quiz_assigned_id = 1),
            lesson_quiz_attempts(
                course_id = 1,
                class_no = 1,
                lesson_no = 1,
                staff_username = 'darrelwilde',
                quiz_score = 60
            ),
            lesson_quiz_attempts(
                course_id = 1,
                class_no = 1,
                lesson_no = 2,
                staff_username = 'darrelwilde',
                quiz_score = 80
            )
        ]
        db.session.bulk_save_objects(objects)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class test_getListOfQuizAttemptsByStaff(TestApp):
    def testMethod(self):
        res = lesson_quiz_attempts.get_listOfQuizAttemptsByStaff(1,1,'darrelwilde')
        expected = {
            'data': [{
                'course_id': 1, 
                'class_no': 1, 
                'lesson_no': 1, 
                'staff_username': 'darrelwilde', 
                'quiz_score': 60
            }, 
            {
                'course_id': 1, 
                'class_no': 1, 
                'lesson_no': 2, 
                'staff_username': 'darrelwilde', 
                'quiz_score': 80
            }], 
            'code': 200}
        self.assertEqual(res, expected)

        failres = lesson_quiz_attempts.get_specificLessonQuizAttempt(1,1,1,"simon")
        self.assertEqual(failres, {'data': None, 'code': 404})

class test_get_specificLessonQuizAttempt(TestApp):
    def testMethod(self):
        res = lesson_quiz_attempts.get_specificLessonQuizAttempt(1,1,1,"darrelwilde")
        expected = {
            'data': {
                'course_id': 1, 
                'class_no': 1, 
                'lesson_no': 1, 
                'staff_username': 'darrelwilde' ,
                'quiz_score': 60}, 
            'code': 200}
        self.assertEqual(res, expected)

        failres = lesson_quiz_attempts.get_specificLessonQuizAttempt(1,1,1,"simon")
        self.assertEqual(failres, {'data': None, 'code': 404})

class test_updateQuizScore(TestApp):
    def testMethod(self):
        res = lesson_quiz_attempts.update_lesson_quizscore(1, 1, 1, "darrelwilde", 70)
        expected = {'data': 70, 'code': 200}
        self.assertEqual(res, expected)

    def testGetRoute(self):
        data = self.client.get(f"/update_quiz_score/1/1/1/darrelwilde/70")
        self.assert200(data)


if __name__ == "__main__":
    unittest.main()
