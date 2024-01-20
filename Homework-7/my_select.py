from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Groups, Students, Teachers, Subjects, Grades, Base


engine = create_engine("postgresql://postgres:mysecretpassword@localhost:5432/postgres")
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    result = (
        session.query(Students.name, func.avg(Grades.value).label("average_grade"))
        .join(Grades)
        .group_by(Students.id)
        .order_by(func.avg(Grades.value).desc())
        .limit(5)
        .all()
    )
    return result


def select_2(subject_name):
    result = (
        session.query(Students.name, func.avg(Grades.value).label("average_grade"))
        .join(Grades)
        .join(Subjects)
        .filter(Subjects.name == subject_name)
        .group_by(Students.id)
        .order_by(func.avg(Grades.value).desc())
        .first()
    )
    return result


def select_3(subject_name):
    result = (
        session.query(Groups.name, func.avg(Grades.value).label("average_grade"))
        .join(Students, Groups.students)
        .join(Grades, Students.grades)
        .join(Subjects)
        .filter(Subjects.name == subject_name)
        .group_by(Groups.name)
        .all()
    )
    return result


def select_4():
    result = session.query(func.avg(Grades.value).label("average_grade")).scalar()
    return result


def select_5(teacher):
    result = (
        session.query(Subjects.name).join(Teachers).filter(Teachers.id == teacher).all()
    )
    return result


def select_6(group_id):
    result = (
        session.query(Students.name).join(Groups).filter(Groups.id == group_id).all()
    )
    return result


def select_7(groud_id, subject_name):
    result = (
        session.query(Students.name, Grades.value)
        .join(Groups)
        .join(Grades)
        .join(Subjects)
        .filter(Groups.id == groud_id, Subjects.name == subject_name)
        .all()
    )
    return result


def select_8(teacher_name):
    result = (
        session.query(func.avg(Grades.value).label("average_grade"))
        .join(Subjects)
        .join(Teachers)
        .filter(Teachers.name == teacher_name)
        .scalar()
    )
    return result


def select_9(student_id):
    result = (
        session.query(Subjects.name)
        .join(Grades)
        .join(Students)
        .filter(Students.id == student_id)
        .all()
    )
    return result


def select_10(student_id, teacher_id):
    result = (
        session.query(Subjects.name)
        .join(Grades)
        .join(Students)
        .join(Teachers)
        .filter(
            Students.id == student_id,
            Teachers.id == teacher_id,
            Subjects.id == Grades.subject_id,
            Subjects.teacher_id == Teachers.id,
        )
        .all()
    )
    return result


def additional_select_1(teacher_id, student_id):
    result = (
        session.query(func.avg(Grades.value))
        .join(Subjects, Grades.subject_id == Subjects.id)
        .join(Teachers, Subjects.teacher_id == Teachers.id)
        .join(Students, Grades.student_id == Students.id)
        .filter(Teachers.id == teacher_id, Students.id == student_id)
        .scalar()
    )
    return result


def additional_select_2(group_id, subject_id):
    result = (
        session.query(Grades.value)
        .join(Subjects, Grades.subject_id == Subjects.id)
        .join(Students, Grades.student_id == Students.id)
        .join(Groups, Students.group_id == Groups.id)
        .filter(Groups.id == group_id, Subjects.id == subject_id)
        .order_by(Grades.date_received)
        .limit(1)
        .all()
    )
    return result


# Example usage in your print_query_results function
def print_query_results(query_function, *args):
    print(f"Running query {query_function.__name__}:")
    result = query_function(*args)
    print("Query Result:")

    if isinstance(result, list):
        for row in result:
            print(row)
    elif isinstance(result, tuple):
        print(result)
    elif result is not None:
        print(result)
    else:
        print("No result found.")
    print()


print_query_results(additional_select_2, 1, 1)
