from db import db

class Staff(db.Model):
    __tablename__ = "staff"

    staff_email = db.Column(db.String(255), primary_key=True)
    years_of_service = db.Column(db.Integer)

    def __init__(self, staff_email, years_of_service):
        self.staff_email = staff_email
        self.years_of_service = years_of_service
    
    def json(self):
        return {
            "staff_email": self.staff_email,
            "years_of_service": self.years_of_service
        }
