# Done by Shun Hui
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
            final_quiz_attempts(
                course_id = 1,
                class_no = 1,
                staff_username = 'darrelwilde',
                quiz_score = 60
            ),
        ]
        db.session.bulk_save_objects(objects)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class test_Exam(TestApp):
    def testMethod(self):
        res = final_quiz_attempts.get_specificFinalQuizAttempt(1,1,'darrelwilde')
        expected = {
            'data': {
                'course_id': 1, 
                'class_no': 1, 
                'staff_username': 'darrelwilde', 
                'quiz_score': 60}, 
            'code': 200}
        self.assertEqual(res,expected)

        Failres = final_quiz_attempts.get_specificFinalQuizAttempt(1,1,'Simon')
        self.assertEqual(Failres,{'data': None, 'code': 404})

    def testGetRoute(self):
        data = self.client.get(f"/exam/1/1/darrelwilde")
        self.assert200(data)

class test_updateFinalQuizScore(TestApp):
    def testMethod(self):
        res = final_quiz_attempts.update_finalquizscore(1,1,'darrelwilde', 70)
        expected = {'data': 70, 'code': 200}
        self.assertEqual(res,expected)

    def testGetRoute(self):
        data = self.client.get(f"/update_finalquiz_score/1/1/darrelwilde/70")
        self.assert200(data)

if __name__ == "__main__":
    unittest.main()
