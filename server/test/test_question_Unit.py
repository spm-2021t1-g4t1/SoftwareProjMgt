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


class TestQuestionClass(TestApp):
    def test_get_courseQues(self):
        aQuestion = Question(
            qid=1,
            ques_id=1,
            question="How is SPM IS212 doing today for YYC?",
            question_type="mcq",
        )
        db.session.add(aQuestion)
        db.session.commit()
        data = Question.get_courseQues(1)
        self.assertEqual(
            data["data"],
            [
                {
                    "qid": 1,
                    "ques_id": 1,
                    "question": "How is SPM IS212 doing today for YYC?",
                    "question_type": "mcq",
                }
            ],
        )

    def test_add_courseQuestion(self):
        Question.add_courseQuestion(
            1, 1, "How is SPM IS212 doing today for YYC?", "mcq"
        )
        data = Question.get_a_question(1, 1)
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 1,
                "question": "How is SPM IS212 doing today for YYC?",
                "question_type": "mcq",
            },
        )

    def test_update_specificQuestion(self):
        Question.add_courseQuestion(
            1, 1, "How is SPM IS212 doing today for YYC?", "mcq"
        )
        Question.update_specificQuestion(
            1, 1, "How do we ensure that the workstation is switched on??"
        )
        data = Question.get_a_question(1, 1)
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 1,
                "question": "How do we ensure that the workstation is switched on??",
                "question_type": "mcq",
            },
        )

    def test_get_a_question(self):
        aQuestion = Question(
            qid=1,
            ques_id=1,
            question="How is SPM IS212 doing today for YYC?",
            question_type="mcq",
        )
        db.session.add(aQuestion)
        db.session.commit()
        data = Question.get_a_question(1, 1)
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 1,
                "question": "How is SPM IS212 doing today for YYC?",
                "question_type": "mcq",
            },
        )
        self.assertEqual(data["code"], 200)

    

if __name__ == "__main__":
    unittest.main()
