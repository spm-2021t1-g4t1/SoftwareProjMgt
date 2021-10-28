# Import external modules
from flask import request, Flask, jsonify
from flask_cors import CORS
import platform


# Import your classes here
from db import db
from model import *

app = Flask(__name__)
CORS(app)

configstr = "mysql+mysqlconnector://root@localhost:3306/lms"
if platform.system() == "Darwin":
    configstr = "mysql+mysqlconnector://root:root@localhost:3306/lms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_size": 100, "pool_recycle": 280}
app.config["SQLALCHEMY_DATABASE_URI"] = configstr


############## Login ###############################################


@app.route("/login/<string:username>")
def get_staff_by_username(username):
    return staff.get_staff_by_username(username)


############## Staff ###############################################

@app.route("/staff")
def list_of_staff():
    return staff.get_staffList()

@app.route('/staff/engineers')
def list_of_engineers():
    return staff.get_engineerList()

############# Class Enrolment ######################################


@app.route("/enrolment/<int:course_id>/<int:class_no>")
def getClasslist(course_id, class_no):
    return classEnrolment.getClasslist(course_id, class_no)


@app.route("/enrolment/<int:course_id>/<int:class_no>/length")
def getClassNumber(course_id, class_no):
    class_number = len(classEnrolment.getClasslist(course_id, class_no)["data"])
    return jsonify({"code": 200, "message": class_number}), 200


@app.route("/enrolment/<string:staff_username>")
def getStaff_Enrollment(staff_username):
    classEnrolments = {"data": []}
    ClassList = classEnrolment.getStaffEnrollment(staff_username)

    for classesObj in ClassList["data"].values():
        Courses = course.get_specificCourse(classesObj["course_id"])["data"]
        classObj = classes.get_specificClass(
            classesObj["course_id"], classesObj["class_no"]
        )["data"]

        classEnrolments["data"].append(
            {
                "course_id": Courses["course_id"],
                "course_name": Courses["course_name"],
                "description": Courses["description"],
                "classes": [classObj]           
            }
        )

    return classEnrolments

@app.route("/enrolment/approve", methods=["POST"])
def ApproveEnrolment():
    data = request.json
    classEnrolmentQueue.removeQueue(data['staff_username'], data['course_id'])
    classEnrolment.enrollToClass(data['staff_username'], data['course_id'], data['class_no'])
    return data

############# Class Completion ######################################

@app.route('/eligiblity/<int:course_id>/<string:staff_username>')
def getStaffCompletion(course_id,staff_username):
    prereqCourses = course.get_prerequisite_courses(course_id)['data']
    completeObj = course_completion.getStaffCompletion(staff_username)
    # print(completeObj['data'])
    for completeCourse in completeObj['data'].values():
        if completeCourse['course_id'] in prereqCourses:
            prereqCourses.remove(completeCourse['course_id'])
    
    if len(prereqCourses) == 0:
        return {"eligiblity": True}
    return {"eligiblity": False}


############# Catalog ######################################

@app.route("/catalog/<string:staff_username>")
def get_all_course(staff_username):
    course_list = []
    alreadyEnrolledCourses = classEnrolment.getStaffEnrollment(staff_username)
    alreadyCompletedCourses = course_completion.getStaffCompletion(staff_username)
    for courseobj in alreadyEnrolledCourses["data"].values():
        course_list.append(courseobj["course_id"])
    for courseobj in alreadyCompletedCourses["data"].values():
        course_list.append(courseobj["course_id"])
    # print(course_list)
    return course.get_listOfCourse(course_list)

############# Queue ######################################

@app.route("/queue/<string:staff_username>/<int:course_id>", methods=["POST", "GET"])
def get_classQueue(staff_username, course_id):
    if request.method == "GET":
        return classEnrolmentQueue.getStaffQueue(staff_username, course_id)
    if request.method == "POST":
        try:
            class_no = request.json["class_no"]
            CE_Queue = classEnrolmentQueue(
                staff_username=staff_username, course_id=course_id, class_no=class_no
            )
            db.session.add(CE_Queue)
            db.session.commit()

            return jsonify({"code": 200, "message": "Enrollment succeed"}), 200
        except:
            return jsonify({"code": 400, "message": "Enrollment failed"}), 400


