from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Groups, Students, Teachers, Subjects, Grades, Base
from datetime import datetime, timedelta
import random

fake = Faker()

# Create engine here
engine = create_engine("postgresql://postgres:mysecretpassword@localhost:5432/postgres")
Base.metadata.create_all(bind=engine)

# create session here

Session = sessionmaker(bind=engine)
session = Session()

# create GROUPS
groups = [Groups(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# create STUDENTS
students = [Students(name=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# create TEACHERS
teachers = [Teachers(name=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

# create SUBJECTS
subjects = [
    Subjects(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)
]
session.add_all(subjects)
session.commit()

# create GRADES
grades = []

for student in students:
    for subject in subjects:
        # Генеруємо випадкову оцінку від 1 до 10
        grade_value = random.randint(1, 10)

        # Генеруємо випадкову дату, коли була отримана оцінка (останні 30 днів)
        grade_date = datetime.now() - timedelta(days=random.randint(1, 30))

        # Створюємо об'єкт Grade і додаємо його до списку grades
        grade = Grades(
            value=grade_value,
            date_received=grade_date,
            subject=subject,
            student=student,
        )
        grades.append(grade)

# Додаємо оцінки до сесії
session.add_all(grades)
session.commit()
