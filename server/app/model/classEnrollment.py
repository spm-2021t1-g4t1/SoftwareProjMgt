from db import db

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

    @classmethod
    def enrollToClass(cls, staff_username, course_id, class_no):
        print('enrol')
        enrollObj = classEnrolment( staff_username = staff_username, class_no = class_no, course_id = course_id)
        db.session.add(enrollObj)
        db.session.commit()
        return {"data": "Added"}