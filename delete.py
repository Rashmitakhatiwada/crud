import json
filename = "student.json"

def delete(id):
    with open(filename, "r") as fp:
        students = json.load(fp)

    student = list(filter(lambda x: x['id'] == id, students))[0]

    students.remove(student)

    with open(filename, 'w') as fp:
        json.dump(students, fp, indent=2 )

    cont = input("the student has been removed. do you still want to continue? Y/N ")
    return True if cont.lower() =='y' else False