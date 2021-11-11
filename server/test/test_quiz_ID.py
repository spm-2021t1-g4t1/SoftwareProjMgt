# Done by Yeo Yao Cong
# Email: ycyeo.2019
import unittest
import flask_testing
from datetime import datetime, timedelta, date, time
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
            duration="00:00:00",
        )
        Objects = [
            course(
                course_id=1,
                course_name="Test Course 1",
                description="Test Description 1",
            ),
            course(
                course_id=2,
                course_name="Test Course 2",
                description="Test Description 2",
            ),
            classes(
                course_id=1,
                class_no=1,
                start_date=datetime.today().date() + timedelta(days=-2),
                end_date=datetime.today().date() + timedelta(days=-1),
                start_time=None,
                end_time=None,
                class_size=40,
                trainer_name="stevejobs",
                selfenrol_start=None,
                selfenrol_end=None,
                finalquiz_id=1,
                lesson=[],
            ),
            classes(
                course_id=2,
                class_no=1,
                start_date=datetime.today().date() + timedelta(days=1),
                end_date=datetime.today().date() + timedelta(days=2),
                start_time=None,
                end_time=None,
                class_size=40,
                trainer_name=None,
                selfenrol_start=None,
                selfenrol_end=None,
                finalquiz_id=1,
                lesson=[],
            ),
        ]

        db.session.bulk_save_objects(Objects)
        db.session.add(q1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestQuiz(TestApp):
    # saves both duration and name
    def test_save_quizDetails(self):
        editQuiz = {
            "quiz_id": 1,
            "quiz_name": "Fundamentals for Xerox WorkCentre Part 1",
            "duration": "0:30:43",
        }
        response = self.client.post(
            f"/quiz_update/{1}",
            data=json.dumps(editQuiz),
            content_type="application/json",
        )
        self.assertEqual(response.json["data"]["status"], 200)

        chk_updated_data = self.client.get("/quiz")
        chk_insertedQuiz = chk_updated_data.json["data"][0]

        self.assertEqual(
            chk_insertedQuiz["quiz_name"], "Fundamentals for Xerox WorkCentre Part 1"
        )
        self.assertEqual(chk_insertedQuiz["duration"], "0:30:43")

    def test_get_all_quiz(self):
        data = self.client.get(f"/quiz")
        get_all_quiz = data.json["data"]
        self.assertEqual(len(get_all_quiz), 1)
        self.assertEqual(get_all_quiz[0]["uploader"], "james_smith")
        self.assertEqual(
            get_all_quiz[0]["quiz_name"], "Fundamentals of Xerox WorkCentre 7845"
        )
        self.assertEqual(get_all_quiz[0]["duration"], "00:00:00")
        self.assertEqual(get_all_quiz[0]["quiz_id"], 1)

    def test_spec_quiz(self):
        data = self.client.get(f"/quiz/{1}")
        insertedQuiz = data.json["data"][0]
        self.assertEqual(insertedQuiz["uploader"], "james_smith")
        self.assertEqual(
            insertedQuiz["quiz_name"], "Fundamentals of Xerox WorkCentre 7845"
        )
        self.assertEqual(
            insertedQuiz["description"], "SECTION 1 of Xerox WorkCentre 7845"
        )
        self.assertEqual(insertedQuiz["duration"], "00:00:00")
        self.assertEqual(insertedQuiz["quiz_id"], 1)

    def test_create_quiz(self):
        response = self.client.get(f"/insert_quiz/2/james_smith")
        self.assertEqual(response.json["data"]["status"], 200)
        data = self.client.get(f"/quiz/{2}")
        insertedQuiz = data.json["data"][0]
        self.assertEqual(insertedQuiz["uploader"], "james_smith")
        self.assertEqual(insertedQuiz["quiz_name"], "Untitled")
        self.assertEqual(insertedQuiz["description"], "")
        self.assertEqual(insertedQuiz["duration"], "00:00:00")
        self.assertEqual(insertedQuiz["quiz_id"], 2)

    def test_delete_quiz(self):
        check_delete = self.client.get(f"/quiz_delete/{1}")
        self.assertEqual(check_delete.json["data"]["status"], 200)
        response = self.client.get("/quiz")
        self.assertEqual(len(response.json["data"]), 0)

    def test_update_assign_finalquiz(self):
        editfinalQuiz = {"course_id": 1, "class_no": 1, "qid": 1}
        response = self.client.post(
            f"/update_assign_finalquiz",
            data=json.dumps(editfinalQuiz),
            content_type="application/json",
        )
        self.assertEqual(response.json["code"], 200)
        self.assertEqual(
            response.json["data"],
            {
                "class_no": 1,
                "course_id": 1,
                "message": "Quiz assigned successfully.",
                "qid": 1,
            },
        )

    def test_final_quiz(self):
        response = self.client.get(f"/final_quiz/{1}/{1}")
        self.assertEqual(response.json["code"], 200)
        self.assertEqual(
            response.json["data"],
            {
                "description": "SECTION 1 of Xerox WorkCentre 7845",
                "duration": "00:00:00",
                "question": [],
                "quiz_id": 1,
                "quiz_name": "Fundamentals of Xerox WorkCentre 7845",
                "uploader": "james_smith",
            },
        )

if __name__ == "__main__":
    unittest.main()
