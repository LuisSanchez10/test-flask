from app import db, bcrypt
import datetime

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    nid = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=True)

    def __init__(self, email, password, confirmed,
                 admin=False, confirmed_on=None, phone_number=000000, nit=00000):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
        # self.nid = nid
        # self.phone_number = phone_number