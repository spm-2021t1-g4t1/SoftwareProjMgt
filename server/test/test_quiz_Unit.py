# Done by Yao Cong
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
        q1 = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="james_smith",
            duration="00:30:43",
        )
        db.session.add(q1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestQuizClass(TestApp):
    def test_get_listofQuiz(self):
        data = Quiz.get_listofQuiz()
        self.assertEqual(data["code"], 200)
        self.assertEqual(
            data["data"],
            [
                {
                    "quiz_id": 1,
                    "quiz_name": "Fundamentals of Xerox WorkCentre 7845",
                    "description": "SECTION 1 of Xerox WorkCentre 7845",
                    "uploader": "james_smith",
                    "question": [],
                    "duration": "00:30:43",
                }
            ],
        )
        self.assertEqual(len(data["data"]), 1)

    def test_get_quiz_details(self):
        data = Quiz.get_quiz_details(1)
        self.assertEqual(data["code"], 200)
        self.assertEqual(
            data["data"],
            [
                {
                    "quiz_id": 1,
                    "quiz_name": "Fundamentals of Xerox WorkCentre 7845",
                    "description": "SECTION 1 of Xerox WorkCentre 7845",
                    "uploader": "james_smith",
                    "question": [],
                    "duration": "00:30:43",
                }
            ],
        )

    def test_delete_quiz(self):
        Quiz.delete_quiz(1)
        self.assertEqual(Quiz.get_one_quiz(1)["code"], 500)
        self.assertEqual(Quiz.get_one_quiz(1)["data"], None)
        data = Quiz.get_quiz_details(1)
        self.assertEqual(data["data"], [])

    def test_save_quizDuration(self):
        saved_quiz = Quiz.save_quizDuration(1, "00:50:00")
        self.assertEqual(saved_quiz["code"], 200)
        self.assertEqual(saved_quiz["data"], "00:50:00")

    def test_saveQuizName(self):
        saved_quiz = Quiz.save_quizName(
            1,
            "Boop",
        )
        self.assertEqual(saved_quiz["code"], 200)
        self.assertEqual(saved_quiz["data"], "Boop")

    def test_create_quiz(self):
        test_create = Quiz.create_quiz(
            2,
            "TEST_SPM_2",
            "TEST_SPM_2",
            "james_smith",
            "00:45:00",
        )
        self.assertEqual(test_create["code"], 200)
        self.assertEqual(
            test_create["data"],
            {
                "quiz_id": 2,
                "quiz_name": "TEST_SPM_2",
                "description": "TEST_SPM_2",
                "uploader": "james_smith",
                "question": [],
                "duration": "00:45:00",
            },
        )


if __name__ == "__main__":
    unittest.main()
