from db import db

class lesson_materials(db.Model):
    __tablename__ = 'lesson_materials'
    course_id = db.Column(db.Integer, primary_key=True)
    class_no = db.Column(db.Integer, primary_key=True)
    lesson_no = db.Column(db.Integer,  primary_key=True)
    course_material_title = db.Column(db.String(255), primary_key=True)
    link = db.Column(db.String(255))


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
            'course_material_title':self.course_material_title,
            'link':self.link,
        }



