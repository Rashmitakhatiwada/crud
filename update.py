import json
filename = "student.json"

def update(id, to_change, value):
    #read students from file
    #filter the student using id
    #Change the student data using to_change and value
    #write the student data
    #cont or not
    with open(filename, "r") as fp:
        students = json.load(fp)

    student = list(filter(lambda x: x['id'] == id, students))
    student=student[0]

    index_of_student = students.index(student)
    students[index_of_student][to_change]=value

    with open(filename, 'w') as fp:
        json.dump(students, fp, indent=2 )

    cont = input("the student has been updated. do you still want to continue? Y/N ")
    return True if cont.lower() =='y' else False