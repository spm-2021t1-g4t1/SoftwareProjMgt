import unittest
import flask_testing
import json
from datetime import datetime
from helper import *

from model.lesson import *
from model.quiz_attempts import *


class TestApp(flask_testing.TestCase):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {}
    app.config["TESTING"] = True

    def create_app(self):
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()
        aCourse = course(
            course_id=2,
            course_name='Programming for Xerox WorkCentre with CardAccess and Integration',
            description='This course will equip you with basic programming skills as well as software integration.'
        )
        db.session.add(aCourse)
        db.session.commit()

        aClass = classes(
            course_id=2,
            class_no=1,
            start_date=datetime(2012, 3, 3, 10, 10, 10),
            end_date=datetime(2012, 3, 3, 10, 10, 10),
            start_time=datetime(2012, 3, 3, 10, 10, 10),
            end_time=datetime(2012, 3, 3, 10, 10, 10),
            class_size=40,
            trainer_name='stevejobs'
        )

        db.session.add(aClass)
        db.session.commit()

        aLesson = lesson(
            course_id=2,
            class_no=1,
            lesson_no=1,
            lesson_name="Lesson 1 - Programming for Xerox WorkCentre with CardAccess and Integration",
            lesson_description="The first lesson of Programming for Xerox WorkCentre with CardAccess and Integration"
        )
        db.session.add(aLesson)
        db.session.commit()

        aLesson2 = lesson(
            course_id=2,
            class_no=1,
            lesson_no=2,
            lesson_name="Lesson 2 - Programming for Xerox WorkCentre with CardAccess and Integration",
            lesson_description="The second lesson of Programming for Xerox WorkCentre with CardAccess and Integration"
        )
        db.session.add(aLesson2)
        db.session.commit()

        aLesson3 = lesson(
            course_id=2,
            class_no=1,
            lesson_no=3,
            lesson_name="Lesson 3 - Programming for Xerox WorkCentre with CardAccess and Integration",
            lesson_description="The last lesson of Programming for Xerox WorkCentre with CardAccess and Integration"
        )
        db.session.add(aLesson3)
        db.session.commit()

        aLesson4 = lesson(
            course_id=2,
            class_no=1,
            lesson_no=4,
            lesson_name="Lesson 4 - Programming for Xerox WorkCentre with CardAccess and Integration",
            lesson_description="The last lesson of Programming for Xerox WorkCentre with CardAccess and Integration"
        )
        db.session.add(aLesson4)
        db.session.commit()

        aLesson5 = lesson(
            course_id=2,
            class_no=1,
            lesson_no=5,
            lesson_name="Lesson 5 - Programming for Xerox WorkCentre with CardAccess and Integration",
            lesson_description="The last lesson of Programming for Xerox WorkCentre with CardAccess and Integration"
        )
        db.session.add(aLesson5)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestGetLessons(TestApp):
    def test_get_lessons_0_lessons_completed_0_quizzes_passed(self):
        response = self.client.get(f"/lesson/2/1/darrelwilde")
        self.assertEqual(len(response.json['data']['classes'][0]['lesson']), 1)

    def test_get_lessons_1_lesson_completed_0_quizzes_passed(self):
        aLessonCompletion = lesson_completion(
            course_id=2,
            class_no=1,
            lesson_no=1,
            staff_username='darrelwilde'
        )
        db.session.add(aLessonCompletion)
        db.session.commit()

        response = self.client.get(f"/lesson/2/1/darrelwilde")
        self.assertEqual(len(response.json['data']['classes'][0]['lesson']), 1)

    def test_get_lessons_3_lessons_completed_3_quizzes_passed(self):
        aLessonCompletion = lesson_completion(
            course_id=2,
            class_no=1,
            lesson_no=1,
            staff_username='darrelwilde'
        )
        db.session.add(aLessonCompletion)
        db.session.commit()

        aLessonCompletion2 = lesson_completion(
            course_id=2,
            class_no=1,
            lesson_no=2,
            staff_username='darrelwilde'
        )

        db.session.add(aLessonCompletion2)
        db.session.commit()

        aLessonCompletion3 = lesson_completion(
            course_id=2,
            class_no=1,
            lesson_no=3,
            staff_username='darrelwilde'
        )
        db.session.add(aLessonCompletion3)
        db.session.commit()

        aQuizAttempt = quiz_attempts(
            course_id=2,
            class_no=1,
            lesson_no=1,
            staff_username='darrelwilde',
            quiz_score=89
        )
        db.session.add(aQuizAttempt)
        db.session.commit()

        aQuizAttempt2 = quiz_attempts(
            course_id=2,
            class_no=1,
            lesson_no=2,
            staff_username='darrelwilde',
            quiz_score=89
        )
        db.session.add(aQuizAttempt2)
        db.session.commit()

        aQuizAttempt3 = quiz_attempts(
            course_id=2,
            class_no=1,
            lesson_no=3,
            staff_username='darrelwilde',
            quiz_score=89
        )
        db.session.add(aQuizAttempt3)
        db.session.commit()

        response = self.client.get(f"/lesson/2/1/darrelwilde")
        self.assertEqual(len(response.json['data']['classes'][0]['lesson']), 4)

