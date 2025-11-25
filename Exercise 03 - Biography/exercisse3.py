name = input("enter your full name: ")
hometown =input("enter your hometown: ")

while True:
    age_input = input("enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("please enter a valid number for age")
        
bio={"Name": name ,"Hometown" : hometown,"Age": age}
        
print(bio["Name"], bio["Hometown"], bio["Age"], sep="\n")        
    