from db import db

#-----------------------------------------------------------------------------------------------------------------------#
class course(db.Model):
    __tablename__ ="course"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    learning_objective = db.relationship('learningObjective', backref='course', lazy = True)
    classes = db.relationship('classes', backref='course', lazy = True)
    prerequisite_courses = db.relationship('course_prerequisite', uselist=True,foreign_keys=[course_id], primaryjoin='(course_prerequisite.course_id == course.course_id)', lazy = True)

    def view_all_json(self):
        learn_obj = []
        for index,learning in enumerate(self.learning_objective):
            learn_obj.append(learning.viewstring())
        
        all_classes = []
        for one_class in self.classes:
            all_classes.append(one_class.viewjson())

        prerequisite_courses = []
        for prereq_course in self.prerequisite_courses:
            prerequisite_courses.append(prereq_course.json())

        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "description": self.description,
            "learning_objective": learn_obj,
            "prerequisite_courses": prerequisite_courses,
            "classes": all_classes,
        }
    
    def view_catalog_json(self):
        learn_obj = []
        for index,learning in enumerate(self.learning_objective):
            learn_obj.append(learning.viewstring())
        
        all_classes = []
        for one_class in self.classes:
            all_classes.append(one_class.coursejson())

        prerequisite_courses = []
        for prereq_course in self.prerequisite_courses:
            prerequisite_courses.append(prereq_course.json())

        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "description": self.description,
            "learning_objective": learn_obj,
            "prerequisite_courses": prerequisite_courses,
            "classes": all_classes,
        }

    
    def json(self):
        learn_obj = []
        for index,learning in enumerate(self.learning_objective):
            learn_obj.append(learning.viewstring())
        
        prerequisite_courses = []
        for prereq_course in self.prerequisite_courses:
            prerequisite_courses.append(prereq_course.json())

        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "description": self.description,
            "learning_objective": learn_obj,
            "prerequisite_courses": prerequisite_courses
        }

    @classmethod
    def get_listOfCourse(cls,course_list):
        courses = cls.query.filter(cls.course_id.notin_(course_list))
        return {'data': [one_course.view_catalog_json() for one_course in courses]}

    @classmethod
    def get_specificCourse(cls,course_id):
        courses = cls.query.filter_by(course_id= course_id).first()
        return {'data': courses.json()}

    @classmethod
    def get_prerequisite_courses(cls,course_id):
        prerequisite_courses = []
        courses = cls.query.filter_by(course_id= course_id).first()
        for prereq in courses.json()['prerequisite_courses']:
            prerequisite_courses.append(prereq["prerequisite_course_id"])
        
        return {"data": prerequisite_courses}

#-----------------------------------------------------------------------------------------------------------------------#

class learningObjective(db.Model):
    __tablename__ ="learning_objective"
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    learning_objective = db.Column(db.String(255),  primary_key=True)

    def viewstring(self):
        return self.learning_objective

#-----------------------------------------------------------------------------------------------------------------------#

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


