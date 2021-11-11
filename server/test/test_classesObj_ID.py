# Done by Yeo Yao Cong
# Email: ycyeo.2019
import unittest
import json
import flask_testing
from datetime import datetime, timedelta
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
        Objects = [
            staff(
                staff_username="coreyroberts",
                staff_name="Corey Roberts",
                role="Learner",
                department="Operation",
                current_designation="Engineer",
            ),
            staff(
                staff_username="hello",
                staff_name="hello",
                role="Learner",
                department="Operation",
                current_designation="Engineer",
            ),
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
            lesson(
                course_id=1,
                class_no=1,
                lesson_no=1,
                lesson_name="Test Lesson Name",
                lesson_description="Test Description",
                quiz_assigned_id=1,
            ),
            lesson(
                course_id=1,
                class_no=1,
                lesson_no=2,
                lesson_name="Test Lesson Name 2",
                lesson_description="Test Description 2",
                quiz_assigned_id=1,
            ),
            lesson_quiz_attempts(
                course_id=1,
                class_no=1,
                lesson_no=1,
                staff_username="darrelwilde",
                quiz_score=60,
            ),
            lesson_quiz_attempts(
                course_id=1,
                class_no=1,
                lesson_no=2,
                staff_username="darrelwilde",
                quiz_score=80,
            ),
            classEnrolment(staff_username="coreyroberts", course_id=1, class_no=1),
            classEnrolment(staff_username="hello", course_id=1, class_no=1),
            classEnrolment(staff_username="coreyroberts", course_id=2, class_no=1),
        ]
        db.session.bulk_save_objects(Objects)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class testGet_specificClass(TestApp):
    def testGet_specificClass(self):
        expected = {
            "data": {
                "course_id": 2,
                "class_no": 1,
                "start_date": str(
                    (datetime.today() + timedelta(days=1)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    )
                ),
                "end_date": str(
                    (datetime.today() + timedelta(days=2)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    )
                ),
                "start_time": "None",
                "end_time": "None",
                "class_size": 40,
                "trainer_name": None,
            }
        }

        self.assertEqual(classes.get_specificClass(2, 1), expected)

    def testGet_specificClassDetail(self):
        expected = {
            "data": {
                "course_id": 2,
                "class_no": 1,
                "start_date": str(
                    (datetime.today() + timedelta(days=1)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    )
                ),
                "end_date": str(
                    (datetime.today() + timedelta(days=2)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    )
                ),
                "start_time": "None",
                "end_time": "None",
                "class_size": 40,
                "trainer_name": None,
                "lesson": [],
            }
        }
        self.assertEqual(classes.get_specificClassDetail(2, 1), expected)


class testGetAllClasses(TestApp):
    def testMethods(self):
        res = classes.getAllClasses()
        expected = [
            {
                "course_name": "Test Course 1",
                "course_id": 1,
                "class_no": 1,
                "start_date": (datetime.today() + timedelta(days=-2)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                ),
                "end_date": (datetime.today() + timedelta(days=-1)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                ),
                "start_time": "None",
                "end_time": "None",
                "class_size": 40,
                "trainer_name": "stevejobs",
                "selfenrol_start": None,
                "selfenrol_end": None,
            },
            {
                "course_name": "Test Course 2",
                "course_id": 2,
                "class_no": 1,
                "start_date": (datetime.today() + timedelta(days=1)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                ),
                "end_date": (datetime.today() + timedelta(days=2)).replace(
                    hour=0, minute=0, second=0, microsecond=0
                ),
                "start_time": "None",
                "end_time": "None",
                "class_size": 40,
                "trainer_name": None,
                "selfenrol_start": None,
                "selfenrol_end": None,
            },
        ]
        self.assertEqual(expected, res)

    def getRoute(self):
        data = self.client.get(f"/class")
        self.assert200(data)


class testSetSelfEnrolDates(TestApp):
    def testMethods(self):
        classes.setSelfEnrolDates(
            {
                "course_id": 1,
                "class_no": 1,
                "selfenrol_start": datetime.strptime("2021-12-01", "%Y-%m-%d").date(),
                "selfenrol_end": datetime.strptime("2021-12-30", "%Y-%m-%d").date(),
            }
        )

        expected = {"start": "2021-12-01", "end": "2021-12-30"}

        updated = classes.query.filter_by(course_id=1, class_no=1).first()
        self.assertEqual(updated.getSelfEnrolDates(), expected)


