from establish_connection import establish_connection

cursor = establish_connection()
sql = """
select * from new_students
"""

cursor.execute(sql)
result = cursor.fetchall()
print(result)
