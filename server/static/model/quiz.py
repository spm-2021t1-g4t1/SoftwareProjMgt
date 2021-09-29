from db import db


class Quiz(db.Model):
    __tablename__ = "quiz"
    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(255))
    description = db.Column(db.String(1000))
    uploader = db.Column(db.String(255))
    questions = db.relationship('Question', backref='quiz', lazy=True)

    def __repr__(self):
        return '<Quiz %r>' % self.quiz_id

    def viewjson(self):
        questions = []
        for index, question in enumerate(self.questions):
            questions.append(question.viewjson())

        return {
            "quiz_id": self.quiz_id,
            "quiz_name": self.quiz_name,
            "description": self.description,
            "uploader": self.uploader,
            "questions": questions
        }


class Question(db.Model):
    __tablename__ = "quiz_questions"
    qid = db.Column(db.Integer, db.ForeignKey(
        'quiz.quiz_id'), primary_key=True)
    ques_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    question_type = db.Column(db.String(255))
    options = db.relationship('QuizOptions', primaryjoin="and_(Question.qid==QuizOptions.qid, Question.ques_id==QuizOptions.ques_id)", lazy='dynamic')

    def viewjson(self):
        options = []
        for index, option in enumerate(self.options):
            options.append(option.viewjson())
        return {
            'qid': self.qid,
            'ques_id': self.ques_id,
            'question': self.question,
            'question_type': self.question_type,
            'options': options
        }


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
