from db import db

#-----------------------------------------------------------------------------------------------------------------------#
class course(db.Model):
    __tablename__ ="course"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    learning_objective = db.relationship('learningObjective', backref='course', lazy = True)
    classes = db.relationship('classes', backref='course', lazy = True)

    def view_all_json(self):
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
    
    def json(self):
        learn_obj = []
        for index,learning in enumerate(self.learning_objective):
            learn_obj.append(learning.viewstring())

        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "description": self.description,
            "learning_objective": learn_obj,
        }

    @classmethod
    def get_listOfCourse(cls,course_list):
        courses = cls.query.filter(cls.course_id.notin_(course_list))
        return {'data': [one_course.view_all_json() for one_course in courses]}

    @classmethod
    def get_specificCourse(cls,course_id):
        courses = cls.query.filter_by(course_id= course_id).first()
        return {'data': courses.json()}

#-----------------------------------------------------------------------------------------------------------------------#

class learningObjective(db.Model):
    __tablename__ ="learning_objective"
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    learning_objective = db.Column(db.String(255),  primary_key=True)

    def viewstring(self):
        return self.learning_objective




