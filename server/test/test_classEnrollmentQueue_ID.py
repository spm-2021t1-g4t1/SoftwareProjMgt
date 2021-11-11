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
        object = [
            classEnrolmentQueue(staff_username = "coreyroberts", course_id = 1 , class_no = 1),
            staff(staff_username = 'coreyroberts', staff_name = 'Corey Roberts', role = 'Learner', department = 'Operation', current_designation = 'Engineer'),
            course(course_id = 1,course_name = "Test Course 1",description = "Test Description 1")
        ]
        db.session.bulk_save_objects(object)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class testIntegrateCEQ(TestApp):
    def testQuery(self):
        response = classEnrolmentQueue.getStaffQueue('coreyroberts',1)
        self.assertEqual(response,{'inQueue': True})

        reponseFailed = classEnrolmentQueue.getStaffQueue('john',1)
        self.assertEqual(reponseFailed,{'inQueue': False})

    def testGetRoute(self):
        data =self.client.get(f"/queue/coreyroberts/{1}")
        self.assert200(data)

    def testPostRoute(self):
        CEQ_body = {"class_no": 1}
        response = self.client.post(
            f"/queue/coreyroberts/{2}",
            data=json.dumps(CEQ_body),
            content_type="application/json",
        )
        self.assert200(response)
        self.assertEqual(response.json,{'code': 200, 'message': 'Enrollment succeed'})
        
        responseFailed = self.client.post(
            f"/queue/coreyroberts/{1}",
            data=json.dumps(CEQ_body),
            content_type="application/json",
        )
        self.assert400(responseFailed)

    

    # @classmethod
    # def getStaffRequest(cls,classobj):
    #     SRobj = {'data': []}
    #     StaffRequests = cls.query.filter(tuple_(cls.course_id, cls.class_no).in_(classobj))
    #     for SR in StaffRequests:
    #         SRobj['data'].append(SR.approvejson())
    #     return SRobj

    # @classmethod
    # def removeQueue(cls, staff_username, course_id ):
    #     StaffQueue = cls.query.filter_by(staff_username = staff_username, course_id = course_id).first()
    #     print(StaffQueue)
    #     db.session.delete(StaffQueue)
    #     db.session.commit()
    #     return {"data": "Removed"}

        
if __name__ == "__main__":
    unittest.main()
