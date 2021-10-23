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


class TestQuestion(TestApp):
    def test_get_all_ques(self):
        aQuestion = Question(
            qid=1,
            ques_id=1,
            question="How is SPM IS212 doing today for YYC?",
            question_type="mcq",
        )
        db.session.add(aQuestion)
        db.session.commit()
        response = self.client.get(f"/quiz_ques/{1}")
        dataObj = response.json
        self.assertEqual(dataObj["code"], 200)
        self.assertEqual(
            dataObj["data"],
            [
                {
                    "qid": 1,
                    "ques_id": 1,
                    "question": "How is SPM IS212 doing today for YYC?",
                    "question_type": "mcq",
                }
            ],
        )

    def test_addQuestion_negative(self):
        request_body = {
            "qid": 1,
            "ques_id": 2,
            "question": "How is SPM IS212 doing today for YYC?",
            "question_type": "mcq",
        }
        response = self.client.post(
            f"/add_ques/{1}",
            data=json.dumps(request_body),
            content_type="application/json",
        )
        dataObj = response.json
        self.assertEqual(
            dataObj["data"]["status"],
            500,
        )
        checkEntry = self.client.get(f"/quiz_ques/{1}")
        data = checkEntry.json
        # print(data["data"])
        self.assertEqual(len(data["data"]), 0)

    def test_addQuestion_positive(self):
        request_body = {
            "qid": 1,
            "ques_id": 1,
            "question": "How is SPM IS212 doing today for YYC?",
            "question_type": "mcq",
        }
        response = self.client.post(
            f"/add_ques/{1}",
            data=json.dumps(request_body),
            content_type="application/json",
        )
        dataObj = response.json
        self.assertEqual(
            dataObj["data"]["status"],
            200,
        )
        checkEntry = self.client.get(f"/quiz_ques/{1}")
        data = checkEntry.json
        self.assertEqual(len(data["data"]), 1)

    def test_delete_question(self):
        aQuestion = Question(
            qid=1,
            ques_id=1,
            question="How is SPM IS212 doing today for YYC?",
            question_type="mcq",
        )
        db.session.add(aQuestion)
        db.session.commit()
        checkEntry = self.client.get(f"/quiz_ques/{1}")
        data = checkEntry.json
        self.assertEqual(len(data["data"]), 1)

        response = self.client.get(f"/ques_delete/{1}/{1}")
        self.assertEqual(response.json["data"]["status"], 200)

        checkEntry = self.client.get(f"/quiz_ques/{1}")
        data = checkEntry.json
        self.assertEqual(len(data["data"]), 0)


if __name__ == "__main__":
    unittest.main()
