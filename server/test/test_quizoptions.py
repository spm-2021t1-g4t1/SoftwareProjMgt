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


class TestQuizOptionsClass(TestApp):
    def test_getQuesOpt(self):
        data = QuizOptions.get_QuesOpt(1, 1)
        self.assertEqual(len(data["data"]), 4)

    def test_get_specificOption(self):
        data = QuizOptions.get_specificOption(1, 1, 4)
        print(data["data"])
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 1,
                "opts_id": 4,
                "is_right": 1,
                "qopt": "Press the On button for the Workstation, clean the nozzle and restart the machine",
            },
        )

    def test_remove_opt(self):
        QuizOptions.remove_opt(1, 1, 1)
        data = QuizOptions.get_specificOption(1, 1, 1)
        self.assertEqual(
            data["data"],
            None,
        )
        self.assertEqual(
            data["code"],
            500,
        )

    def test_update_quiz_options(self):
        QuizOptions.update_quiz_options(1, 1, 4, 0, "Restart the machine")
        data = QuizOptions.get_specificOption(1, 1, 4)
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 1,
                "opts_id": 4,
                "is_right": 0,
                "qopt": "Restart the machine",
            },
        )
        self.assertEqual(data["code"], 200)

    def test_insert_quiz_options(self):
        QuizOptions.insert_quiz_options(1, 1, 5, 0, "Restart the machine")
        data = QuizOptions.get_specificOption(1, 1, 5)
        self.assertEqual(
            data["data"],
            {
                "qid": 1,
                "ques_id": 1,
                "opts_id": 5,
                "is_right": 0,
                "qopt": "Restart the machine",
            },
        )
        self.assertEqual(data["code"], 200)

    def test_remove_all_opt(self):
        data = QuizOptions.remove_all_opt(1, 1)
        self.assertEqual(data["data"], "Removed")
        response = QuizOptions.get_QuesOpt(1, 1)
        self.assertEqual(response["data"], [])


if __name__ == "__main__":
    unittest.main()
