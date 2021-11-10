from db import db
class learningObjective(db.Model):
    __tablename__ ="learning_objective"
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    learning_objective = db.Column(db.String(255),  primary_key=True)

    def viewstring(self):
        return self.learning_objective
