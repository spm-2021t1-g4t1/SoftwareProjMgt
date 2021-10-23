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


class TestQuizOptionsClass(TestApp):
    def test_getQuesOpt(self):
        anOption = QuizOptions(
            quiz_id=1,
            ques_id=1,
            opts_id=1,
            is_right=1,
            qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
        )
        db.session.add(anOption)
        db.session.commit()
        data = QuizOptions.get_QuesOpt(1, 1)
        self.assertEqual(
            data["data"],
            [
                {
                    "quiz_id": 1,
                    "ques_id": 1,
                    "opts_id": 1,
                    "is_right": 1,
                    "qopt": "Press the On button for the Workstation, clean the nozzle and restart the machine",
                }
            ],
        )

    def test_get_specificOption(self):
        anOption = QuizOptions(
            quiz_id=1,
            ques_id=1,
            opts_id=1,
            is_right=1,
            qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
        )
        db.session.add(anOption)
        db.session.commit()
        data = QuizOptions.get_specificOption(1, 1, 1)
        self.assertEqual(
            data["data"],
            {
                "quiz_id": 1,
                "ques_id": 1,
                "opts_id": 1,
                "is_right": 1,
                "qopt": "Press the On button for the Workstation, clean the nozzle and restart the machine",
            },
        )

    def test_remove_opt(self):
        anOption = QuizOptions(
            quiz_id=1,
            ques_id=1,
            opts_id=1,
            is_right=1,
            qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
        )
        db.session.add(anOption)
        db.session.commit()
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
        anOption = QuizOptions(
            quiz_id=1,
            ques_id=1,
            opts_id=1,
            is_right=1,
            qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
        )
        db.session.add(anOption)
        db.session.commit()
        QuizOptions.update_quiz_options(1, 1, 1, 0, "Restart the machine")
        data = QuizOptions.get_specificOption(1, 1, 1)
        self.assertEqual(
            data["data"],
            {
                "quiz_id": 1,
                "ques_id": 1,
                "opts_id": 1,
                "is_right": 0,
                "qopt": "Restart the machine",
            },
        )
        self.assertEqual(data["code"], 200)

    def test_insert_quiz_options(self):
        QuizOptions.insert_quiz_options(1, 1, 1, 1, "Restart the machine")
        data = QuizOptions.get_specificOption(1, 1, 1)
        self.assertEqual(
            data["data"],
            {
                "quiz_id": 1,
                "ques_id": 1,
                "opts_id": 1,
                "is_right": 1,
                "qopt": "Restart the machine",
            },
        )

    def test_remove_all_opt(self):
        anOption = QuizOptions(
            quiz_id=1,
            ques_id=1,
            opts_id=1,
            is_right=1,
            qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
        )
        abOption = QuizOptions(
            quiz_id=1,
            ques_id=1,
            opts_id=2,
            is_right=0,
            qopt="Clean the nozzle and restart the machine",
        )
        db.session.add(anOption)
        db.session.add(abOption)
        db.session.commit()
        data = QuizOptions.remove_all_opt(1, 1)
        self.assertEqual(data["data"], "Removed")
        response = QuizOptions.get_QuesOpt(1, 1)
        self.assertEqual(response["data"], [])


if __name__ == "__main__":
    unittest.main()
