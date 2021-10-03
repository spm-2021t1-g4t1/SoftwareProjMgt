from db import db

#-----------------------------------------------------------------------------------------------------------------------#
class course(db.Model):
    __tablename__ ="course"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    learning_objective = db.relationship('learningObjective', backref='course', lazy = True)
    classes = db.relationship('classes', backref='course', lazy = True)

    def viewjson(self):
        learn_obj = []
        for index,learning in enumerate(self.learning_objective):
            learn_obj.append(learning.viewstring())
        
        all_classes = []
        for one_class in self.classes:
            all_classes.append(one_class.viewjson())

        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "description": self.description,
            "learning_objective": learn_obj,
            "classes": all_classes
        }


    @classmethod
    def get_listOfCourse(cls):
        courses = cls.query.all()
        return {'data': [one_course.viewjson() for one_course in courses]}

    @classmethod
    def get_specificCourse(cls,course_id):
        courses = cls.query.filter_by(course_id= course_id).first()
        return {'data': [one_course.viewjson() for one_course in courses]}


#-----------------------------------------------------------------------------------------------------------------------#
class learningObjective(db.Model):
    __tablename__ ="learning_objective"
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    learning_objective = db.Column(db.String(255),  primary_key=True)

    def viewstring(self):
        return self.learning_objective


class classes(db.Model):
    __tablename__ ="classes"
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
    class_no = db.Column(db.Integer)
    start_date  = db.Column(db.DateTime)
    end_date  = db.Column(db.DateTime)
    start_time  = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    class_size   = db.Column(db.Integer)
    trainer_name  = db.Column(db.String(255), db.ForeignKey('staff.staff_email'), nullable=True)
    section = db.relationship('lesson', backref='classes', lazy = True)
    
    __table_args__ = (
    db.PrimaryKeyConstraint(
        course_id, class_no,
        ),
    )


    def viewjson(self):
        section_obj = []
        for section in self.section:
            section_obj.append(section.viewjson())
        
        return {
            "course_id": self.course_id,
            "class_no": self.class_no,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "start_time": str(self.start_time),
            "end_time": str(self.end_time),
            "class_size": self.class_size,
            "trainer_name": self.trainer_name,
            'section' : section_obj
        }

#-----------------------------------------------------------------------------------------------------------------------#
class lesson(db.Model):
    __tablename__ = 'lesson'
    course_id = db.Column(db.Integer, primary_key=True)
    class_no = db.Column(db.Integer, primary_key=True)
    lesson_no = db.Column(db.Integer, primary_key=True)
    lesson_name = db.Column(db.String(255))
    lesson_description = db.Column(db.String(255))
    lesson_materials = db.relationship('lesson_materials', backref='lesson', lazy = True)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['course_id', 'class_no'], ["classes.course_id",'classes.class_no']
        ),
    )

    def viewjson(self):
        lesson_mat_obj = []
        for lesson_material in self.lesson_materials:
            lesson_mat_obj.append(lesson_material.viewjson())

        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'lesson_no':self.lesson_no,
            'lesson_name': self.lesson_name,
            'lesson_description':self.lesson_description,
            'lesson_materials': lesson_mat_obj
        }

#-----------------------------------------------------------------------------------------------------------------------#
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

    def viewjson(self):
        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'lesson_no':self.lesson_no,
            'course_material_title':self.course_material_title,
            'link':self.link
        }