import json

password = input("set your password")
data = {"password": password }

with open("password.json",'w') as fp:
    json.dump(data, fp, indent=2)
print("password added successful")



