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
        q1 = Question(
            qid=1,
            ques_id=1,
            question="How is SPM IS212 doing today for YYC?",
            question_type="mcq",
        )
        q2 = Question(
            qid=1,
            ques_id=2,
            question="SPM TRUUE FALSE CHECKER",
            question_type="tf",
        )
        db.session.add(q1)
        db.session.add(q2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestQuestionClass(TestApp):
    def test_get_courseQues(self):
        data = Question.get_courseQues(1)
        self.assertEqual(
            data["data"],
            [
                {
                    "qid": 1,
                    "ques_id": 1,
                    "question": "How is SPM IS212 doing today for YYC?",
                    "question_option": [],
                    "question_type": "mcq",
                },
                {
                    "qid": 1,
                    "ques_id": 2,
                    "question": "SPM TRUUE FALSE CHECKER",
                    "question_option": [],
                    "question_type": "tf",
                },
            ],
        )
        self.assertEqual(len(data["data"]), 2)

    def test_add_courseQuestion(self):
        Question.add_courseQuestion(1, 3, "xxxx_test", "mcq")
        data = Question.get_a_question(1, 3)
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 3,
                "question": "xxxx_test",
                "question_option": [],
                "question_type": "mcq",
            },
        )
        self.assertEqual(data["code"], 200)

    def test_update_specificQuestion(self):
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
                "question_option": [],
                "question_type": "mcq",
            },
        )

    def test_get_a_question(self):
        data = Question.get_a_question(1, 1)
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 1,
                "question": "How is SPM IS212 doing today for YYC?",
                "question_option": [],
                "question_type": "mcq",
            },
        )
        self.assertEqual(data["code"], 200)


if __name__ == "__main__":
    unittest.main()
