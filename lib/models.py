from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base, relationship

from datetime import datetime

# naming convention
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

meta = MetaData(naming_convention=convention)

# declarative_base
Base = declarative_base(metadata=meta)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    date = Column(DateTime(), default=datetime.now())

    workouts = relationship("Workout", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


class Workout(Base):
    __tablename__ = "workouts"


    id = Column(Integer, primary_key=True)
    
    date = Column(DateTime(), default=datetime.now())
    workout_name = Column(String, nullable=False)
    notes = Column(Text, nullable=True)
    intensity = Column(Float)

    user_id = Column(Integer, ForeignKey("users.id")) 

    user = relationship("User", back_populates="workouts")
    exercises = relationship("Exercise", back_populates="workout")

    def __repr__(self):
        return f"<Workout(id={self.id}, name={self.name}, date={self.date})>"
    


class Exercise(Base):
    __tablename__ = "exercises"


    id = Column(Integer, primary_key=True)
    date = Column(DateTime(), default=datetime.now())
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # e.g., cardio, strength, mobility
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float, nullable=True)
    duration = Column(Integer)  # in minutes

    workout_id = Column(Integer, ForeignKey("workouts.id"))

    workout = relationship("Workout", back_populates="exercises")

    def __repr__(self):
        return f"<Exercise(id={self.id}, name={self.name}, type={self.type})>"




    
