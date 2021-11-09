from db import db
from json import dumps, loads


class QuizOptions(db.Model):
    __tablename__ = "quiz_options"
    __table_args__ = {"extend_existing": True}
    qid = db.Column(db.Integer, db.ForeignKey("quiz_questions.qid"), primary_key=True)
    ques_id = db.Column(
        db.Integer, db.ForeignKey("quiz_questions.ques_id"), primary_key=True
    )
    opts_id = db.Column(db.Integer, primary_key=True)
    qopt = db.Column(db.String(1000), primary_key=True)
    is_right = db.Column(db.Integer)

    __table_args__ = (
        db.ForeignKeyConstraint(
            ["qid", "ques_id"], ["quiz_questions.qid", "quiz_questions.ques_id"]
        ),
    )

    def viewjson(self):
        return {
            "qid": self.qid,
            "ques_id": self.ques_id,
            "opts_id": self.opts_id,
            "qopt": self.qopt,
            "is_right": self.is_right,
        }

    @classmethod
    def get_QuesOpt(cls, quiz_id, ques_id):
        opts_bank = cls.query.filter_by(qid=quiz_id, ques_id=ques_id)
        return {
            "data": [loads(dumps(opt.viewjson(), default=str)) for opt in opts_bank],
            "code": 200,
        }

    @classmethod
    def get_specificOption(cls, quiz_id, ques_id, opts_id):
        data = cls.query.filter_by(
            qid=quiz_id, ques_id=ques_id, opts_id=opts_id
        ).first()
        if data is not None:
            return {"data": loads(dumps(data.viewjson(), default=str)), "code": 200}
        else:
            return {"data": None, "code": 500}

    @classmethod
    def remove_opt(cls, q_id, quid, oid):
        row_to_delete = cls.query.filter_by(qid=q_id, ques_id=quid, opts_id=oid).first()
        db.session.delete(row_to_delete)
        db.session.commit()
        return {"data": "Removed", "code": 200}

    @classmethod
    def update_quiz_options(cls, quiz_id, ques_id, opts_id, is_right, qopt):
        row_to_updates = cls.query.filter_by(
            qid=quiz_id, ques_id=ques_id, opts_id=opts_id
        )
        for row_to_update in row_to_updates:
            row_to_update.quiz_id = quiz_id
            row_to_update.ques_id = ques_id
            row_to_update.opts_id = opts_id
            row_to_update.is_right = is_right
            row_to_update.qopt = qopt

        db.session.commit()
        return {"data": "Updated", "code": 200}

    @classmethod
    def insert_quiz_options(cls, quiz_id, ques_id, opts_id, is_right, qopt):
        option = QuizOptions(
            qid=quiz_id,
            ques_id=ques_id,
            opts_id=opts_id,
            is_right=is_right,
            qopt=qopt,
        )
        db.session.add(option)
        db.session.commit()
        return {"data": "Inserted", "code": 200}

    @classmethod
    def remove_all_opt(cls, q_id, quid):
        rows_to_delete = cls.query.filter_by(qid=q_id, ques_id=quid)
        for i in rows_to_delete:
            db.session.delete(i)
        db.session.commit()
        return {"data": "Removed", "code": 200}
