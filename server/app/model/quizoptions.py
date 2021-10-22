from db import db
from json import dumps, loads

class QuizOptions(db.Model):
    __tablename__ = "quiz_options"
    __table_args__ = {"extend_existing": True}
    quiz_id = db.Column(
        db.Integer, db.ForeignKey("quiz_questions.qid"), primary_key=True
    )
    ques_id = db.Column(
        db.Integer, db.ForeignKey("quiz_questions.ques_id"), primary_key=True
    )
    opts_id = db.Column(db.Integer, primary_key=True)
    qopt = db.Column(db.String(1000), primary_key=True)
    is_right = db.Column(db.Integer)

    def viewjson(self):
        return {
            "quiz_id": self.quiz_id,
            "ques_id": self.ques_id,
            "opts_id": self.opts_id,
            "qopt": self.qopt,
            "is_right": self.is_right,
        }
    
    @classmethod
    def get_QuesOpt(cls, quiz_id, ques_id):
        opts_bank = cls.query.filter_by(quiz_id=quiz_id, ques_id=ques_id)
        return {
            "data": [loads(dumps(opt.viewjson(), default=str)) for opt in opts_bank],
            "code": 200
        }

    @classmethod
    def remove_opt(cls, q_id, quid, oid):
        row_to_delete = QuizOptions.query.filter_by(
        quiz_id=q_id, ques_id=quid, opts_id=oid).first()
        db.session.delete(row_to_delete)
        db.session.commit()
        return {
            "data": "Removed",
            "code": 200
        }