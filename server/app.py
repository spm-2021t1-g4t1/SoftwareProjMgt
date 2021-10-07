<<<<<<< Updated upstream
#Import external modules
from logging import exception
from flask import request, Flask
=======
# Import external modules
from flask import Flask, request, jsonify
>>>>>>> Stashed changes
from db import db
from flask_cors import CORS
import json
import platform


# Import your classes here
from static.model.staff import *
from static.model.course import *
from static.model.quiz import *
from static.model.classEnrollment_queue import *


app = Flask(__name__)
CORS(app)

configstr = "mysql+mysqlconnector://root@localhost:3306/lms"
if platform.system() == "Darwin":
    configstr = "mysql+mysqlconnector://root:root@localhost:3306/lms"

app.config["SQLALCHEMY_DATABASE_URI"] = configstr


@app.route("/staff")
def list_of_staff():
    return staff.get_staffList()


@app.route("/enrolment/<int:course_id>/<int:class_no>")
def getClasslist(course_id, class_no):
    return classEnrolment.getClasslist(course_id, class_no)


@app.route("/enrolment/<string:staff_username>")
def getStaff_Enrollment(staff_username):
    classEnrolments = {"data": []}
    ClassList = classEnrolment.getStaffEnrollment(staff_username)

    for classesObj in ClassList["data"].values():
        # print(classesObj)
        Courses = course.get_specificCourse(classesObj["course_id"])["data"]
        classObj = classes.get_specificClass(
            classesObj["course_id"], classesObj["class_no"]
        )["data"]

        classEnrolments["data"].append(
            {
                "course_id": Courses["course_id"],
                "course_name": Courses["course_name"],
                "description": Courses["description"],
                "classes": [classObj],
            }
        )

    return classEnrolments


@app.route("/course")
def get_all_course():
    return course.get_listOfCourse()


@app.route("/course/<int:course_id>")
def get_one_course(course_id):
    return course.get_specificCourse(course_id)

