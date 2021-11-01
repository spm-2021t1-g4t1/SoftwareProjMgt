from db import db

#-----------------------------------------------------------------------------------------------------------------------#
class lesson_quiz_attempts(db.Model):
    __tablename__ = 'lesson_quiz_attempts'
    course_id = db.Column(db.Integer, primary_key=True)
    class_no = db.Column(db.Integer, primary_key=True)
    lesson_no = db.Column(db.Integer,  primary_key=True)
    staff_username = db.Column(db.String(255))
    quiz_score = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['course_id', 'class_no', "lesson_no"], ["lesson.course_id",'lesson.class_no', "lesson.lesson_no"]
        ),
    )

    def json(self):
        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'lesson_no':self.lesson_no,
            'staff_username':self.staff_username,
            'quiz_score':self.quiz_score
        }
    @classmethod
    def get_listOfQuizAttemptsByStaff(cls, course_id, class_no, staff_username):
        attempts = cls.query.filter_by(course_id=course_id, class_no=class_no,staff_username=staff_username).all()
        return {'data': [one_attempt.json() for one_attempt in attempts]}

    @classmethod
    def get_specificLessonQuizAttempt(cls, course_id, class_no, lesson_no, staff_username):
        attempt = cls.query.filter_by(course_id=course_id, class_no=class_no,lesson_no=lesson_no,staff_username=staff_username).first()
        return {'data': attempt.json()}


