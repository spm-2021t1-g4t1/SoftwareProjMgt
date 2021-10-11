from db import db
from json import dumps, loads


class Quiz(db.Model):
    __tablename__ = "quiz"
    __table_args__ = {"extend_existing": True}
    quiz_id = db.Column("quiz_id", db.Integer, primary_key=True)
    quiz_name = db.Column("quiz_name", db.String(255))
    description = db.Column("description", db.String(255))
    uploader = db.Column("uploader", db.String(255))
    duration = db.Column("duration", db.Time)
    questions = db.relationship("Question")

    def __init__(
        self, quiz_id="", quiz_name="", description="", uploader="", duration=""
    ):
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

    def viewjson(self):
        return {
            "quiz_id": self.quiz_id,
            "quiz_name": self.quiz_name,
            "description": self.description,
            "uploader": self.uploader,
            "duration": self.duration,
        }

    @classmethod
    def get_listofQuiz(cls):
        quizzes = cls.query.all()
        return {
            "data": [loads(dumps(quiz.viewjson(), default=str)) for quiz in quizzes]
        }

    @classmethod
    def get_quiz_details(cls, quiz_id):
        quiz_details = cls.query.filter_by(quiz_id=quiz_id)
        return {
            "data": [
                loads(dumps(quiz.viewjson(), default=str)) for quiz in quiz_details
            ]
        }


