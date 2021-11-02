from db import db

#-----------------------------------------------------------------------------------------------------------------------#
class course_completion(db.Model):
    __tablename__ ="course_completion"
    course_id = db.Column(db.Integer, primary_key=True)
    staff_username = db.Column(db.String(255), primary_key=True)
  
    def json(self):
        return {
            "course_id": self.course_id,
            "staff_username": self.staff_username
        }
    
    @classmethod
    def insert_course_completion(cls, course_completion):
        try:
            db.session.add(course_completion)
            db.session.commit()
            return {"code": 200, "message": "Course marked as complete"}
        except:
            return {"code": 400, "message": "Failed to mark course as complete"}

    @classmethod
    def getStaffCompletion(cls, staff_username):
        ClassListDAO = cls.query.filter_by(staff_username = staff_username).all()
        classList = {'data':{}}
        for index, classes in enumerate(ClassListDAO):
            classList['data'][index] = classes.json()
        return classList
    
    @classmethod
    def getCompletionByCourse(cls, course_id):
        result = cls.query.filter_by(course_id=course_id).all()
        resultList = []
        for index, course in enumerate(result):
            resultList.append({"staff_username": course.json()["staff_username"]})
        return resultList
