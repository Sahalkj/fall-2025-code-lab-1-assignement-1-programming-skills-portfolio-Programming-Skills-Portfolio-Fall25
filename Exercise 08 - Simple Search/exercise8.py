list=["Jake","Zac","Ian","Ron","Sam","Dave"]
search_name="Sam"
#Checking if the name "Sam" is in the list
if search_name in list:
    print("The name",search_name, "found in the list")
#Asking user for thew name that should be searched in the list
user_input=input("Enter the name to be searched:") 
#Checking if the given name is in the list
if user_input.capitalize() in list: 
        print("The name",user_input,"has been found in the list") 
else:
        print("no name found in the list")
        