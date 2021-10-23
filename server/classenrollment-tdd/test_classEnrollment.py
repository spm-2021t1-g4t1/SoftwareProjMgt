# import unittest
# import flask_testing
# import json
# from helper import *
# from app import *
# from datetime import datetime
# # from app.model import staff
# # from app import app, db

# # staff.py
# # do for classenrollment too

# class TestApp(flask_testing.TestCase):
#     app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
#     app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
#     app.config['TESTING'] = True

#     def create_app(self):
#         db.init_app(app)
#         return app

#     def setUp(self):
#         db.create_all()
#         aStaff = staff(
#             staff_username = 'coreyroberts',
#             staff_name = 'Corey Roberts',
#             role = 'Learner',
#             department = 'Operation',
#             current_designation = 'Engineer'
#         )
#         db.session.add(aStaff)
#         db.session.commit()
#         aStaff2 = staff(
#             staff_username = 'hello',
#             staff_name = 'Corey Roberts',
#             role = 'Learner',
#             department = 'Operation',
#             current_designation = 'Engineer'
#         )
#         db.session.add(aStaff2)
#         db.session.commit()

#         # # Set up course objects
#         # course1 = course(
#         #     course_id = 1,
#         #     course_name = "Test Course 1",
#         #     description = "Test Description 1"
#         # )
#         # course2 = course(
#         #     course_id = 2,
#         #     course_name = "Test Course 2",
#         #     description = "Test Description 2"
#         # )
#         # db.session.add(course1)
#         # db.session.add(course2)

#         # # class
#         # classes1 = classes(
#         #     course_id = 1,
#         #     class_no = 1,
#         #     start_date = datetime(2021,9,1),
#         #     end_date = datetime(2021,9,2),
#         #     # start_time = '08:00:00',
#         #     # end_time = '11:00:00',
#         #     class_size = 40,
#         #     trainer_name = 'stevejobs'
#         # )
#         # classes2 = classes(
#         #     course_id = 2,
#         #     class_no = 1,
#         #     start_date = datetime(2021,9,1),
#         #     end_date = datetime(2021,9,2),
#         #     # start_time = '08:00:00',
#         #     # end_time = '11:00:00',
#         #     class_size = 40,
#         #     trainer_name = 'stevejobs'
#         # )
#         # db.session.add(classes1)
#         # db.session.add(classes2)
#         # db.session.commit()

#         # # lessons
#         # lesson1 = lesson(
#         #     course_id = 1,
#         #     class_no = 1,
#         #     lesson_no = 1,
#         #     lesson_name = 'name',
#         #     lesson_description = 'desc'
#         # )
#         # lesson2 = lesson(
#         #     course_id = 2,
#         #     class_no = 1,
#         #     lesson_no = 1,
#         #     lesson_name = 'name',
#         #     lesson_description = 'desc'
#         # )
#         # db.session.add(lesson1)
#         # db.session.add(lesson2)
#         # db.session.commit()

#         # # lesson materials
#         # lm1 = lesson_materials(
#         #     course_id = 1,
#         #     class_no = 1,
#         #     lesson_no = 1,
#         #     course_material_title = 'title',
#         #     link = 'link'
#         # )
#         # lm2 = lesson_materials(
#         #     course_id = 1,
#         #     class_no = 1,
#         #     lesson_no = 1,
#         #     course_material_title = 'title',
#         #     link = 'link'
#         # )
#         # db.session.add(lm1)
#         # db.session.add(lm2)
#         # db.session.commit()

        

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

# class testClassEnrollment(TestApp):
#     def testGetClassList(self):
#         aStudent1 = classEnrolment(
#             staff_username = 'coreyroberts',
#             course_id = 1,
#             class_no = 1
#         )
#         aStudent2 = classEnrolment(
#             staff_username = 'hello',
#             course_id = 1,
#             class_no = 1
#         )

#         db.session.add(aStudent1)
#         db.session.add(aStudent2)
#         db.session.commit()

#         data = self.client.get(f"/enrolment/{1}/{1}")
#         insertedStudents = data.json["data"]

#         # print(insertedStudents)
#         # print(insertedStudents['0'])

#         self.assertEqual(insertedStudents['0']['staff_username'], 'coreyroberts')
#         self.assertEqual(insertedStudents['1']['staff_username'], 'hello')
    
    
#     # def testGetStaffEnrollment(self):
#     #     aStudent1 = classEnrolment(
#     #         staff_username = 'coreyroberts',
#     #         course_id = 1,
#     #         class_no = 1
#     #     )
#     #     aStudent2 = classEnrolment(
#     #         staff_username = 'coreyroberts',
#     #         course_id = 2,
#     #         class_no = 2
#     #     )
#     #     db.session.add(aStudent1)
#     #     db.session.add(aStudent2)
#     #     db.session.commit()

        

        


#         # data = self.client.get(f"/enrolment/coreyroberts")
#         # # insertedStaff = data.json['data']
#         # print('hi')
#         # print(data)



# if __name__ == "__main__":
#     unittest.main()

print('hi')
