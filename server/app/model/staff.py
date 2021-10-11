from db import db

class staff(db.Model):
    __tablename__ = "staff"

    staff_username = db.Column(db.String(255), primary_key=True)
    staff_name = db.Column(db.String(255), primary_key=True)
    role = db.Column(db.Integer)
    department = db.Column(db.String(255))
    current_designation = db.Column(db.String(255))
    
    def viewjson(self):
        return {
            "staff_email": self.staff_username,
            "staff_name": self.staff_name,
            "role": self.role,
            "department": self.department,
            "current_designation": self.current_designation
        }

    @classmethod
    def get_staffList(cls):
        staffList = cls.query.all()
        return {'data': [staff.viewjson() for staff in staffList]}


