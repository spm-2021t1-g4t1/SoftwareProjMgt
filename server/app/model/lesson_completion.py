from db import db

class lesson_completion(db.Model):
    __tablename__ = 'lesson_completion'
    course_id = db.Column(db.Integer, primary_key=True)
    class_no = db.Column(db.Integer, primary_key=True)
    lesson_no = db.Column(db.Integer,  primary_key=True)
    staff_username = db.Column(db.String(255), primary_key=True) # It should be a PK

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['course_id', 'class_no', 'lesson_no'], ["lesson_materials.course_id",'lesson_materials.class_no', "lesson_materials.lesson_no"]
        ),
        db.ForeignKeyConstraint(
            ['staff_username'], ["staff.staff_username"]

        )
    )

    def json(self):
        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'lesson_no':self.lesson_no,
            'staff_username':self.staff_username

        }
    @classmethod
    def mark_lesson_completed(cls, lesson_completion):
        try:
            db.session.add(lesson_completion)
            db.session.commit()
            return {"code": 200, "message": "Lesson marked as complete"}
        except:
            return {"code": 400, "message": "Failed to mark lesson as complete"}
        

    @classmethod
    def get_listOfLessonCompletionByStaff(cls, course_id, class_no, staff_username):
        lesson_completion_list = cls.query.filter_by(course_id=course_id, class_no=class_no, staff_username=staff_username).all()
        print({'data': [one_lesson_completion.json() for one_lesson_completion in lesson_completion_list]})
        return {'data': [one_lesson_completion.json() for one_lesson_completion in lesson_completion_list]}