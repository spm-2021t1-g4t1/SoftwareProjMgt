from datetime import date, datetime
import collections
from db import db

from itertools import groupby
from operator import itemgetter

#-----------------------------------------------------------------------------------------------------------------------#

class classes(db.Model):
    __tablename__ ="classes"
    courses = db.relationship("course", lazy=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    class_no = db.Column(db.Integer)
    start_date  = db.Column(db.DateTime)
    end_date  = db.Column(db.DateTime)
    start_time  = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    class_size   = db.Column(db.Integer)
    trainer_name  = db.Column(db.String(255), db.ForeignKey('staff.staff_username'), nullable=True)
    selfenrol_start = db.Column(db.DateTime)
    selfenrol_end = db.Column(db.DateTime)
    finalquiz_id  = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'))
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
    
    def coursejson(self):
        return {
            "course_name": self.courses.course_name,
            "course_id": self.course_id,
            "class_no": self.class_no,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "class_size": self.class_size,
            "trainer_name": self.trainer_name,
            "selfenrol_start": self.selfenrol_start,
            "selfenrol_end": self.selfenrol_end
        }

    def getSelfEnrolDates(self):
        
        return {
            "start": datetime.strftime(self.selfenrol_start, "%Y-%m-%d"), 
            "end": datetime.strftime(self.selfenrol_end, "%Y-%m-%d")
        }
    
    def setFinalQuiz(self, qid):
        self.finalquiz_id = qid
    
    @classmethod 
    def getAllClasses(cls):
        clslist = cls.query.all()
        return [
            a_class.coursejson()
         for a_class in clslist]

    @classmethod
    def setSelfEnrolDates(cls, data):
        target = classes.query.filter_by(course_id=data['course_id'], class_no=data['class_no']).first()
        target.selfenrol_start = data['selfenrol_start']
        target.selfenrol_end = data['selfenrol_end']
        db.session.commit()
        return {"updated": True}

    @classmethod
    def get_specificClass(cls,course_id, class_no):
        classobj = cls.query.filter_by(course_id= course_id, class_no = class_no).first()

        return {'data': classobj.json()}

    @classmethod
    def get_specificClassDetail(cls,course_id, class_no):
        classobj = cls.query.filter_by(course_id= course_id, class_no = class_no).first()
        return {'data': classobj.viewjson()}

    @classmethod
    def get_unassignedClass(cls):
        classesObj = cls.query.filter(cls.trainer_name == None).all()
        return {'data': [classObj.coursejson() for classObj in classesObj]}

    @classmethod
    def get_futureClass(cls):
        classesObj = cls.query.filter(cls.start_date > date.today()).all()
        return {'data': [classObj.coursejson() for classObj in classesObj]}

    @classmethod
    def modifyTrainer(cls, course_id, class_no, staff_username):
        classobj = cls.query.filter_by(course_id= course_id, class_no = class_no).first()
        classobj.trainer_name = staff_username
        db.session.commit()
        return {"data": "Updated"}

    @classmethod    
    def get_trainerAssignedClass(cls,staff_username):
        classesObj = cls.query.filter_by(trainer_name= staff_username).all()
        Classes = [classObj.coursejson() for classObj in classesObj]
        dicClass = collections.defaultdict(list)
        classlist = []
        for Class in Classes:
            dicClass[Class['course_name']].append(
                Class
            )

        for dickey in dicClass:
            classlist.append({dickey: dicClass[dickey]})

        return classlist