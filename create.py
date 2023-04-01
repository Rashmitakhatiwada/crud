import os
import json

import decorator
from decorator import pass_require
filename = "student.json"

@pass_require
def create():
    id = input("enter the id of a student ")
    name = input("enter the name of a student ")
    department = input("enter the department ")

    student = dict(id= id,name= name,department=department)
    if os.path.exists(filename):
        with open(filename, "r") as fp:
            students = json.load(fp)
    else:
        students = []

    students.append(student)

    with open(filename, 'w') as fp:
        json.dump(students, fp, indent=2 )
    cont = input("a new student is added. do you still want to continue? Y/N ")
    return True if cont.lower() =='y' else False
    # if cont.lower() == y:
    #     return true
    # else:
    #     return false