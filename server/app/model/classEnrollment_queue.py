from db import db

class classEnrolmentQueue(db.Model):
    __tablename__ = 'classenrollment_queue'

    staff_username = db.Column(db.String(255), db.ForeignKey('staff.staff_username') , primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    class_no = db.Column(db.Integer ,primary_key=True)
    course = db.relationship('course', backref='classenrollment_queue', lazy = True)
    staff = db.relationship('staff', backref='classenrollment_queue', lazy = True)
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

    def approvejson(self):
        return {
            'course_id': self.course_id,
            'class_no': self.class_no,
            'course_name': self.course.course_name,
            'staff_name': self.staff.staff_name,
            'staff_username': self.staff.staff_username
        }

    @classmethod
    def getStaffQueue(cls, staff_username, course_id):
        StaffQueue = cls.query.filter_by(staff_username = staff_username, course_id = course_id).first()
        if StaffQueue == None:
            data = {'inQueue': False}
        else:
            data = {'inQueue': True}

        return data

    @classmethod
    def getStaffRequest(cls):
        SRobj = {'data': []}
        StaffRequests = cls.query.all()
        for SR in StaffRequests:
            SRobj['data'].append(SR.approvejson())
        return SRobj

    @classmethod
    def removeQueue(cls, staff_username, course_id ):
        StaffQueue = cls.query.filter_by(staff_username = staff_username, course_id = course_id).first()
        print(StaffQueue)
        db.session.delete(StaffQueue)
        db.session.commit()
        return {"data": "Removed"}
