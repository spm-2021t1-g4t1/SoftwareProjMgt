from db import db

class staff(db.Model):
    __tablename__ = "staff"

    staff_username = db.Column(db.String(255), primary_key=True)
    staff_name = db.Column(db.String(255), primary_key=True)
    role = db.Column(db.Integer)
    department = db.Column(db.String(255))
    current_designation = db.Column(db.String(255))
    
    def viewjson(self):
        return {
            "staff_email": self.staff_username,
            "staff_name": self.staff_name,
            "role": self.role,
            "department": self.department,
            "current_designation": self.current_designation
        }

    @classmethod
    def get_staffList(cls):
        staffList = cls.query.all()
        return {'data': [staff.viewjson() for staff in staffList]}



class classEnrolment(db.Model):
    __tablename__ = 'class_enrolment'

    staff_username = db.Column(db.String(255), db.ForeignKey('staff.staff_username') , primary_key=True)
    course_id = db.Column(db.Integer , primary_key=True)
    class_no = db.Column(db.Integer ,primary_key=True)
    staff = db.relationship('staff', backref='staff', lazy = True)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['course_id', 'class_no'], ["lesson.course_id",'lesson.class_no']
        ),
    )

    def json(self):
        return {
            "staff_username": self.staff_username,
            "course_id": self.course_id,
            "class_no": self.class_no,
        }

    @classmethod
    def getClasslist(cls,course_id, class_no):
        ClassListDAO = cls.query.filter_by(course_id = course_id, class_no = class_no).all()
        classList = {'data':{}}
        for index, Student in enumerate(ClassListDAO):
            classList['data'][index] = Student.staff.viewjson()
        return classList


    @classmethod
    def getStaffEnrollment(cls, staff_username):
        ClassListDAO = cls.query.filter_by(staff_username = staff_username).all()
        classList = {'data':{}}
        for index, classes in enumerate(ClassListDAO):
            classList['data'][index] = classes.json()
        return classList

# class classAssignment(db.Model):
#     __tablename__ = 'class_assignment'

#     staff_email = db.Column(db.String(255), db.ForeignKey('staff.staff_email') ,primary_key=True)
#     course_id = db.Column(db.Integer , primary_key=True)
#     class_no = db.Column(db.Integer ,primary_key=True)

#     __table_args__ = (
#         db.ForeignKeyConstraint(
#             ['course_id', 'class_no'], ["lesson.course_id",'lesson.class_no']
#         ),
#     )

#     def json(self):
#         return {
#             "staff_email": self.staff_email,
#             "course_id": self.course_id,
#             "class_no": self.class_no,
#         }
