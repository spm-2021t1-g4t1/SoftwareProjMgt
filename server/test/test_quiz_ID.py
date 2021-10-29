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


class TestQuiz(TestApp):
    def test_save_quizName(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        db.session.commit()
        data = self.client.get(f"/quiz")
        insertedQuiz = data.json["data"][0]
        self.assertEqual(insertedQuiz["uploader"], "James Smith")
        self.assertEqual(
            insertedQuiz["quiz_name"], "Fundamentals of Xerox WorkCentre 7845"
        )
        self.assertEqual(
            insertedQuiz["description"], "SECTION 1 of Xerox WorkCentre 7845"
        )
        self.assertEqual(insertedQuiz["duration"], "00:30:43")

        editQuiz = {
            "quiz_id": 1,
            "quiz_name": "Fundamentals for Xerox WorkCentre Part 1",
        }

        response = self.client.post(
            f"/quiz_update/{1}",
            data=json.dumps(editQuiz),
            content_type="application/json",
        )
        self.assertEqual(response.json["data"]["status"], 200)

        chk_updated_data = self.client.get("/quiz")

        chk_insertedQuiz = chk_updated_data.json["data"][0]
        #Changes
        self.assertEqual(
            chk_insertedQuiz["quiz_name"], "Fundamentals for Xerox WorkCentre Part 1"
        )
        self.assertEqual(
            chk_insertedQuiz["description"],
            "SECTION 1 of Xerox WorkCentre 7845",
        )
        #Changes
        self.assertEqual(chk_insertedQuiz["duration"], "00:30:43")

    def test_save_quiz_fail(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        db.session.commit()
        editQuiz = {
            "quiz_id": 1,
            "quiz_name": "Fundamentals for Xerox WorkCentre Part 1",
            "description": "SECTION 1 of Xerox WorkCentre 7845 -- Fundamentals",
            "duration": "00:25:57",
        }

        response = self.client.post(
            f"/quiz_update/{1}",
            data=json.dumps(editQuiz),
            content_type="application/json",
        )

        self.assertRaises(Exception)
        #Changes
        self.assertEqual(response.json["data"]["status"], 200)

    def test_get_all_quiz(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        db.session.commit()
        data = self.client.get(f"/quiz")
        insertedQuiz = data.json["data"][0]
        self.assertEqual(insertedQuiz["uploader"], "James Smith")
        self.assertEqual(
            insertedQuiz["quiz_name"], "Fundamentals of Xerox WorkCentre 7845"
        )
        self.assertEqual(
            insertedQuiz["description"], "SECTION 1 of Xerox WorkCentre 7845"
        )
        self.assertEqual(insertedQuiz["duration"], "00:30:43")
        self.assertEqual(insertedQuiz["quiz_id"], 1)
        self.assertEqual(len(data.json["data"]), 1)

    def test_spec_quiz(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        db.session.commit()
        data = self.client.get(f"/quiz/{1}")
        insertedQuiz = data.json["data"][0]
        self.assertEqual(insertedQuiz["uploader"], "James Smith")
        self.assertEqual(
            insertedQuiz["quiz_name"], "Fundamentals of Xerox WorkCentre 7845"
        )
        self.assertEqual(
            insertedQuiz["description"], "SECTION 1 of Xerox WorkCentre 7845"
        )
        self.assertEqual(insertedQuiz["duration"], "00:30:43")
        self.assertEqual(insertedQuiz["quiz_id"], 1)
        self.assertEqual(len(data.json["data"]), 1)

    def test_create_quiz(self):
        body = {
            "quiz_id": 1,
            "quiz_name": "Fundamentals of Xerox WorkCentre 7845",
            "description": "SECTION 1 of Xerox WorkCentre 7845",
            "uploader": "James Smith",
            "duration": "00:30:43",
        }
        response = self.client.post(
            f"/insert_quiz",
            data=json.dumps(body),
            content_type="application/json",
        )

        self.assertEqual(response.json["data"]["status"], 200)
        data = self.client.get(f"/quiz/{1}")
        insertedQuiz = data.json["data"][0]
        self.assertEqual(insertedQuiz["uploader"], "James Smith")
        self.assertEqual(
            insertedQuiz["quiz_name"], "Fundamentals of Xerox WorkCentre 7845"
        )
        self.assertEqual(
            insertedQuiz["description"], "SECTION 1 of Xerox WorkCentre 7845"
        )
        self.assertEqual(insertedQuiz["duration"], "00:30:43")
        self.assertEqual(insertedQuiz["quiz_id"], 1)
        self.assertEqual(len(data.json["data"]), 1)

    def test_delete_quiz(self):
        aQuiz = Quiz(
            quiz_id=1,
            quiz_name="Fundamentals of Xerox WorkCentre 7845",
            description="SECTION 1 of Xerox WorkCentre 7845",
            uploader="James Smith",
            duration="00:30:43",
        )
        db.session.add(aQuiz)
        db.session.commit()
        check_delete = self.client.get(f"/quiz_delete/{1}")
        self.assertEqual(check_delete.json["data"]["status"], 200)
        response = self.client.get("/quiz")
        self.assertEqual(len(response.json["data"]), 0)


if __name__ == "__main__":
    unittest.main()
