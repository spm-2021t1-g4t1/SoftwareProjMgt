from db import db
from json import dumps, loads

class Question(db.Model):
    __tablename__ = "quiz_questions"
    __table_args__ = {"extend_existing": True}
    qid = db.Column(db.Integer, db.ForeignKey("quiz.quiz_id"), primary_key=True)
    ques_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    question_type = db.Column(db.String(255))

    def getQid(self):
        return self.qid

    def getQues_id(self):
        return self.ques_id

    def getQuestion(self):
        return self.question

    def getQuestion_type(self):
        return self.question_type

    def viewjson(self):
        return {
            "qid": self.qid,
            "ques_id": self.ques_id,
            "question": self.question,
            "question_type": self.question_type,
        }

    @classmethod
    def get_courseQues(cls, qid):
        questionsbank = cls.query.filter_by(qid=qid)
        return {
            "data": [
                loads(dumps(ques.viewjson(), default=str)) for ques in questionsbank
            ],
            "code": 200,
        }

    @classmethod
    def get_a_question(cls, qid, ques_id):
        ques = cls.query.filter_by(qid=qid, ques_id=ques_id).first()
        return {
            "data": 
                loads(dumps(ques.viewjson(), default=str)),
            "code": 200,
        }


