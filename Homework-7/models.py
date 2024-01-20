from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    students = relationship("Students", back_populates="group")


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Groups", back_populates="students")
    grades = relationship("Grades", back_populates="student")


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subjects = relationship("Subjects", back_populates="teacher")


class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teachers", back_populates="subjects")
    grades = relationship("Grades", back_populates="subject")


class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    date_received = Column(DateTime, default=datetime.now())
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    subject = relationship("Subjects", back_populates="grades")
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Students", back_populates="grades")
