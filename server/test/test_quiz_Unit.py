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

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestQuizClass(TestApp):
    def test_get_listofQuiz(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        db.session.commit()
        data = Quiz.get_listofQuiz()
        self.assertEqual(data["code"], 200)
        self.assertEqual(
            data["data"],
            [
                {
                    "quiz_id": 1,
                    "quiz_name": "Fundamentals of Xerox WorkCentre 7845",
                    "description": "SECTION 1 of Xerox WorkCentre 7845",
                    "uploader": "James Smith",
                    "duration": "00:30:43",
                }
            ],
        )

    def test_get_quiz_details(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        db.session.commit()
        data = Quiz.get_quiz_details(1)
        self.assertEqual(data["code"], 200)
        self.assertEqual(
            data["data"],
            [
                {
                    "quiz_id": 1,
                    "quiz_name": "Fundamentals of Xerox WorkCentre 7845",
                    "description": "SECTION 1 of Xerox WorkCentre 7845",
                    "uploader": "James Smith",
                    "duration": "00:30:43",
                }
            ],
        )

    def test_delete_quiz(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        Quiz.delete_quiz(1)
        db.session.commit()
        self.assertEqual(Quiz.get_one_quiz(1)["code"], 500)
        self.assertEqual(Quiz.get_one_quiz(1)["data"], None)

    def test_save_quiz(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundx WorkCentre 7845",
            description="SECTIOre 7845",
            uploader="Jath",
            duration="00:00:00",
        )
        db.session.add(aQuiz)
        saved_quiz = Quiz.save_quiz(
            1,
            "Fundamentals of Xerox WorkCentre 7845",
            "SECTION 1 of Xerox WorkCentre 7845",
            "James Smith",
            "00:30:43",
        )
        self.assertEqual(saved_quiz["code"], 200)

    def test_create_quiz(self):
        Quiz.create_quiz(
            1,
            "Fundamentals of Xerox WorkCentre 7845",
            "SECTION 1 of Xerox WorkCentre 7845",
            "James Smith",
            "00:30:43",
        )
        chk_quiz = Quiz.get_one_quiz(1)
        self.assertEqual(
            chk_quiz["data"],
            {
                "quiz_id": 1,
                "quiz_name": "Fundamentals of Xerox WorkCentre 7845",
                "description": "SECTION 1 of Xerox WorkCentre 7845",
                "uploader": "James Smith",
                "duration": "00:30:43",
            },
        )


if __name__ == "__main__":
    unittest.main()
