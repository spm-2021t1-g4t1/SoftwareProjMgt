from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from model.classEnrollment_queue import *
from model.classEnrollment import *
from model.classes import *
from model.course import *
from model.lesson import *
from model.materials_viewed import *
from model.quiz_attempts import *
from model.quiz import *
from model.question import *
from model.quizoptions import *
from model.staff import *


