import json

def pass_require(func):
    def inner_func(*args,**kwargs):

        b=""
        b = input("enter your password")
        with open("password.json", "r") as fp:
            pw = json.load(fp)

        if b in pw['password']:
            print("access given")
            return func(*args, **kwargs)
        else:
            print("you do not have an excess")


    return inner_func


# @pass_require
# def password_check():
#     print("hello world")
#
# password_check()