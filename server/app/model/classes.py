from db import db

#-----------------------------------------------------------------------------------------------------------------------#

class classes(db.Model):
    __tablename__ ="classes"
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    class_no = db.Column(db.Integer)
    start_date  = db.Column(db.DateTime)
    end_date  = db.Column(db.DateTime)
    start_time  = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    class_size   = db.Column(db.Integer)
    trainer_name  = db.Column(db.String(255), db.ForeignKey('staff.staff_username'), nullable=True)
    lesson = db.relationship('lesson', backref='classes', lazy = True)
    
    __table_args__ = (
    db.PrimaryKeyConstraint(
        course_id, class_no,
        ),
    )

    def json(self):
        return {
            "course_id": self.course_id,
            "class_no": self.class_no,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "class_size": self.class_size,
            "trainer_name": self.trainer_name,
        }

    def viewjson(self):
        lesson_obj = []
        for lesson in self.lesson:
            lesson_obj.append(lesson.json())
        
        return {
            "course_id": self.course_id,
            "class_no": self.class_no,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "class_size": self.class_size,
            "trainer_name": self.trainer_name,
            'lesson' : lesson_obj
        }


    @classmethod
    def get_specificClass(cls,course_id, class_no):
        classobj = cls.query.filter_by(course_id= course_id, class_no = class_no).first()
        return {'data': classobj.json()}

    @classmethod
    def get_specificClassDetail(cls,course_id, class_no):
        classobj = cls.query.filter_by(course_id= course_id, class_no = class_no).first()
        return {'data': classobj.viewjson()}