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
        for i in range(1, 4):
            db.session.add(
                QuizOptions(
                    qid=1,
                    ques_id=1,
                    opts_id=i,
                    is_right=0,
                    qopt="testing " + str(i),
                )
            )
        db.session.add(
            QuizOptions(
                qid=1,
                ques_id=1,
                opts_id=4,
                is_right=1,
                qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
            )
        )
        db.session.add(q2)
        db.session.add(
            QuizOptions(
                qid=1,
                ques_id=2,
                opts_id=1,
                is_right=1,
                qopt="True",
            )
        )
        db.session.add(
            QuizOptions(
                qid=1,
                ques_id=2,
                opts_id=2,
                is_right=0,
                qopt="False",
            )
        )
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestQuestion(TestApp):
    def test_get_all_ques(self):
        response = self.client.get(f"/quiz_ques/{1}")
        dataObj = response.json
        self.assertEqual(dataObj["code"], 200)
        self.assertEqual(len(dataObj["data"]), 2)
        self.assertEqual(len(dataObj["data"][0]["question_option"]), 4)
        self.assertEqual(len(dataObj["data"][1]["question_option"]), 2)
        # self.assertEqual(dataObj['data'], 2)

    def test_addQuestion_negative(self):
        # CANNOT ADD WHEN QUES ID EXIST
        request_body = {
            "qid": 1,
            "ques_id": 1,
            "question": "How is SPM IS212 doing today for Booppss?",
            "question_option": [],
            "question_type": "mcq",
        }
        response = self.client.post(
            f"/add_ques/{1}",
            data=json.dumps(request_body),
            content_type="application/json",
        )
        dataObj = response.json
        self.assertEqual(dataObj["data"]["status"], 500)

    def test_addQuestion_positive(self):
        # ADD WHEN QUES ID DOES NOT EXIST
        request_body = {
            "qid": 1,
            "ques_id": 3,
            "question": "How is SPM IS212 doing today for Booppss?",
            "question_option": [],
            "question_type": "mcq",
        }
        response = self.client.post(
            f"/add_ques/{1}",
            data=json.dumps(request_body),
            content_type="application/json",
        )
        dataObj = response.json
        self.assertEqual(dataObj["data"]["status"], 200)

    def test_delete_question(self):
        response = self.client.get(f"/ques_delete/{1}/{1}")

        self.assertEqual(response.json["data"]["status"], 200)
        checkEntry = self.client.get(f"/quiz_ques/{1}")
        data = checkEntry.json
        print(data)
        self.assertEqual(len(data["data"]), 1)


if __name__ == "__main__":
    unittest.main()
