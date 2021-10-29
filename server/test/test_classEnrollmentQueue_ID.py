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
        self.CEQ1 = classEnrolmentQueue(staff_username = "jane", course_id = 1 , class_no = 1)
        db.session.add(self.CEQ1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class testIntegrateCEQ(TestApp):
    def testQuery(self):
        response = self.CEQ1.getStaffQueue('jane',1)
        self.assertEqual(response,{'inQueue': True})

        reponseFailed = self.CEQ1.getStaffQueue('john',1)
        self.assertEqual(reponseFailed,{'inQueue': False})

    def testGetRoute(self):
        data =self.client.get(f"/queue/jane/{1}")
        self.assert200(data)
        
        # data = self.client.get(f"/queue/john/1")
        # self.assert200(data)

    def testPostRoute(self):
        CEQ_body = {"class_no": 1}
        response = self.client.post(
            f"/queue/jane/{2}",
            data=json.dumps(CEQ_body),
            content_type="application/json",
        )
        self.assert200(response)
        self.assertEqual(response.json,{'code': 200, 'message': 'Enrollment succeed'})
        
        # print(self.client.get(f"/queue/jane/{3}").json)
        
        
        responseFailed = self.client.post(
            f"/queue/jane/{1}",
            data=json.dumps(CEQ_body),
            content_type="application/json",
        )
        self.assert400(responseFailed)

        
        
if __name__ == "__main__":
    unittest.main()
