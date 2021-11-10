import unittest
import json
import flask_testing
from datetime import datetime, timedelta
from helper import *

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()
        Objects = [
            staff(staff_username = 'coreyroberts', staff_name = 'Corey Roberts', role = 'Learner', department = 'Operation', current_designation = 'Engineer'),
            staff(staff_username = 'hello', staff_name = 'hello', role = 'Learner', department = 'Operation', current_designation = 'Engineer'),
            course(course_id = 1, course_name = "Test Course 1", description = "Test Description 1" ),
            course(course_id = 2, course_name = "Test Course 2", description = "Test Description 2"),
            
            classes(course_id = 1, 
                    class_no = 1, 
                    start_date = datetime.today().date() + timedelta(days=-2), 
                    end_date = datetime.today().date() +  timedelta(days=-1), 
                    start_time = None,
                    end_time = None,
                    class_size = 40, 
                    trainer_name = 'stevejobs',
                    selfenrol_start = None,
                    selfenrol_end = None,
                    finalquiz_id = 1, 
                    lesson = []
            ),

            classes(course_id = 2, 
                    class_no = 1, 
                    start_date = datetime.today().date() + timedelta(days=1), 
                    end_date = datetime.today().date() +  timedelta(days=2), 
                    start_time = None,
                    end_time = None,
                    class_size = 40, 
                    trainer_name = None,
                    selfenrol_start = None,
                    selfenrol_end = None,
                    finalquiz_id = 1, 
                    lesson = [])

        ]

        db.session.bulk_save_objects(Objects)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testClasssesObj(TestApp):
    def testGetAllClasses(self):
        res = classes.getAllClasses()
        expected = [
            {'course_name': 'Test Course 1', 
            'course_id': 1, 
            'class_no': 1, 
            'start_date': (datetime.today() + timedelta(days=-2)).replace(hour=0, minute=0, second=0, microsecond=0), 
            'end_date': (datetime.today() +  timedelta(days=-1)).replace(hour=0, minute=0, second=0, microsecond=0), 
            'start_time': 'None',
            'end_time':'None', 
            'class_size': 40, 
            'trainer_name': 'stevejobs', 
            'selfenrol_start': None, 
            'selfenrol_end': None}, 

            {'course_name': 'Test Course 2', 
            'course_id': 2, 
            'class_no': 1, 
            'start_date': (datetime.today() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0), 
            'end_date': (datetime.today() +  timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0), 
            'start_time': 'None', 
            'end_time': 'None', 
            'class_size': 40, 
            'trainer_name': None, 
            'selfenrol_start': None, 
            'selfenrol_end': None}
            ]
        self.assertEqual(expected, res)

    def testSetSelfEnrolDates(self):
        classes.setSelfEnrolDates({
            "course_id": 1, 
            "class_no": 1,
            "selfenrol_start": datetime.strptime("2021-12-01", "%Y-%m-%d").date(),
            "selfenrol_end": datetime.strptime("2021-12-30", "%Y-%m-%d").date()
            })
        
        expected = {
            "start": "2021-12-01", 
            "end": "2021-12-30"
        }

        updated = classes.query.filter_by(course_id=1, class_no=1).first()
        self.assertEqual(updated.getSelfEnrolDates(), expected)

    def testGet_specificClass(self):
        expected = {
            "data": {
                'course_id': 2, 
                'class_no': 1, 
                'start_date': '2021-11-10 00:00:00', 
                'end_date': '2021-11-11 00:00:00', 
                'start_time': 'None', 
                'end_time': 'None', 
                'class_size': 40, 
                'trainer_name': None
            }
        }

        self.assertEqual(classes.get_specificClass(2,1), expected)

    def testGet_specificClassDetail(self):
        expected = {
            'data': 
                {
                    'course_id': 2, 
                    'class_no': 1, 
                    'start_date': '2021-11-10 00:00:00', 
                    'end_date': '2021-11-11 00:00:00', 
                    'start_time': 'None', 
                    'end_time': 'None', 
                    'class_size': 40, 
                    'trainer_name': None, 
                    'lesson': []
                }
        }
        self.assertEqual(classes.get_specificClassDetail(2, 1), expected)

    def testget_unassignedClass(self):
        expected = {
            'data': [
                {   
                    'course_name': 'Test Course 2', 
                    'course_id': 2, 
                    'class_no': 1, 
                    'start_date': datetime(2021, 11, 10, 0, 0), 
                    'end_date': datetime(2021, 11, 11, 0, 0), 
                    'start_time': 'None', 
                    'end_time': 'None', 
                    'class_size': 40, 
                    'trainer_name': None, 
                    'selfenrol_start': None, 
                    'selfenrol_end': None
                }
            ]
        }
        self.assertEqual(classes.get_unassignedClass(), expected)

    def testGetFutureClasses(self):
        res = classes.get_futureClass()
        expected = {
            'data': [
                {'course_name': 'Test Course 2', 
                'course_id': 2, 
                'class_no': 1, 
                'start_date': (datetime.today() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0), 
                'end_date': (datetime.today() +  timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0), 
                'start_time': 'None', 
                'end_time': 'None', 
                'class_size': 40, 
                'trainer_name': None, 
                'selfenrol_start': None, 
                'selfenrol_end': None}
            ]
        }
        self.assertEqual(res, expected)

    def testModifyTrainer(self):
        res = classes.modifyTrainer(2,1,'jackma')
        self.assertEqual(res, {'data': 'Updated'})

        res1 = classes.get_specificClass(2,1)
        expected1 = {
            'data': {
                'course_id': 2, 
                'class_no': 1, 
                'start_date': '2021-11-10 00:00:00', 
                'end_date': '2021-11-11 00:00:00', 
                'start_time': 'None', 
                'end_time': 'None', 
                'class_size': 40, 
                'trainer_name': 'jackma'
            }
        }
        self.assertEqual(res1, expected1)

    def testGet_get_trainerAssignedClass(self):
        res = classes.get_trainerAssignedClass("stevejobs")
        expected = [{
                'Test Course 1': 
                    [{'course_name': 'Test Course 1', 
                    'course_id': 1, 
                    'class_no': 1, 
                    'start_date': datetime(2021, 11, 7, 0, 0), 
                    'end_date': datetime(2021, 11, 8, 0, 0), 
                    'start_time': 'None', 
                    'end_time': 'None', 
                    'class_size': 40,
                    'trainer_name': 'stevejobs', 
                    'selfenrol_start': None, 
                    'selfenrol_end': None}]
            }]
        self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
