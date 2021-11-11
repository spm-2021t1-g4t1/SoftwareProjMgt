# Done by Yeo Yao Cong
# Email: ycyeo.2019
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


class TestQuizOptions(TestApp):
    def test_get_the_options(self):
        response1 = self.client.get(f"/ques_opt/{1}/{1}")
        data1 = response1.json["data"]
        response2 = self.client.get(f"/ques_opt/{1}/{2}")
        data2 = response2.json["data"]
        self.assertEqual(len(data1), 4)
        self.assertEqual(len(data2), 2)

    def test_update_options(self):
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
        chkdata = self.client.get(f"/ques_opt/{1}/{1}")
        self.assertEqual(
            chkdata.json["data"][0]["qopt"],
            "Ensure that the workstation is switched On, Clean the nozzle and restart the machine",
        )

    def test_insert_options(self):
        update_question_body = {
            "question": "Changing Question",
            "optionsList": [
                {
                    "quiz_id": 1,
                    "ques_id": 1,
                    "opts_id": 5,
                    "is_right": 0,
                    "qopt": "Boop",
                }
            ],
        }
        response = self.client.post(
            f"/ques_opt_update/{1}/{1}",
            data=json.dumps(update_question_body),
            content_type="application/json",
        )
        data = response.json
        self.assertEqual(data["data"]["status"], 200)
        chkdata = self.client.get(f"/ques_opt/{1}/{1}")
        chk = chkdata.json
        self.assertEqual(len(chk["data"]), 5)

    def test_many_insert_options(self):
        update_question_body = {
            "question": "How do I troubleshoot for Xerox Workstation properly?",
            "optionsList": [
                {
                    "quiz_id": 1,
                    "ques_id": 1,
                    "opts_id": 1,
                    "is_right": False,
                    "qopt": "Beep1 he nozzle and restart the machine",
                },
                {
                    "quiz_id": 1,
                    "ques_id": 1,
                    "opts_id": 2,
                    "is_right": False,
                    "qopt": "Test2, Clean the nozzle and restart the machine",
                },
                {
                    "quiz_id": 1,
                    "ques_id": 1,
                    "opts_id": 3,
                    "is_right": True,
                    "qopt": "Test3, Clean the nozzle and restart the machine",
                },
                {
                    "quiz_id": 1,
                    "ques_id": 1,
                    "opts_id": 4,
                    "is_right": False,
                    "qopt": "Perform debug development mode, Access command line to clean the nozzle and restart the machine",
                },
            ],
        }
        response = self.client.post(
            f"/ques_opt_update/{1}/{1}",
            data=json.dumps(update_question_body),
            content_type="application/json",
        )
        self.assertEqual(response.json["data"]["status"], 200)

        chkdata = self.client.get(f"/ques_opt/{1}/{1}")
        all_entry = chkdata.json["data"]
        self.assertEqual(len(all_entry), 4)
        first_entry = all_entry[0]
        sec_entry = all_entry[1]
        third_entry = all_entry[2]
        fourth_entry = all_entry[3]
        self.assertEqual(first_entry["qid"], 1)
        self.assertEqual(first_entry["ques_id"], 1)
        self.assertEqual(first_entry["opts_id"], 1)
        self.assertEqual(first_entry["is_right"], False)
        self.assertEqual(
            first_entry["qopt"],
            "Beep1 he nozzle and restart the machine",
        )

        self.assertEqual(sec_entry["qid"], 1)
        self.assertEqual(sec_entry["ques_id"], 1)
        self.assertEqual(sec_entry["opts_id"], 2)
        self.assertEqual(sec_entry["is_right"], False)
        self.assertEqual(
            sec_entry["qopt"],
            "Test2, Clean the nozzle and restart the machine",
        )

        self.assertEqual(third_entry["qid"], 1)
        self.assertEqual(third_entry["ques_id"], 1)
        self.assertEqual(third_entry["opts_id"], 3)
        self.assertEqual(third_entry["is_right"], True)
        self.assertEqual(
            third_entry["qopt"],
            "Test3, Clean the nozzle and restart the machine",
        )

        self.assertEqual(fourth_entry["qid"], 1)
        self.assertEqual(fourth_entry["ques_id"], 1)
        self.assertEqual(fourth_entry["opts_id"], 4)
        self.assertEqual(fourth_entry["is_right"], False)
        self.assertEqual(
            fourth_entry["qopt"],
            "Perform debug development mode, Access command line to clean the nozzle and restart the machine",
        )

    def test_delete_options(self):
        del4 = self.client.get(f"/ques_opt_delete/{1}/{1}/{4}")
        self.assertEqual(del4.json["data"]["status"], 200)
        chkdata = self.client.get(f"/ques_opt/{1}/{1}")
        all_entry = chkdata.json["data"]
        self.assertEqual(len(all_entry), 3)
        del4 = self.client.get(f"/ques_opt_delete/{1}/{1}/{2}")
        chkdata = self.client.get(f"/ques_opt/{1}/{1}")
        all_entry = chkdata.json["data"]
        self.assertEqual(len(all_entry), 2)


if __name__ == "__main__":
    unittest.main()
