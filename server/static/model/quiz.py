from db import db

class Quiz(db.Model):
    __tablename__ = 'quiz'
    __table_args__ = {'extend_existing': True}
    quiz_id = db.Column('quiz_id', db.Integer, primary_key = True)
    quiz_name = db.Column('quiz_name', db.String(255))
    description = db.Column('description', db.String(255))
    uploader = db.Column('uploader', db.String(255))
    duration = db.Column('duration', db.Time)
    questions = db.relationship('Question')

    def __init__(self, quiz_id="", quiz_name="", description="", uploader="", duration=""):      
        self.quiz_id = quiz_id
        self.quiz_name = quiz_name
        self.description = description
        self.uploader = uploader
        self.duration = duration


    def getQuiz_id(self):
        return self.quiz_id
    
    def getQuiz_name(self):
        return self.quiz_name
    
    def getDescription(self):
        return self.description

    def getUploader(self):
        return self.uploader

    def getDuration(self):
        return self.duration


    def json(self):
        return {"quiz_id": self.quiz_id, 
        "quiz_name": self.quiz_name, 
        "description": self.description, 
        "uploader": self.uploader,
        "duration": self.duration}

# class Quiz(db.Model):
#     __tablename__ = "quiz"
#     __table_args__ = {'extend_existing': True}
#     quiz_id = db.Column(db.Integer, primary_key=True)
#     quiz_name = db.Column(db.String(255))
#     description = db.Column(db.String(1000))
#     uploader = db.Column(db.String(255))
#     questions = db.relationship('Question', backref='quiz', lazy=True)

    # def __repr__(self):
    #     return '<Quiz %r>' % self.quiz_id

    # def viewjson(self):
    #     questions = []
    #     for index, question in enumerate(self.questions):
    #         questions.append(question.viewjson())

    #     return {
    #         "quiz_id": self.quiz_id,
    #         "quiz_name": self.quiz_name,
    #         "description": self.description,
    #         "uploader": self.uploader,
    #         "questions": questions
    #     }


class Question(db.Model):
    __tablename__ = "quiz_questions"
    __table_args__ = {'extend_existing': True}
    qid = db.Column(db.Integer, db.ForeignKey(
        'quiz.quiz_id'), primary_key=True)
    ques_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    question_type = db.Column(db.String(255))
    options = db.relationship('QuizOptions', primaryjoin="and_(Question.qid==QuizOptions.qid, Question.ques_id==QuizOptions.ques_id)", lazy='dynamic')

    def getQid(self):
        return self.qid
    
    def getQues_id(self):
        return self.ques_id
    
    def getQuestion(self):
        return self.question

    def getQuestion_type(self):
        return self.question_type

    def json(self):
        return {
            "qid": self.qid, 
        "ques_id": self.ques_id, 
        "question": self.question, 
        "question_type": self.question_type
        }
    # def viewjson(self):
    #     options = []
    #     for index, option in enumerate(self.options):
    #         options.append(option.viewjson())
    #     return {
    #         'qid': self.qid,
    #         'ques_id': self.ques_id,
    #         'question': self.question,
    #         'question_type': self.question_type,
    #         'options': options
    #     }
        

class QuizOptions(db.Model):
    __tablename__ = "quiz_options"
    qid = db.Column(db.Integer, db.ForeignKey('quiz_questions.qid'), primary_key=True)
    ques_id = db.Column(db.Integer, db.ForeignKey('quiz_questions.ques_id'), primary_key=True)
    optionz = db.Column(db.String(1000), primary_key=True)
    is_right = db.Column(db.Integer)


    def viewjson(self):
        return {
            'qid': self.qid,
            'ques_id': self.ques_id,
            'optionz': self.optionz,
            'is_right': self.is_right
        }
