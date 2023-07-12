
user_dict = {}


def input_error(func):
    def inner(user_str):
        try:
            result = func(user_str)
        except KeyError:
            result = "This name does not exist. Give me other name please."
        except ValueError:
            if user_str.startswith("phone"):
                result = "Give me name please"
            else:
                result = "Give me name and phone please."            
        except IndexError:
            if user_str.startswith("phone"):
                result = "Give me name please"
            else:
                result = "Give me name and phone please."
        return result
    return inner


@input_error
def add_user(user_str):
    user_split = user_str.split(" ") 
    if user_split[0] != "add" or user_split[1] == "":
        return "Enter:add 'name' 'phone'"
    if user_dict.get(user_split[1])== None:
        user_dict[user_split[1]] = user_split[2]
        res = "added"
    else:
        res = f"Do not added. Name {user_split[1]} already exist."
    return res


@input_error
def change_user(user_str):
    user_split = user_str.split(" ") 
    if user_split[0] != "change" or user_split[1] == "":
        return "Enter:change 'name' 'phone'"
    if user_dict.get(user_str.split(" ")[1]) != None:
        user_dict[user_str.split(" ")[1]] = user_str.split(" ")[2]
        res = "changed"
    else:
        res = f"Do not changed. Name {user_split[1]} does not exist."
    return res


@input_error
def phone_user(user_str):
    user_split = user_str.split(" ")
    if user_split[0] != "phone":
        return "Enter:phone 'name'"
    res = user_dict[user_split[1]]
    return res


def main(): 
    print("Hello!")
    
    while True:
        input_user = str(input(">>>")).lower().strip()
        if input_user == "hello":
            input_user = input("How can I help you?>>>").lower().strip()
        if input_user in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        if input_user ==("show all"):
            print(user_dict)
        if input_user.startswith("add") == True:
            print(add_user(input_user))
        if input_user.startswith("change") == True:
            print(change_user(input_user))
        if input_user.startswith("phone") == True:
            print(phone_user(input_user))

    
if __name__ == "__main__": 
    main()    