@app.route("/queue/withdraw" , methods=["POST"])
def withdraw_classQueue():
        try:
            staff_username = request.json["staff_username"]
            course_id = request.json["course_id"]

            CE_Queue = classEnrolmentQueue.query.filter_by(course_id= course_id, staff_username=staff_username).first()
            db.session.delete(CE_Queue)
            db.session.commit()

            return jsonify({"code": 200, "message": "Enrollment succeed"}), 200
        except:
            return jsonify({"code": 400, "message": "Enrollment failed"}), 400

# New function (probably no test yet)
@app.route('/queue/getList/')
def get_enrollmentRequest():
    return classEnrolmentQueue.getStaffRequest()
    
############# Course ######################################


@app.route("/course/<int:course_id>")
def get_one_course(course_id):
    return course.get_specificCourse(course_id)


@app.route("/course/<int:course_id>/<int:class_no>")
def get_specificCourseDetail(course_id, class_no):
    ClassDetail = {"data": []}

    Courses = course.get_specificCourse(course_id)["data"]
    classObj = classes.get_specificClass(course_id, class_no)["data"]

    ClassDetail["data"] = {
        "course_id": Courses["course_id"],
        "course_name": Courses["course_name"],
        "description": Courses["description"],
        "learning_objective": Courses["learning_objective"],
        "classes": [classObj],
    }
    return ClassDetail

############# Lesson ######################################
 
@app.route("/lesson/<int:course_id>/<int:class_no>/<string:staff_username>")
def get_lessons(course_id, class_no, staff_username):
    # lessonDetail = {"data": []}

    # Courses = course.get_specificCourse(course_id)["data"]
    # classObj = classes.get_specificClassDetail(course_id, class_no)["data"]

    all_lessons = lesson.get_allLessonByClass(course_id, class_no)["data"]
    LessonDetail = {"data": []}
    LessonDetail["data"].append(all_lessons[0])

    list_of_lessons_completed_by_staff = lesson_completion.get_listOfLessonCompletionByStaff(course_id, class_no, staff_username)["data"]
    list_of_quiz_attempts_by_staff = quiz_attempts.get_listOfQuizAttemptsByStaff(course_id, class_no, staff_username)["data"]
    completed_lesson_no_list = []
    for each_completed_lesson in list_of_lessons_completed_by_staff:
        completed_lesson_no_list.append(each_completed_lesson['lesson_no'])
    most_recent_lesson_completed = 0    
    if len(completed_lesson_no_list) > 0:
        most_recent_lesson_completed = max(completed_lesson_no_list)  

    for index in range(0, len(all_lessons)): 
        if index + 1 != len(all_lessons):
            lesson_no = all_lessons[index]['lesson_no']
            if most_recent_lesson_completed + 1 >= lesson_no+1:
                for attempt in list_of_quiz_attempts_by_staff:
                    if attempt["lesson_no"] == lesson_no:
                        if attempt["quiz_score"] >= 80:
                            LessonDetail['data'].append(all_lessons[index+1])
                        

    # classObj["lesson"] = LessonDetail["data"]
    # ClassDetail["data"] = {
    #     "course_id": Courses["course_id"],
    #     "course_name": Courses["course_name"],
    #     "description": Courses["description"],
    #     "learning_objective": Courses["learning_objective"],
    #     "classes": [classObj],
    # }

    return LessonDetail

@app.route("/lesson_completion/mark_complete", methods=["POST"])
def mark_lesson_as_complete():
    class_info = request.get_json()
    lesson_completion_object = lesson_completion(
        course_id=class_info['course_id'], 
        class_no=class_info['class_no'], 
        lesson_no=class_info['lesson_no'], 
        staff_username=class_info['staff_username'])

    result = lesson_completion.mark_lesson_completed(lesson_completion_object)
    
    return result

@app.route("/lesson_completion/<int:course_id>/<int:class_no>/<string:staff_username>", methods=["GET"])
def get_lessonCompletion(course_id,class_no,staff_username):
    lessonCompletion = lesson_completion.get_listOfLessonCompletionByStaff(course_id, class_no, staff_username)
    return lessonCompletion


############# Quiz ######################################


@app.route("/quiz", methods=["POST", "GET"])
def get_all_quiz():
    return Quiz.get_listofQuiz()


