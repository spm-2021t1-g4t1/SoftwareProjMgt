from db import db

#-----------------------------------------------------------------------------------------------------------------------#
class materials_viewed(db.Model):
    __tablename__ = 'materials_viewed'
    course_id = db.Column(db.Integer, primary_key=True)
    class_no = db.Column(db.Integer, primary_key=True)
    lesson_no = db.Column(db.Integer,  primary_key=True)
    course_material_title = db.Column(db.String(255), primary_key=True)
    staff_username = db.Column(db.String(255), primary_key=True) # It should be a PK

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['course_id', 'class_no', "lesson_no", "course_material_title"], ["lesson_materials.course_id",'lesson_materials.class_no', "lesson_materials.lesson_no", "lesson_materials.course_material_title"]
        ),
    )

    def json(self):
        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'lesson_no':self.lesson_no,
            'course_material_title':self.course_material_title,
            'staff_username':self.staff_username

        }
    @classmethod
    def get_listOfMaterialsViewedByStaff(cls, course_id, class_no, lesson_no, staff_username):
        materials = cls.query.filter_by(course_id=course_id, class_no=class_no, lesson_no=lesson_no, staff_username=staff_username).all()
        return {'data': [one_material.json() for one_material in materials]}
