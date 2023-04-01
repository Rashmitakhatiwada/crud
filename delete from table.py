from establish_connection import establish_connection

cursor = establish_connection()
sql ="""
delete from new_students
"""

cursor.execute(sql)
print("data deleted successfully !!")