<<<<<<< Updated upstream
@app.route('/course/<int:course_id>/<int:class_no>' )
def get_specificCourseDetail(course_id,class_no):
    ClassDetail = {'data':[]}

    Courses = course.get_specificCourse(course_id)['data']
    classObj = classes.get_specificClassDetail(course_id,class_no)['data']
        
    ClassDetail['data'] ={
            'course_id' : Courses['course_id'],
            'course_name': Courses['course_name'],
            'description': Courses['description'],
            "learning_objective": Courses['learning_objective'],
            'classes': [classObj]
=======

@app.route("/course/<int:course_id>/<int:class_no>")
def get_specificCourseDetail(course_id, class_no):
    ClassDetail = {"data": []}

    Courses = course.get_specificCourse(course_id)["data"]
    classObj = classes.get_specificClassDetail(course_id, class_no)["data"]

    ClassDetail["data"] = {
        "course_id": Courses["course_id"],
        "course_name": Courses["course_name"],
        "description": Courses["description"],
        "learning_objective": Courses["learning_objective"],
        "classes": [classObj],
>>>>>>> Stashed changes
    }

    return ClassDetail
    
@app.route('/lesson/<int:course_id>/<int:class_no>/<string:staff_username>') ######
def get_lessons(course_id, class_no, staff_username):
    ClassDetail = {'data':[]}

    Courses = course.get_specificCourse(course_id)['data']
    classObj = classes.get_specificClassDetail(course_id,class_no)['data']
        

    all_lessons = lesson.get_allLessonByClass(course_id, class_no)['data']
    LessonDetail = {'data': []}
    LessonDetail['data'].append(all_lessons[0])
    curr_index = 0
    for each_lesson in all_lessons:
        material_count_for_current_lesson = len(each_lesson['lesson_materials'])
        list_of_material_viewed_by_staff = materials_viewed.get_listOfMaterialsViewedByStaff(course_id, class_no, each_lesson['lesson_no'], staff_username)['data']
        if material_count_for_current_lesson == len(list_of_material_viewed_by_staff) and material_count_for_current_lesson != 0:
            current_staff_quiz_score = quiz_attempts.get_listOfQuizAttemptsByStaff(course_id, class_no, staff_username)['data']['quiz_score']
            if current_staff_quiz_score >= 80 and curr_index+1 < len(all_lessons):   
                LessonDetail['data'].append(all_lessons[curr_index+1])
        curr_index = curr_index + 1
    
    classObj['lesson'] = LessonDetail['data']
    ClassDetail['data'] ={
            'course_id' : Courses['course_id'],
            'course_name': Courses['course_name'],
            'description': Courses['description'],
            "learning_objective": Courses['learning_objective'],
            'classes': [classObj]
    }
    
    
    return ClassDetail


@app.route("/quiz", methods=["POST", "GET"])
def get_all_quiz():
    return Quiz.get_listofQuiz()


@app.route("/quiz/<int:quiz_id>", methods=["POST", "GET"])
def get_spec_quiz(quiz_id):
    return Quiz.get_quiz_details(quiz_id)


@app.route("/quiz_ques/<int:qid>", methods=["POST", "GET"])
def get_all_ques(qid):
    # return json.loads(str(Question.get_courseQues(qid)))
    return Question.get_courseQues(qid)


<<<<<<< Updated upstream

@app.route('/queue/<string:staff_username>/<int:course_id>',  methods=['POST', 'GET'])
def get_classQueue(staff_username, course_id):
    if request.method == 'GET':
        return classEnrolmentQueue.getStaffQueue(staff_username, course_id)
    if request.method == 'POST':
        try:
            class_no = request.json['class_no']
            CE_Queue = classEnrolmentQueue(staff_username = staff_username, course_id = course_id, class_no = class_no)
            db.session.add(CE_Queue)
            db.session.commit()
            return {"Data": {"status": 200 , "message": "Enrollment successful"}}
        except:
            return {"Data": {"status": 400 ,"message": "Enrollment failed"}}
        # print(request.data)
        # class_no = request.json['class_no']
        # CE_Queue = classEnrolmentQueue(staff_username = staff_username, course_id = course_id, class_no = class_no)
        # db.session.add(CE_Queue)
        # db.session.commit()

# @app.route('/queue/add', )
=======
@app.route("/ques_opt/<int:quiz_id>/<int:ques_id>")
def get_the_options(quiz_id, ques_id):
    # return json.loads(str(Question.get_courseQues(qid)))
    return QuizOptions.get_QuesOpt(quiz_id, ques_id)


@app.route("/ques_opt_update/<int:quiz_id>/<int:ques_id>", methods=["POST"])
def update_options(quiz_id, ques_id):
    data = request.get_json()
    optionsList = data["optionsList"]
    question = data["question"]
    print(optionsList, question)

    try:
        ques = Question.query.filter_by(qid=quiz_id, ques_id=ques_id).first()
        ques.question = question
        db.session.commit()
    except:
        return jsonify({"code": 500, "message": "An error occurred."}), 500
    # return "Boop"

    for i in optionsList:
        optz = QuizOptions.query.filter_by(
            quiz_id=quiz_id, ques_id=ques_id, opts_id=i["opts_id"]
        ).first()
        print(i)
        print()
        try:
            optz.quiz_id = i["quiz_id"]
            optz.ques_id = i["ques_id"]
            optz.opts_id = i["opts_id"]
            optz.is_right = i["is_right"]
            optz.qopt = i["qopt"]
            db.session.commit()
        except:
            option = QuizOptions(
                quiz_id=i["quiz_id"],
                ques_id=i["ques_id"],
                opts_id=i["opts_id"],
                is_right=i["is_right"],
                qopt=i["qopt"],
            )
            db.session.add(option)
            db.session.commit()
    return "Boop"

>>>>>>> Stashed changes

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
    # just python app.py to execute