@app.route("/insert_quiz", methods=["POST", "GET"])
def insert_quiz():
    data = request.get_json()
    addQuiz = Quiz(
        quiz_id=data["quiz_id"],
        quiz_name=data["quiz_name"],
        description=data["description"],
        uploader=data["uploader"],
        duration=data["duration"],
    )
    db.session.add(addQuiz)
    db.session.commit()
    return {"data": {"status": 200, "message": "Quiz is successfully created"}}


@app.route("/quiz/<int:quiz_id>", methods=["POST", "GET"])
def get_spec_quiz(quiz_id):
    return Quiz.get_quiz_details(quiz_id)


@app.route("/quiz_ques/<int:qid>", methods=["POST", "GET"])
def get_all_ques(qid):
    return Question.get_courseQues(qid)


@app.route("/get_spec_quiz_ques/<int:qid>/<int:ques_id>", methods=["POST", "GET"])
def get_specific_ques(qid, ques_id):
    return Question.get_a_question(qid, ques_id)


@app.route("/ques_opt/<int:quiz_id>/<int:ques_id>")
def get_the_options(quiz_id, ques_id):
    return QuizOptions.get_QuesOpt(quiz_id, ques_id)


@app.route("/add_ques/<int:quiz_id>", methods=["POST"])
def addQuestion(quiz_id):
    # return json.loads(str(Question.get_courseQues(qid)))
    questions = Question.get_courseQues(quiz_id)
    # print(len(questions["data"]))
    data = request.get_json()
    if data["ques_id"] == len(questions["data"]) + 1:
        Question.add_courseQuestion(
            quiz_id,
            data["ques_id"],
            data["question"],
            data["question_type"],
        )
        return {"data": {"status": 200, "message": "Question Added successful"}}
    else:
        return {"data": {"status": 500, "message": "Question NOT added"}}


@app.route("/ques_opt_update/<int:quiz_id>/<int:ques_id>", methods=["POST"])
def update_options(quiz_id, ques_id):
    data = request.get_json()
    optionsList = data["optionsList"]
    question = data["question"]
    Question.update_specificQuestion(quiz_id, ques_id, question)
    # Question.query.filter_by(qid=quiz_id, ques_id=ques_id).first()
    for i in optionsList:
        x = QuizOptions.get_specificOption(
            quiz_id=quiz_id, ques_id=ques_id, opts_id=i["opts_id"]
        )
        if x["data"] is not None:
            QuizOptions.update_quiz_options(
                i["quiz_id"], i["ques_id"], i["opts_id"], i["is_right"], i["qopt"]
            )
        else:
            QuizOptions.insert_quiz_options(
                i["quiz_id"], i["ques_id"], i["opts_id"], i["is_right"], i["qopt"]
            )
    return {
        "data": {
            "status": 200,
            "message": "Questions and Options updated Successfully!",
            "data": Question.get_a_question(quiz_id, ques_id),
        }
    }


@app.route(
    "/ques_opt_delete/<int:quiz_id>/<int:ques_id>/<int:opts_id>",
    methods=["POST", "GET"],
)
def delete_options(quiz_id, ques_id, opts_id):
    QuizOptions.remove_opt(quiz_id, ques_id, opts_id)
    return {"data": {"status": 200, "message": "Options Deleted successful"}}


@app.route(
    "/quiz_delete/<int:quiz_id>",
    methods=["POST", "GET"],
)
def delele_quiz(quiz_id):
    try:
        Quiz.delete_quiz(quiz_id)
        return {"data": {"status": 200, "message": "Quiz deleted successful"}}
    except:
        return {"data": {"status": 500, "message": "Error in deleting quiz"}}


@app.route("/ques_delete/<int:quiz_id>/<int:ques_id>", methods=["POST", "GET"])
def delete_questions(quiz_id, ques_id):
    Question.remove_question(quiz_id, ques_id)
    QuizOptions.remove_all_opt(quiz_id, ques_id)
    return {"data": {"status": 200, "message": "Question Deleted successful"}}


@app.route("/quiz_update/<int:quiz_id>", methods=["POST", "GET"])
def save_quiz(quiz_id):
    try:
        data = request.get_json()
        Quiz.save_quiz(
            quiz_id,
            data["quiz_name"],
            data["description"],
            data["uploader"],
            data["duration"],
        )
        return {"data": {"status": 200, "message": "Saved Quiz successful"}}
    except:
        return {"data": {"status": 500, "message": "Quiz cant be saved successful"}}


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
