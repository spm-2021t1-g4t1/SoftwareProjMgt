from db import db

#-----------------------------------------------------------------------------------------------------------------------#
class final_quiz_attempts(db.Model):
    __tablename__ = 'final_quiz_attempts'
    course_id = db.Column(db.Integer, primary_key=True)
    class_no = db.Column(db.Integer, primary_key=True)
    staff_username = db.Column(db.String(255))
    quiz_score = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['course_id', 'class_no'], ["classes.course_id",'classes.class_no']
        ),
    )

    def json(self):
        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'staff_username':self.staff_username,
            'quiz_score':self.quiz_score
        }

    @classmethod
    def get_specificFinalQuizAttempt(cls, course_id, class_no, staff_username):
        try:
            attempt = cls.query.filter_by(course_id=course_id, class_no=class_no,staff_username=staff_username).first()
            return {'data': attempt.json(), 'code': 200}
        except:
            return {'data': None, 'code': 404}

    
    @classmethod
    def update_finalquizscore(cls, course_id, class_no, staff_username, quiz_score):
            if(cls.query.filter_by(course_id=course_id, class_no=class_no, staff_username=staff_username).first()):
                try:
                    row_to_update = cls.query.filter_by(course_id=course_id, class_no=class_no, staff_username=staff_username).first()
                    row_to_update.quiz_score = quiz_score
                    db.session.commit()
                    return {'data': quiz_score, 'code': 200}
                except:
                    return {'data': None, 'code': 500}
            else:
                attempt = final_quiz_attempts(
                    course_id = course_id,
                    class_no = class_no,
                    staff_username = staff_username,
                    quiz_score = quiz_score
                )
                db.session.add(attempt)
                db.session.commit()
                return {'data': quiz_score, 'code': 200}



