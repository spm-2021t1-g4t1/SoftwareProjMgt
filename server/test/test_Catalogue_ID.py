#Shun Hui
#shunhui.lee.2019
import unittest
import json
import flask_testing
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
            classEnrolmentQueue(staff_username = "jane", course_id = 1 , class_no = 1),
            classEnrolmentQueue(staff_username = "jane", course_id = 2 , class_no = 1),
            course(course_id = '1', course_name='Fundamentals of Xerox WorkCentre 784', description = 'This course is a basic introduction to the Fundamentals of Xerox WorkCentre printer course.'),
            course(course_id = '2', course_name='Programming for Xerox WorkCentre with CardAccess and Integration', description = 'This course will equip you with basic programming skills as well as software integration.'),
            learningObjective(course_id = '1', learning_objective= 'Create complete Angular applications'),
            learningObjective(course_id = '1', learning_objective= 'Fundamentals of working with Angular'),
            learningObjective(course_id = '2', learning_objective= 'Create complete Angular applications'),
            learningObjective(course_id = '2', learning_objective= 'Fundamentals of working with Angular')
        ]
        db.session.bulk_save_objects(Objects)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class testIntegrateCatalog(TestApp):
    def testCatalogPageResponse(self):
        response =self.client.get(f"/catalog/jane")
        self.assert200(response)
        
        Course1 = response.json['data'][0]
        Course2 = response.json['data'][1]
        
        self.assertEqual(Course1['course_id'],1)
        self.assertEqual(Course2['course_id'],2)
        self.assertEqual(Course1['course_name'], 'Fundamentals of Xerox WorkCentre 784')
        self.assertEqual(Course1['description'], 'This course is a basic introduction to the Fundamentals of Xerox WorkCentre printer course.')

        self.assertTrue(type(Course1['learning_objective']) == list)
        self.assertTrue(type(Course1['classes']) == list)

        
if __name__ == "__main__":
    unittest.main()
