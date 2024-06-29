from statistics import mean

users = {"Name": [""], "Birthday" : [0], "Gender" : [""]}
i= 0
ages = []
women = {"Name": [""], "Birthday" : [0], "Gender" : [""]}
men = {"Name": [""], "Birthday" : [0], "Gender" : [""]}
choice = 0
while(True):
    while(True):
        print("Select an Option: 1 - Add user, 2 - List users and information or 3 - Leave")
        try:
            choice = int(input("Type a number: "))
        except ValueError:
            print("Please, type a number.")
        if(choice<=0 or choice>= 4):
            print("Please, type a number between 1 and 3")
        else:
            break
    if(choice == 1):
        name = input("Type your name: ")
        genders = ["Male", "Female", "Other"]
        while(True):
            try:
                birthday = int(input("Type your year of birth: "))
                break
            except ValueError:
                print("Please, type a number.")
        print("Select your gender from the list: 1 - Male, 2 - Female or 3 - Other")
        while(True):
                try:
                    gender = int(input("Type a number to select your gender: "))
                except ValueError:
                    print("Please, type a number.")
                if(gender<=0 or gender>= 4):
                    print("Please, type a number between 1 and 3")
                else:
                    break
        if(i == 0):
            users["Birthday"][i] = birthday
            users["Gender"][i] = genders[gender-1]
            users["Name"][i] = name
        else:
            users["Birthday"].append(birthday)
            users["Gender"].append(genders[gender-1])
            users["Name"].append(name)
        i+=1
    
    elif(choice == 2):
        c = 0
        d= 0
        for b in range(len(users["Name"])):

            print(" ")
            ages.append(2024 - users['Birthday'][b])
            print(f"Number of users {len(users['Name'])}")
            print(f"Usuario {b+1}:")
            print(f"Name: {users['Name'][b]}")
            print(f"Birthday: {users['Birthday'][b]}")
            print(f"Gender: {users['Gender'][b]}")
            if(users['Gender'][b] == 'Female' and ages[b] <30):
                if(c == 0):
                    women["Birthday"][0] = users['Birthday'][b]
                    women["Name"][0] = users['Name'][b]
                    women["Gender"][0] = users['Gender'][b]
                else:
                    women["Birthday"].append(users['Birthday'][b])
                    women["Name"].append(users['Name'][b])
                    women["Gender"].append(users['Gender'][b])
            if(users['Gender'][b] == 'Male'):
                if(d == 0):
                    men["Birthday"][0] = int(users['Birthday'][b])
                    men["Name"][0] = users['Name'][b]
                    men["Gender"][0] = users['Gender'][b]
                else:
                    men["Birthday"].append(int(users['Birthday'][b]))
                    men["Name"].append(users['Name'][b])
                    men["Gender"].append(users['Gender'][b])
            d+=1
            c+=1
            print(" ")
        print(f"The number of users is {len(users['Name'])}")
        print(f"The average age of the users is {mean(ages)}")
        print(f"Men over the average age:")
        for b in range(len(men["Name"])):
            if(2024 - men['Birthday'][b]> mean(ages)):
                print(f"Name: {men['Name'][b]}")
                print(f"Birthday: {men['Birthday'][b]}")
                print(f"Gender: {men['Gender'][b]}")
                print(" ")
        print(f"Females under the age of 30: ")
        print(" ")
        for b in range(len(women["Name"])):
            print("reached")
            if(2024 - women['Birthday'][b] <30):
                print(f"Name: {women['Name'][b]}")
                print(f"Birthday: {women['Birthday'][b]}")
                print(f"Gender: {women['Gender'][b]}")
                print(" ")
        
    else:
        exit()