class testGet_unassignedClass(TestApp):
    def testMethods(self):
        expected = {
            "data": [
                {
                    "course_name": "Test Course 2",
                    "course_id": 2,
                    "class_no": 1,
                    "start_date": (datetime.today() + timedelta(days=1)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    ),
                    "end_date": (datetime.today() + timedelta(days=2)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    ),
                    "start_time": "None",
                    "end_time": "None",
                    "class_size": 40,
                    "trainer_name": None,
                    "selfenrol_start": None,
                    "selfenrol_end": None,
                }
            ]
        }
        self.assertEqual(classes.get_unassignedClass(), expected)

    def testGetRoute(self):
        data = self.client.get(f"/class/get_unassignedClass")
        self.assert200(data)


class testGetFutureClasses(TestApp):
    def testMethods(self):
        res = classes.get_futureClass()
        expected = {
            "data": [
                {
                    "course_name": "Test Course 2",
                    "course_id": 2,
                    "class_no": 1,
                    "start_date": (datetime.today() + timedelta(days=1)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    ),
                    "end_date": (datetime.today() + timedelta(days=2)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    ),
                    "start_time": "None",
                    "end_time": "None",
                    "class_size": 40,
                    "trainer_name": None,
                    "selfenrol_start": None,
                    "selfenrol_end": None,
                }
            ]
        }
        self.assertEqual(res, expected)

    def testGetRoute(self):
        data = self.client.get(f"/class/get_futureClass")
        self.assert200(data)


class testModifyTrainer(TestApp):
    def testMethods(self):
        res = classes.modifyTrainer(2, 1, "jackma")
        self.assertEqual(res, {"data": "Updated"})

        res1 = classes.get_specificClass(2, 1)
        expected1 = {
            "data": {
                "course_id": 2,
                "class_no": 1,
                "start_date": str(
                    (datetime.today() + timedelta(days=1)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    )
                ),
                "end_date": str(
                    (datetime.today() + timedelta(days=2)).replace(
                        hour=0, minute=0, second=0, microsecond=0
                    )
                ),
                "start_time": "None",
                "end_time": "None",
                "class_size": 40,
                "trainer_name": "jackma",
            }
        }
        self.assertEqual(res1, expected1)

    def testPostRoute(self):
        body = {"class_no": 1, "course_id": 2, "staff_username": "jackma"}
        response = self.client.post(
            f"/class/trainer/modify",
            data=json.dumps(body, default=str),
            content_type="application/json",
        )
        self.assert200(response)


class testGet_trainerAssignedClass(TestApp):
    def testGet_trainerAssignedClass(self):
        res = classes.get_trainerAssignedClass("stevejobs")
        expected = [
            {
                "Test Course 1": [
                    {
                        "course_name": "Test Course 1",
                        "course_id": 1,
                        "class_no": 1,
                        "start_date": (datetime.today() + timedelta(days=-2)).replace(
                            hour=0, minute=0, second=0, microsecond=0
                        ),
                        "end_date": (datetime.today() + timedelta(days=-1)).replace(
                            hour=0, minute=0, second=0, microsecond=0
                        ),
                        "start_time": "None",
                        "end_time": "None",
                        "class_size": 40,
                        "trainer_name": "stevejobs",
                        "selfenrol_start": None,
                        "selfenrol_end": None,
                    }
                ]
            }
        ]
        self.assertEqual(res, expected)

    def testGetRoute(self):
        data = self.client.get(f"/class/stevejobs/get_assignedClass")
        self.assert200(data)

    def test_class_result(self):
        res = self.client.get(f"/class_result/1/1")
        self.assertEqual(len(res.json["data"]), 2)

    def test_assign_finalquiz_to_course(self):
        data = {"course_id": 1, "class_no": 1, "qid": 1}
        response = self.client.post(
            f"/update_assign_finalquiz",
            data=json.dumps(data, default=str),
            content_type="application/json",
        )
        print(response.json)
        self.assertEqual(
            response.json["data"],
            {
                "class_no": 1,
                "course_id": 1,
                "message": "Quiz assigned successfully.",
                "qid": 1,
            },
        )
        self.assertEqual(response.json["code"], 200)

    def test_selfEnrolDates(self):
        data = {
            "course_id": 1,
            "class_no": 1,
            "start_date": datetime.today().date() + timedelta(days=-2),
            "end_date": datetime.today().date() + timedelta(days=-1),
            "start_time": None,
            "end_time": None,
            "class_size": 40,
            "trainer_name": "stevejobs",
            "selfenrol_start": None,
            "selfenrol_end": None,
            "finalquiz_id": 1,
            "lesson": [],
        }
        response = self.client.post(
            f"/class/setSelfEnrolDates",
            data=json.dumps(data, default=str),
            content_type="application/json",
        )
        self.assertEqual(response.json["updated"], True)


if __name__ == "__main__":
    unittest.main()
