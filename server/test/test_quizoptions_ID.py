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


class TestQuizOptions(TestApp):
    # def test_get_the_options(self):
    #     anOption = QuizOptions(
    #         quiz_id=1,
    #         ques_id=1,
    #         opts_id=1,
    #         is_right=True,
    #         qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
    #     )
    #     db.session.add(anOption)
    #     db.session.commit()
    #     response = self.client.get(f"/ques_opt/{1}/{1}")
    #     data = response.json["data"][0]
    #     self.assertEqual(response.json["code"], 200)
    #     self.assertEqual(data["quiz_id"], 1)
    #     self.assertEqual(data["ques_id"], 1)
    #     self.assertEqual(data["opts_id"], 1)
    #     self.assertEqual(data["is_right"], True)
    #     self.assertEqual(
    #         data["qopt"],
    #         "Press the On button for the Workstation, clean the nozzle and restart the machine",
    #     )

    def test_update_options(self):
        aQuestion = Question(
            qid=1,
            ques_id=1,
            question="How is SPM IS212 doing today for YYC?",
            question_type="mcq",
        )

        anOption = QuizOptions(
            quiz_id=1,
            ques_id=1,
            opts_id=1,
            is_right=1,
            qopt="Press the On button for the Workstation, clean the nozzle and restart the machine",
        )
        db.session.add(aQuestion)
        db.session.add(anOption)
        db.session.commit()
        # print(self.client.get(f"/ques_opt/{1}/{1}").json)

        update_question_body = {
            "question": "How do I troubleshoot for Xerox Workstation properly?",
            "optionsList": [
                {
                    "quiz_id": 1,
                    "ques_id": 1,
                    "opts_id": 1,
                    "is_right": 0,
                    "qopt": "Ensure that the workstation is switched On, Clean the nozzle and restart the machine",
                }
            ],
        }
        response = self.client.post(
            f"/ques_opt_update/{1}/{1}",
            data=json.dumps(update_question_body),
            content_type="application/json",
        )
        self.assertEqual(response.json["data"]["status"], 200)
        # print(response.json)
        chkdata = self.client.get(f"/ques_opt/{1}/{1}")
        # print(chkdata.json)
        first_entry = chkdata.json["data"][0]
        # print(first_entry)
        self.assertEqual(first_entry["quiz_id"], 1)
        self.assertEqual(first_entry["ques_id"], 1)
        self.assertEqual(first_entry["opts_id"], 1)
        self.assertEqual(first_entry["is_right"], 0)
        self.assertEqual(
            first_entry["qopt"],
            "Ensure that the workstation is switched On, Clean the nozzle and restart the machine",
        )
        chkques = self.client.get(f"/get_spec_quiz_ques/{1}/{1}")
        updated_question = chkques.json["data"]
        self.assertEqual(
            updated_question["question"],
            "How do I troubleshoot for Xerox Workstation properly?",
        )

    # def test_insert_options(self):
    #     aQuestion = Question(
    #         qid=1,
    #         ques_id=1,
    #         question="How is SPM IS212 doing today for YYC?",
    #         question_type="mcq",
    #     )

    #     db.session.add(aQuestion)
    #     db.session.commit()

    #     update_question_body = {
    #         "question": "How do I troubleshoot for Xerox Workstation properly?",
    #         "optionsList": [
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 1,
    #                 "is_right": False,
    #                 "qopt": "Ensure that the workstation is switched On, Clean the nozzle and restart the machine",
    #             },
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 2,
    #                 "is_right": False,
    #                 "qopt": "Ensure that the workstation is switched Off, Clean the nozzle and restart the machine",
    #             },
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 3,
    #                 "is_right": False,
    #                 "qopt": "Workstation must be in maintenance mode, Clean the nozzle and restart the machine",
    #             },
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 4,
    #                 "is_right": True,
    #                 "qopt": "Perform debug development mode, Access command line to clean the nozzle and restart the machine",
    #             },
    #         ],
    #     }
    #     response = self.client.post(
    #         f"/ques_opt_update/{1}/{1}",
    #         data=json.dumps(update_question_body),
    #         content_type="application/json",
    #     )
    #     self.assertEqual(response.json["data"]["status"], 200)
    #     chkdata = self.client.get(f"/ques_opt/{1}/{1}")
    #     all_entry = chkdata.json["data"]
    #     self.assertEqual(len(all_entry), 4)
    #     first_entry = all_entry[0]
    #     sec_entry = all_entry[1]
    #     third_entry = all_entry[2]
    #     fourth_entry = all_entry[3]
    #     self.assertEqual(first_entry["quiz_id"], 1)
    #     self.assertEqual(first_entry["ques_id"], 1)
    #     self.assertEqual(first_entry["opts_id"], 1)
    #     self.assertEqual(first_entry["is_right"], False)
    #     self.assertEqual(
    #         first_entry["qopt"],
    #         "Ensure that the workstation is switched On, Clean the nozzle and restart the machine",
    #     )

    #     self.assertEqual(sec_entry["quiz_id"], 1)
    #     self.assertEqual(sec_entry["ques_id"], 1)
    #     self.assertEqual(sec_entry["opts_id"], 2)
    #     self.assertEqual(sec_entry["is_right"], False)
    #     self.assertEqual(
    #         sec_entry["qopt"],
    #         "Ensure that the workstation is switched Off, Clean the nozzle and restart the machine",
    #     )

    #     self.assertEqual(third_entry["quiz_id"], 1)
    #     self.assertEqual(third_entry["ques_id"], 1)
    #     self.assertEqual(third_entry["opts_id"], 3)
    #     self.assertEqual(third_entry["is_right"], False)
    #     self.assertEqual(
    #         third_entry["qopt"],
    #         "Workstation must be in maintenance mode, Clean the nozzle and restart the machine",
    #     )

    #     self.assertEqual(fourth_entry["quiz_id"], 1)
    #     self.assertEqual(fourth_entry["ques_id"], 1)
    #     self.assertEqual(fourth_entry["opts_id"], 4)
    #     self.assertEqual(fourth_entry["is_right"], True)
    #     self.assertEqual(
    #         fourth_entry["qopt"],
    #         "Perform debug development mode, Access command line to clean the nozzle and restart the machine",
    #     )

    # def test_delete_options(self):
    #     aQuestion = Question(
    #         qid=1,
    #         ques_id=1,
    #         question="How is SPM IS212 doing today for YYC?",
    #         question_type="mcq",
    #     )

    #     db.session.add(aQuestion)
    #     db.session.commit()
    #     update_question_body = {
    #         "question": "How do I troubleshoot for Xerox Workstation properly?",
    #         "optionsList": [
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 1,
    #                 "is_right": False,
    #                 "qopt": "Ensure that the workstation is switched On, Clean the nozzle and restart the machine",
    #             },
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 2,
    #                 "is_right": False,
    #                 "qopt": "Ensure that the workstation is switched Off, Clean the nozzle and restart the machine",
    #             },
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 3,
    #                 "is_right": False,
    #                 "qopt": "Workstation must be in maintenance mode, Clean the nozzle and restart the machine",
    #             },
    #             {
    #                 "quiz_id": 1,
    #                 "ques_id": 1,
    #                 "opts_id": 4,
    #                 "is_right": True,
    #                 "qopt": "Perform debug development mode, Access command line to clean the nozzle and restart the machine",
    #             },
    #         ],
    #     }
    #     response = self.client.post(
    #         f"/ques_opt_update/{1}/{1}",
    #         data=json.dumps(update_question_body),
    #         content_type="application/json",
    #     )
    #     self.assertEqual(response.json["data"]["status"], 200)
    #     del4 = self.client.get(f"/ques_opt_delete/{1}/{1}/{4}")

    #     chkdata = self.client.get(f"/ques_opt/{1}/{1}")
    #     all_entry = chkdata.json["data"]
    #     self.assertEqual(len(all_entry), 3)
    #     del4 = self.client.get(f"/ques_opt_delete/{1}/{1}/{2}")
    #     chkdata = self.client.get(f"/ques_opt/{1}/{1}")
    #     all_entry = chkdata.json["data"]
    #     self.assertEqual(len(all_entry), 2)


if __name__ == "__main__":
    unittest.main()
