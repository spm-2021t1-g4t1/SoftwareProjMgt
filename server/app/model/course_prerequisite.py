from db import db

class course_prerequisite(db.Model):
    __tablename__ = "course_prerequisite"
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    prerequisite_course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    prerequisite_course_name = db.relationship('course', foreign_keys=[prerequisite_course_id])



    def json(self):
        # print()
        return {
            "course_id": self.course_id,
            "prerequisite_course_id": self.prerequisite_course_id,
            "prerequisite_course_name":self.prerequisite_course_name.json()['course_name']
        }
