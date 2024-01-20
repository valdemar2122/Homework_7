import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Students, Teachers, Groups

engine = create_engine("postgresql://postgres:mysecretpassword@localhost:5432/postgres")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# CREATE / LIST / UPDATE / REMOVE


# CRUD FOR MODEL TEACHER
def create_teacher(name):
    new_teacher = Teachers(name=name)
    session.add(new_teacher)
    session.commit()
    print(f"Teacher {name} created successfully")


def list_teachers():
    teachers_list = session.query(Teachers).all()
    for teacher in teachers_list:
        print(f"Teachers ID: {teacher.id}, Teacher's name: {teacher.name}")


def update_teacher(teacher_id, new_name):
    teacher = session.query(Teachers).get(teacher_id)
    if teacher:
        teacher.name = new_name
        session.commit()
        print(f"Teacher with ID {teacher_id} updated successfully ")
    else:
        print(f"Teacher with ID {teacher_id} not found ")


def remove_teacher(teacher_id):
    teacher = session.query(Teachers).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher with ID {teacher_id} removed successfully ")
    else:
        print(f"Teacher with ID {teacher_id} not found ")


# CRUD FOR MODEL Students


def create_student(name):
    new_student = Students(name=name)
    session.add(new_student)
    session.commit()
    print(f"Student {name} created successfully")


def list_students():
    students_list = session.query(Students).all()
    for student in students_list:
        print(f"Student ID: {student.id}, Student's name: {student.name}")


def update_student(student_id, new_name):
    student = session.query(Students).get(student_id)
    if student:
        student.name = new_name
        session.commit()
        print(f"Student with ID {student_id} updated successfully ")
    else:
        print(f"Student with ID {student_id} not found ")


def remove_student(student_id):
    student = session.query(Students).get(student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Student with ID {student_id} removed successfully ")
    else:
        print(f"Student with ID {student_id} not found ")


# CRUD FOR MODEL Groups


def create_group(name):
    new_group = Groups(name=name)
    session.add(new_group)
    session.commit()
    print(f"Group {name} created successfully")


def list_groups():
    group_list = session.query(Groups).all()
    for group in group_list:
        print(f"Group ID: {group.id}, Group's name: {group.name}")


def update_group(group_id, new_name):
    group = session.query(Groups).get(group_id)
    if group:
        group.name = new_name
        session.commit()
        print(f"Group with ID {group_id} updated successfully ")
    else:
        print(f"Group with ID {group_id} not found ")


def remove_group(group_id):
    group = session.query(Groups).get(group_id)
    if group:
        session.delete(group)
        session.commit()
        print(f"Group with ID {group_id} removed successfully ")
    else:
        print(f"Group with ID {group_id} not found ")


def main():
    parser = argparse.ArgumentParser(
        description="CLI programm to manage CRUD operations"
    )
    parser.add_argument(
        "--action",
        "-a",
        choices=["create", "list", "update", "remove"],
        required=True,
        help="CRUD Actions to perform",
    )
    parser.add_argument(
        "--model",
        "-m",
        choices=["Teachers"],
        required=True,
        help="Model on which to perform operation",
    )
    parser.add_argument("--name", "-n", help="Name of the entity to create or update")
    parser.add_argument(
        "--id", "-i", type=int, help="ID of the entity to update or remove"
    )

    args = parser.parse_args()

    if args.action == "create":
        if args.model == "Teachers":
            create_teacher(args.name)
        elif args.model == "Students":
            create_student(args.name)
        elif args.model == "Groups":
            create_group(args.name)

    elif args.action == "list":
        if args.model == "Teachers":
            list_teachers()
        elif args.model == "Students":
            list_students()
        elif args.model == "Groups":
            list_groups()

    elif args.action == "update":
        if args.model == "Teachers":
            update_teacher(args.id, args.name)
        elif args.model == "Students":
            update_student(args.id, args.name)
        elif args.model == "Groups":
            update_group(args.id, args.name)

    elif args.action == "remove":
        if args.model == "Teachers":
            remove_teacher(args.id)
        elif args.model == "Students":
            remove_student(args.id)
        elif args.model == "Groups":
            remove_group(args.id)


if __name__ == "__main__":
    main()
