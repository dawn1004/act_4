
def menu():
    print("[1] ADD")
    print("[2] Search")
    print("[0] Exit")

    choice = input("")
    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "0":
        return True
    else:
        menu()


def add():
    print("##### Contact Person #####")
    print("----- Add New Contact -----")

    contact_person = input("Contact Name: ")
    contact_info = contact_person
    contact = ""
    while True:
        contact_type = input("Contact Type: ")
        if contact_type == "0":
            break
        if contact_type.lower() == "email":
            temp = input("email: ")
            while temp.isnumeric():
                print("please enter email format")
                temp = input("email: ")
            contact += "#email^" + temp
        elif contact_type.lower() == "mobile":
            temp = input("Mobile No.: ")
            while temp.isnumeric() == False:
                print("please enter Mobile Number format")
                temp = input("Mobile No.: ")
            contact += "#mobile^" + temp
        else:
            print("Only Accept Email and Mobile")

    whole_detail = contact_person + contact + "\n"

    file = open("group_data_section.txt", "a")
    file.write(whole_detail)
    file.close()


def search():
    print("##### Contact Person #####")
    print("----- Search Contact -----")

    user_input = input("Contact Name:")

    file = open("group_data_section.txt", "r")

    # looking for positions of searched
    x = 1
    pos = []
    for contact_details in file:
        if user_input.lower() in contact_details.split("#")[0].lower():
            pos.append(x)
        x += 1
    if len(pos) == 0:
        print("No records")
        menu()

    # displaying of the searched

    file.seek(0)
    contact_details = file.read().split("\n")
    num = 1
    for position in pos:
        print("[{}] {}".format(num, contact_details[position-1].split("#")[0]))
        num += 1
    # choosing in searched item
    choice = int(input(""))
    choice = pos[choice-1]
    file.close()
    displaySearchedItem(choice)


def displaySearchedItem(choice):
    print("##### Contact Person #####")
    print("----- Contact Details -----")

    file = open("group_data_section.txt", "r")

    chosen_details = file.read().split("\n")[choice-1]

    x = 1
    for contact_info in chosen_details.split("#"):
        if x == 1:
            print("\n Contact Name=> {} \n".format(contact_info))
        else:
            print("{} => {}".format(contact_info.split(
                "^")[0], contact_info.split("^")[1]))
        x += 1

    print("[1] Go back")
    print("[2] Update Contacts")
    print("[3] Delete Team")
    print("[0] Main menu")

    file.close()
    userinput = input("")
    if userinput == "1":
        search()
    elif userinput == "2":
        updateContacts(choice)
    elif userinput == "3":
        deleteContactPerson(choice)
    elif userinput == "0":
        menu()


def updateContacts(choice):
    file = open("group_data_section.txt", "r")

    oldcontact = file.read().split("\n")[choice-1]
    file.close()
    contacts = oldcontact.split("#")[1:]

    print("Contact name => {}".format(oldcontact.split("#")[0]))
    for contact in contacts:
        contact = contact.split("^")
        print("[{}] => {}".format(contact[0], contact[1]))

    userinput = input("Choice: ")
    NewContactDetail = input("New {}: ".format(userinput))
    temp = []
    for contact in contacts:
        contact = contact.split("^")
        if contact[0].lower() == userinput.lower():
            temp.append(contact[0]+"^"+NewContactDetail)
        else:
            temp.append(contact[0]+"^"+contact[1])

    final = oldcontact.split("#")[0]+"#"+temp[0]+"#"+temp[1]

    file = open("group_data_section.txt", "r")
    updated_content = file.read().replace(oldcontact, final)
    file.close()

    file = open("group_data_section.txt", "w")
    file.write(updated_content)
    file.close()
    print("Update Saved...!!")
    displaySearchedItem(choice)


def deleteContactPerson(choice):
    print("##### Contact Person #####")
    print("----- Delete Contact -----")

    file = open("group_data_section.txt", "r+")

    account_details = file.read().split("\n")[choice-1]

    contact_name = account_details.split("#")[0]
    print("Contact Name => {}".format(contact_name))

    userinput = input("Are you sure you want to proceed> [y/n]:")

    file.seek(0)
    upated_content = file.read()
    file.close()

    if userinput.lower() == "y":
        file = open("group_data_section.txt", "w")
        upated_content = upated_content.replace(account_details, "")
        print("deleted")
        file.write(upated_content)
        file.close()
        menu()
    else:
        displaySearchedItem(choice)


menu()


#     pos = lookForPosition(user_input)
#     print(pos)


# def lookForPosition(user_input):
#     file = open("group_data_section.txt", "r")
#     pos = 1

#     for contact_infos in file:
#         name_email_mobile_details = []
#         contact_infos = contact_infos.split("#")
#         name_email_mobile_details.append(contact_infos[0].lower())
#         for contact_info in contact_infos[1:]:
#             name_email_mobile_details.append(
#                 contact_info.split("^")[1].lower())

#         if user_input.lower() in name_email_mobile_details or user_input.lower()+"\n" in name_email_mobile_details:
#             return pos
#             break
#         pos += 1

#     # print(name_email_mobile_details)
#     # print(pos)
#     file.close()
