first_name= input("Enter first name:")
last_name= input("Enter last name:")
age=input("Enter your age:")

username = first_name[:3].lower() + "_" +last_name.lower() + age
print("username:",username)