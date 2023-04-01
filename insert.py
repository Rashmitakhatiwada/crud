from establish_connection import establish_connection
from read_csv import read_csv

data = read_csv()
cursor = establish_connection()

for each in data[:3]:
    id = each['id']
    name = each['name']
    departments = each['departments']

    # print(each)

    sql = f"""
    insert into new_students(ID,NAME,departments)
    VALUES('{id}','{name}','{departments}')
    """

    cursor.execute(sql)
    print("data inserted successfully")