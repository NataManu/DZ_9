
user_dict = {}


def input_error(func):
    def inner(input_list):
        try:
            result = func(input_list)
        except KeyError:
            result = "This name does not exist. Give me other name please."
        except ValueError:
            result = "ValueError."            
        except IndexError:
            if input_list[0] == "phone":
                result = "Give me name please"
            else:
                result = "Give me name and phone please."
        return result
    return inner


@input_error
def add_user(input_list):
    if user_dict.get(input_list[1])== None:
        user_dict[input_list[1]] = input_list[2]
        return "added"
    else:
        return f"Not added. Name {input_list[1]} already exist."


@input_error
def change_user(input_list):
    if user_dict.get(input_list[1]) != None:
        user_dict[input_list[1]] = input_list[2]
        return "changed"
    else:
        return f"Not changed. Name {input_list[1]} does not exist."


@input_error
def phone_user(input_list):
    return user_dict[input_list[1]]


def split_str(input_user_):
    input_split = input_user_.split(" ") 
    if input_split[0] not in ["add", "change", "phone"]:
        return "Command error"
    else:
        if input_split[0] == "add":
            return add_user(input_split)
        elif input_split[0] == "change":
            return change_user(input_split)
        else:
            return phone_user(input_split)


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
            continue

        print(split_str(input_user))

    
if __name__ == "__main__": 
    main()    