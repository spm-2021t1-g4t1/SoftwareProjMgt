from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import environ
from flask_cors import CORS
import json

from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='root', server='localhost', database='LMS')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Quiz(db.Model):
    __tablename__ = 'quiz'

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
    

class Question(db.Model):
    __tablename__ = 'quiz_questions'

    qid = db.Column('qid', db.Integer, db.ForeignKey('quiz.quiz_id'), primary_key = True)
    ques_id = db.Column('ques_id', db.Integer, primary_key = True)
    question = db.Column('question', db.String(255))
    question_type = db.Column('question_type', db.String(255))

    def __init__(self, qid="", ques_id="", question="", question_type=""):
        self.qid = qid
        self.ques_id = ques_id
        self.question = question
        self.question_type = question_type

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



@app.route('/quiz', methods=['POST', 'GET'])
def get_all():
    quiz = Quiz.query.all()
    json_thing = {
        "code": 200,
        "data": {
            "quiz": [q.json() for q in quiz]
        }
    }

    return json.dumps(json_thing, default=str)

@app.route('/quiz_ques/<int:qid>', methods=['POST', 'GET'])
def get_all_ques(qid):
    ques = Question.query.filter_by(qid=qid).all()
    json_thing = {
        "code": 200,
        "data": {
            "ques": [q.json() for q in ques]
        }
    }

    return json.dumps(json_thing, default=str)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


