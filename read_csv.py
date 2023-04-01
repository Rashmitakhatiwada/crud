import csv
import json

def read_csv():
    with open("data.csv" , 'r') as fp :
        reader= csv.reader(fp, delimiter=',')
        students = []
        for index, data in enumerate(reader):
            if index==0:
                continue
            # print(data)
            each ={
                "id": data[0],
                "name": data[1],
                "departments": data[2],
            }
            students.append(each)

    return students

    # print(students)

# with open("first_five.csv",'w') as fp:
#     data = students[:5]
#     json.dump(data, fp, indent=2)
# print("data added successful")

