from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    modified_date = Column(DateTime, default=datetime.now, nullable=False)

    jobs = relationship('Job', back_populates='user')
    departments = relationship('Department', back_populates='chief_user')

    def __repr__(self):
        return f"<Colonist> {self.id} {self.surname} {self.name}"


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey('users.id'), nullable=False)
    team_leader_user = relationship(
        'User',
        foreign_keys=[team_leader],
        back_populates='jobs'
    )
    job = Column(String, nullable=False)
    work_size = Column(Integer, nullable=False)
    collaborators = Column(String)
    start_date = Column(DateTime, default=datetime.now, nullable=False)
    end_date = Column(DateTime)
    is_finished = Column(Boolean, default=False, nullable=False)

    user = relationship('User', back_populates='jobs')

    def __repr__(self):
        return f"<Job> {self.job}"


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    chief = Column(Integer, ForeignKey('users.id'), nullable=False)
    members = Column(String)  # List of user IDs stored as comma-separated string
    email = Column(String, nullable=False)

    chief_user = relationship('User', back_populates='departments')

    def __repr__(self):
        return f"<Department> {self.title}"
