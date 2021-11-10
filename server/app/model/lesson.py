from db import db
from json import dumps, loads

#-----------------------------------------------------------------------------------------------------------------------#
class lesson(db.Model):
    __tablename__ = 'lesson'
    course_id = db.Column(db.Integer, primary_key=True)
    class_no = db.Column(db.Integer, primary_key=True)
    lesson_no = db.Column(db.Integer, primary_key=True)
    lesson_name = db.Column(db.String(255))
    lesson_description = db.Column(db.String(255))
    lesson_materials = db.relationship('lesson_materials', backref='lesson', lazy = True)
    quiz_assigned_id = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['course_id', 'class_no'], ["classes.course_id",'classes.class_no']
        ),
    )

    def json(self):
        lesson_mat_obj = []
        for lesson_material in self.lesson_materials:
            lesson_mat_obj.append(lesson_material.json())

        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'lesson_no':self.lesson_no,
            'lesson_name': self.lesson_name,
            'lesson_description':self.lesson_description,
            'lesson_materials': lesson_mat_obj,
            'quiz_assigned_id': self.quiz_assigned_id

        }
    
    @classmethod
    def get_allLessonByClass(cls, course_id, class_no):
        lessons = cls.query.filter_by(course_id=course_id, class_no=class_no).all()
        return {'data': [one_lesson.json() for one_lesson in lessons]}

    @classmethod
    def get_specificLesson(cls,course_id,class_no, lesson_no):
        lessonobj = cls.query.filter_by(course_id=course_id,class_no=class_no,lesson_no=lesson_no).first()
        return {'data': lessonobj.json()}

    @classmethod
    def get_all_lessons(cls):
        lessons = cls.query.all()
        return {
            "data": [loads(dumps(lesson.json(), default=str)) for lesson in lessons],
            "code": 200,
        }

    @classmethod
    def get_lesson_of_quiz(cls, quiz_assigned_id):
        if(cls.query.filter_by(quiz_assigned_id=quiz_assigned_id).first()):
            data = cls.query.filter_by(quiz_assigned_id=quiz_assigned_id).first()
            return {
                    "data": data.json(),
                    "code": 200,
                }
        else:
            return {
                    "data": None,
                    "code": 200,
                }
    @classmethod
    def get_quiz_for_lesson(cls, course_id, class_no, lesson_no):
        row_to_take = cls.query.filter_by(course_id=course_id, class_no=class_no, lesson_no=lesson_no).first()
        return row_to_take.quiz_assigned_id
                

    @classmethod
    def save_quiz_to_lesson(cls, course_id, class_no, lesson_no, quiz_assigned_id):
        if(cls.query.filter_by(quiz_assigned_id=quiz_assigned_id).first()):
            rows_to_update = cls.query.filter_by(quiz_assigned_id=quiz_assigned_id)
            for row in rows_to_update:
                row.quiz_assigned_id = 0
            lessons_to_update = cls.query.filter_by(course_id=course_id, class_no=class_no, lesson_no=lesson_no)
            for lesson in lessons_to_update:
                lesson.quiz_assigned_id = quiz_assigned_id
            db.session.commit()
            return {
                "data": cls.query.filter_by(course_id=course_id, class_no=class_no, lesson_no=lesson_no).first().json(),
                "code": 200,
            }
        else:
            lesson = cls.query.filter_by(course_id=course_id, class_no=class_no, lesson_no=lesson_no).first()
            lesson.quiz_assigned_id = quiz_assigned_id
            db.session.commit()
            return {
                "data": cls.query.filter_by(course_id=course_id, class_no=class_no, lesson_no=lesson_no).first().json(),
                "code": 200,
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

    def json(self):
        return {
            'course_id':self.course_id,
            'class_no':self.class_no,
            'lesson_no':self.lesson_no,
            'course_material_title':self.course_material_title,
            'link':self.link,
        }



#-----------------------------------------------------------------------------------------------------------------------#
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