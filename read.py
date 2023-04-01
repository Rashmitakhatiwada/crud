import json

def read(id):
    #read the students from file
    #filter the student from the list with provided id
    #print the result
    #continue or not
    with open("student.json", "r") as fp:
        students = json.load(fp)

    student = list(filter(lambda x: x['id'] == id, students))
    print(student[0])

    cont = input("Do you still want to continue? Y/N ")
    return True if cont.lower() =='y' else False
