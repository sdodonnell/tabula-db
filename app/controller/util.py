import csv
from app import tabula
from app.models import Teacher, Student

# TODO: Add some protection here so that this isn't so easy to do.
@tabula.route('/seed')
def seed():
    Teacher.query.delete()
    Student.query.delete()
    with open('data/teachers.csv', newline='') as file:
        reader = csv.reader(file)

        try:
            for line in reader:
                first_name, last_name, email, pronouns = line
                teacher = Teacher(
                    first_name=first_name, last_name=last_name, email=email, pronouns=pronouns)
                teacher.save()
        except Exception as err:
            print(f"Error: {err=}, {type(err)=}")

    with open('data/students.csv', newline='') as file:
        reader = csv.reader(file)

        try:
            for line in reader:
                first_name, last_name, email, pronouns, year = line
                student = Student(first_name=first_name, last_name=last_name,
                                  email=email, pronouns=pronouns, year=year)
                student.save()
        except Exception as err:
            print(f"Error: {err=}, {type(err)=}")

    return f"Database successfully seeded."
