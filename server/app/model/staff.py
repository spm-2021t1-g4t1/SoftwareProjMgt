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
            "staff_username": self.staff_username,
            "staff_name": self.staff_name,
            "role": self.role,
            "department": self.department,
            "current_designation": self.current_designation
        }


    @classmethod
    def get_staffList(cls):
        staffList = cls.query.all()
        return {'data': [staff.viewjson() for staff in staffList]}

    @classmethod
    def get_staff_by_username(cls, username):
        staffDAO = cls.query.filter_by(staff_username = username).first()
        if staffDAO is None: return {'data': None}
        # print(staffDAO)
        login_staff = {
            "staff_username": staffDAO.staff_username,
            "role": staffDAO.role
        }
        return {'data': login_staff}

    @classmethod
    def get_engineerList(cls):
        staffDAO = cls.query.filter(cls.role.notin_(['Administrator']))
        return {'data': [one_staff.viewjson() for one_staff in staffDAO]}
